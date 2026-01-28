import os
import asyncio
import uuid
import discord
from discord.ext import tasks
from dotenv import load_dotenv
from status_messages import STATUS_MESSAGES

load_dotenv()

bot_instances: dict[str, "VegapunkBot"] = {}
broadcast_messages: list[tuple[str, str, str | None, bool, int]] = []
broadcast_lock = asyncio.Lock()

AUTHORISED_USER_IDS: set[int] = set()
_auth_ids = os.getenv("AUTHORISED_USER_IDS", "")
if _auth_ids:
    AUTHORISED_USER_IDS.update(
        int(uid.strip()) for uid in _auth_ids.split(",") if uid.strip()
    )

BOT_CONFIG = [
    ("Shaka", "SHAKA_TOKEN"),
    ("Lilith", "LILITH_TOKEN"),
    ("Edison", "EDISON_TOKEN"),
    ("Pythagoras", "PYTHAGORAS_TOKEN"),
    ("Atlas", "ATLAS_TOKEN"),
    ("York", "YORK_TOKEN"),
]

STATUS_CYCLE_INTERVAL = 60
MAX_MESSAGE_LENGTH = 2000
ALLOWED_MENTIONS = discord.AllowedMentions.none()


def validate_broadcast_content(content: str) -> tuple[bool, str]:
    """Validate message content before broadcasting."""
    content = content.strip()
    if len(content) == 0:
        return False, "Message cannot be empty"
    if len(content) > MAX_MESSAGE_LENGTH:
        return False, f"Message too long (max {MAX_MESSAGE_LENGTH} characters)"
    return True, content


class VegapunkBot(discord.Client):
    def __init__(self, name: str, channel_id: int):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        super().__init__(intents=intents)
        self.bot_name = name
        self.channel_id = channel_id
        self.status_index = 0
        self.messages = STATUS_MESSAGES.get(name, ["Online"])
        self.processed_message_ids: set[str] = set()

    async def setup_hook(self):
        self.cycle_status.start()
        self.check_broadcast.start()

    async def on_ready(self):
        print(f"[{self.bot_name}] Logged in as {self.user}")
        bot_instances[self.bot_name] = self
        await self.set_status()

    async def set_status(self):
        message = self.messages[self.status_index]
        activity = discord.CustomActivity(name=message)
        await self.change_presence(status=discord.Status.online, activity=activity)
        print(f"[{self.bot_name}] Status: {message}")

    @tasks.loop(seconds=STATUS_CYCLE_INTERVAL)
    async def cycle_status(self):
        self.status_index = (self.status_index + 1) % len(self.messages)
        await self.set_status()

    @cycle_status.before_loop
    async def before_cycle(self):
        await self.wait_until_ready()

    async def on_message(self, message: discord.Message):
        if (
            isinstance(message.channel, discord.DMChannel)
            and message.author != self.user
        ):
            if AUTHORISED_USER_IDS and message.author.id not in AUTHORISED_USER_IDS:
                await message.reply("You are not authorised to use this bot.")
                print(
                    f"[{self.bot_name}] Unauthorised: "
                    f"{message.author.name} ({message.author.id})"
                )
                return

            message_id = str(uuid.uuid4())
            content = message.content

            if content.lower().startswith("/all "):
                actual_content = content[5:].strip()

                if actual_content.lower().startswith("/"):
                    await message.reply("Cannot use commands after /all prefix.")
                    return

                valid, result = validate_broadcast_content(actual_content)
                if not valid:
                    await message.reply(f"Invalid message: {result}")
                    return

                target_bot_name = None
                is_all_broadcast = True
                async with broadcast_lock:
                    broadcast_messages.append(
                        (
                            message_id,
                            actual_content,
                            target_bot_name,
                            is_all_broadcast,
                            0,
                        )
                    )
                await message.reply("Broadcast sent to all bots.")
            elif content.lower() == "/help":
                help_text = """Available Commands:
/all <message> - Send message from all 6 bots
/help - Show this help message
<any text> - Send message only from this bot"""
                await message.reply(help_text)
            else:
                valid, result = validate_broadcast_content(content)
                if not valid:
                    await message.reply(f"Invalid message: {result}")
                    return

                target_bot_name = self.bot_name
                is_all_broadcast = False
                async with broadcast_lock:
                    broadcast_messages.append(
                        (
                            message_id,
                            content,
                            target_bot_name,
                            is_all_broadcast,
                            0,
                        )
                    )
                await message.reply("Message sent.")

    async def send_broadcast(self, content: str) -> bool:
        try:
            valid, result = validate_broadcast_content(content)
            if not valid:
                print(f"[{self.bot_name}] Invalid message: {result}")
                return False
            channel = self.get_channel(self.channel_id)
            if channel and isinstance(channel, discord.TextChannel):
                await channel.send(result, allowed_mentions=ALLOWED_MENTIONS)
                print(f"[{self.bot_name}] Broadcast sent to channel {self.channel_id}")
                return True
            else:
                print(
                    f"[{self.bot_name}] ERROR - Invalid channel ID: {self.channel_id}"
                )
                return False
        except Exception as e:
            print(f"[{self.bot_name}] ERROR sending broadcast: {e}")
            return False

    @tasks.loop(seconds=1)
    async def check_broadcast(self):
        async with broadcast_lock:
            for (
                message_id,
                content,
                target_bot_name,
                is_all_broadcast,
                processed_count,
            ) in broadcast_messages:
                if message_id not in self.processed_message_ids:
                    if is_all_broadcast or target_bot_name == self.bot_name:
                        await self.send_broadcast(content)
                        self.processed_message_ids.add(message_id)
                        index = next(
                            i
                            for i, msg in enumerate(broadcast_messages)
                            if msg[0] == message_id
                        )
                        broadcast_messages[index] = (
                            message_id,
                            content,
                            target_bot_name,
                            is_all_broadcast,
                            processed_count + 1,
                        )

                        if processed_count + 1 >= 6:
                            broadcast_messages.pop(index)

    @check_broadcast.before_loop
    async def before_check_broadcast(self):
        await self.wait_until_ready()


async def run_bot(name: str, token: str, channel_id: int):
    bot = VegapunkBot(name, channel_id)
    try:
        await bot.start(token)
    except discord.LoginFailure:
        print(f"[{name}] FAILED - Invalid token!")
    except Exception as e:
        print(f"[{name}] Error: {e}")


async def main():
    print("Starting Vegapunk Satellite Bots...")
    print("=" * 50)

    broadcast_channel_id = os.getenv("BROADCAST_CHANNEL_ID")
    if not broadcast_channel_id:
        print("WARNING - No BROADCAST_CHANNEL_ID found in .env")
        print("Broadcast functionality will be disabled.")
        channel_id = 0
    else:
        channel_id = int(broadcast_channel_id)

    tasks_list = []
    for name, env_var in BOT_CONFIG:
        token = os.getenv(env_var)
        if token:
            tasks_list.append(run_bot(name, token, channel_id))
        else:
            print(f"[{name}] WARNING - No token found in {env_var}")

    if tasks_list:
        await asyncio.gather(*tasks_list)
    else:
        print("No valid tokens found. Check your .env file.")


if __name__ == "__main__":
    asyncio.run(main())
