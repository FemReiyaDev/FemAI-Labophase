import os
import asyncio
import discord
from discord.ext import tasks
from dotenv import load_dotenv
from status_messages import STATUS_MESSAGES

load_dotenv()

BOT_CONFIG = [
    ("Shaka", "SHAKA_TOKEN"),
    ("Lilith", "LILITH_TOKEN"),
    ("Edison", "EDISON_TOKEN"),
    ("Pythagoras", "PYTHAGORAS_TOKEN"),
    ("Atlas", "ATLAS_TOKEN"),
    ("York", "YORK_TOKEN"),
]

STATUS_CYCLE_INTERVAL = 60


class VegapunkBot(discord.Client):
    def __init__(self, name: str, *args, **kwargs):
        intents = discord.Intents.default()
        super().__init__(intents=intents, *args, **kwargs)
        self.bot_name = name
        self.status_index = 0
        self.messages = STATUS_MESSAGES.get(name, ["Online"])

    async def setup_hook(self):
        self.cycle_status.start()

    async def on_ready(self):
        print(f"[{self.bot_name}] Logged in as {self.user}")
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


async def run_bot(name: str, token: str):
    bot = VegapunkBot(name)
    try:
        await bot.start(token)
    except discord.LoginFailure:
        print(f"[{name}] FAILED - Invalid token!")
    except Exception as e:
        print(f"[{name}] Error: {e}")


async def main():
    print("Starting Vegapunk Satellite Bots...")
    print("=" * 50)

    tasks_list = []
    for name, env_var in BOT_CONFIG:
        token = os.getenv(env_var)
        if token:
            tasks_list.append(run_bot(name, token))
        else:
            print(f"[{name}] WARNING - No token found in {env_var}")

    if tasks_list:
        await asyncio.gather(*tasks_list)
    else:
        print("No valid tokens found. Check your .env file.")


if __name__ == "__main__":
    asyncio.run(main())
