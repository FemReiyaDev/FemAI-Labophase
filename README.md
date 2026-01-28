# 🤖 Vegapunk Discord Bots

A collection of 6 Discord bots themed after Vegapunk's satellites from One Piece. Each bot cycles through themed status messages that reflect their unique personalities!

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![discord.py](https://img.shields.io/badge/discord.py-2.6.4-purple)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- **6 Unique Bots**: Shaka, Lilith, Edison, Pythagoras, Atlas, and York
- **Themed Status Messages**: Each bot has 5 personality-driven status messages
- **Auto-Cycling**: Statuses automatically change every 60 seconds
- **Async/Await**: Built with modern Python async patterns
- **Easy Configuration**: Simple `.env` file setup
- **Broadcast Messages**: Send messages to all bots simultaneously via DM

## 🔐 Authorisation

### Configuring Authorised Users

To control who can use the bots, set the `AUTHORISED_USER_IDS` environment variable in your `.env` file:

```env
AUTHORISED_USER_IDS=123456789012345678,987654321098765432
```

**Important notes:**
- Use comma-separated Discord user IDs (numeric IDs only)
- If `AUTHORISED_USER_IDS` is empty or not set, **any user can use the bots** (default for testing)
- Set this in production to restrict access to authorised users only

### Finding Discord User IDs

1. Open Discord
2. Enable **Developer Mode**:
   - Go to **Settings** → **Advanced** → Toggle on **Developer Mode**
3. Right-click on any user and select **Copy ID**
4. Paste the ID into your `.env` file

### How It Works

- When a user DMs a bot, their Discord user ID is checked against `AUTHORISED_USER_IDS`
- If the ID is in the list (or the list is empty), the user can proceed with commands
- If not authorised, the bot replies: "You are not authorised to use this bot."
- Unauthorised attempts are logged to the console with user details

## 📢 Broadcast Messages

Send messages through DM using a command-based system! Control whether a message goes to all 6 bots or just the one you're messaging.

### Available Commands

- `/all <message>` - Send message from all 6 bots to broadcast channel
- `/help` - Show this help message with all available commands
- `<any text>` - Send message only from the bot you're DM-ing

### How to Use

1. **Configure Broadcast Channel**:
   - Set the `BROADCAST_CHANNEL_ID` in your `.env` file
   - This is the channel where bots will send broadcast messages
   - Find the channel ID by right-clicking the channel in Discord → Copy ID

2. **Enable Required Intents**:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - For each bot:
     - Navigate to "Bot" settings
     - Enable **Message Content Intent** ✅
     - Enable **Messages Intent** ✅
     - Save changes

3. **Send a Broadcast**:
   - Open a DM with ANY of the 6 bots (Shaka, Lilith, Edison, Pythagoras, Atlas, or York)
   - Use `/all <message>` to broadcast to all 6 bots
   - Use regular text to send from just that bot
   - Use `/help` to see all available commands
   - Bots will then return to their normal status cycling

### Example

```
You → DM Shaka: "/all Hello everyone!"
↓
All 6 bots → Send "Hello everyone!" to broadcast channel
↓
Shaka → DM reply: "Broadcast sent to all bots."
↓
All bots → Continue status cycling
```

### Important Notes

- The broadcast channel ID is not sensitive and can be shared
- Users must be authorised (via `AUTHORISED_USER_IDS`) to trigger broadcasts
- If `AUTHORISED_USER_IDS` is empty, anyone who can DM the bots can use them (for testing)
- Use `/all` prefix to broadcast, regular text for single-bot messages
- Messages are sent simultaneously by all bots when using `/all`
- Bots ignore messages they send themselves
- Invalid channel IDs will be logged to console
- If BROADCAST_CHANNEL_ID is not set, broadcast functionality will be disabled

## 👾 The Bots

### Shaka (The Good - Wisdom/Ethics)
- "Taking meeting notes diligently."
- "Ethically vetting Edison's ideas."
- "York, honesty is a virtue..."
- "Violence was not the answer, Atlas."
- "Teamwork is the ethical choice."

### Lilith (The Evil - Combat/Profit)
- "Doodling profit charts in the meeting."
- "Costing Edison's 'profitable' ones."
- "That prototype cost 80 million berries."
- "Filing an insurance claim..."
- "Fine. I'll 'collaborate.' For profit."

### Edison (The Genius - Creativity/Ideas)
- "IDEA! Wrong meeting. Sorry."
- "THEY'RE ALL GOOD IDEAS, TRUST ME!"
- "I can rebuild it! NEW IDEA!"
- "Ooh! I can make it BETTER now!"
- "GROUP BRAINSTORM! EVERYONE TALK!"

### Pythagoras (The Wise - Logic/Analysis)
- "Calculating meeting efficiency: 12%."
- "299 rejected. 1 pending review."
- "Crumb analysis points to York."
- "Structural failure was 87% predictable."
- "Dividing tasks by optimal efficiency."

### Atlas (The Violent - Strength/Protection)
- "Guarding the snack table."
- "Edison's last idea exploded. Cleaning up."
- "Interrogating York (gently)."
- "It was looking at me funny."
- "I'll carry the heavy stuff!"

### York (The Greed - Appetite/Laziness)
- "Brought snacks. Ate the snacks."
- "Ignoring Edison. Napping."
- "It looked like a donut, okay?!"
- "Didn't see anything. Was eating."
- "Supervising. From the couch. With snacks."

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- Discord Developer Account

### Step 1: Clone the Repository
```bash
git clone https://github.com/FemReiyaDev/FemAI-Labophase.git
cd FemAI-Labophase
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Discord Bots

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create 6 new applications (one for each bot)
3. For each bot:
   - Go to the "Bot" section
   - Enable **Presence Intent** (required for custom status)
   - Enable **Message Content Intent** (required for broadcast messages)
   - Enable **Messages Intent** (required for broadcast messages)
   - Generate a bot token
   - Invite the bot to your server

### Step 5: Set Up Environment Variables

Create a `.env` file in the project root:
```env
SHAKA_TOKEN=your_shaka_token_here
LILITH_TOKEN=your_lilith_token_here
EDISON_TOKEN=your_edison_token_here
PYTHAGORAS_TOKEN=your_pythagoras_token_here
ATLAS_TOKEN=your_atlas_token_here
YORK_TOKEN=your_york_token_here
BROADCAST_CHANNEL_ID=your_channel_id_here
AUTHORISED_USER_IDS=123456789012345678,987654321098765432
```

## 🎮 Usage

### Quick Start (Windows)
Double-click `run.bat` or run from command line:
```bash
run.bat
```

### Manual Start
```bash
# Activate virtual environment
venv\Scripts\activate

# Run the bots
python vegapunk_bots.py
```

### Stop the Bots
Press `Ctrl+C` in the terminal to stop all bots gracefully.

## ⚙️ Configuration

### Customize Status Cycle Interval

Edit `vegapunk_bots.py`:
```python
STATUS_CYCLE_INTERVAL = 60  # Change to desired seconds
```

### Add/Modify Status Messages

Edit `status_messages.py` to customize or add new messages:
```python
STATUS_MESSAGES = {
    "Shaka": [
        "Your custom message here.",
        # Add more...
    ],
    # ... other bots
}
```

### Configure Broadcast Channel

Set the broadcast channel in your `.env` file:
```env
BROADCAST_CHANNEL_ID=123456789012345678
```

To find your channel ID:
1. Open Discord
2. Right-click on the desired channel
3. Select "Copy ID"
4. Paste the ID into your `.env` file

If `BROADCAST_CHANNEL_ID` is not set, the broadcast feature will be disabled.

## 🛠️ Development

### Code Style
This project follows the guidelines:
- Black for code formatting
- flake8 for linting
- mypy for type checking

### Run Linting
```bash
black . && flake8 . && mypy .
```

## 📁 Project Structure
```
FemAI-Labophase/
├── vegapunk_bots.py      # Main bot runner
├── status_messages.py    # Status message definitions
├── requirements.txt      # Python dependencies
├── run.bat              # Windows batch script
├── AGENTS.md            # Agent guidelines
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Invalid token" error | Regenerate token in Discord Developer Portal |
| Bots show offline | Enable **Presence Intent** in bot settings |
| Status not updating | Ensure discord.py 2.0+ is installed |
| Import errors | Make sure virtual environment is activated |

## 🔐 Security

### Authorisation

The bots include authorisation to control who can trigger broadcasts:

- **AUTHORISED_USER_IDS**: Comma-separated list of authorised Discord user IDs
- Users must be in this list to use bot commands via DM
- If empty, any user can use the bots (useful for testing, but set in production!)
- Unauthorised users receive a clear error message and are logged
- Authorisation checks are performed on every command attempt

### Token Management

- **NEVER** commit `.env` files to version control
- **NEVER** share bot tokens publicly
- Regenerate tokens immediately if exposed
- The `.env` file is already in `.gitignore`

### Rate Limiting

The bots include rate limiting to prevent spam and abuse:

- **MAX_MESSAGES_PER_MINUTE**: 25 messages per user per minute
- Each user's message timestamps are tracked in a sliding window
- Messages older than 60 seconds are automatically removed from tracking
- Thread-safe implementation using `asyncio.Lock` for concurrent bot access
- Users exceeding the rate limit receive a clear error message

### Input Validation

The bots include comprehensive input validation to prevent abuse:

#### Message Length Limits

- **MAX_MESSAGE_LENGTH**: 2000 characters (Discord's API limit)
- Messages exceeding this limit are rejected before sending
- Empty messages are automatically filtered out

#### Mention Protection

- **ALLOWED_MENTIONS**: All Discord mentions are blocked by default
- `@everyone` and `@here` mentions are automatically disabled
- User and role mentions are prevented from expanding
- This prevents spam and abuse through broadcast messages

#### Content Validation

- The `validate_broadcast_content()` function checks all broadcast messages
- Validates message length before sending
- Filters empty or whitespace-only messages
- Returns descriptive error messages for invalid content

### How It Works

```python
# Example of security in action
async def send_broadcast(self, content: str) -> bool:
    valid, result = validate_broadcast_content(content)
    if not valid:
        return False
    
    # allowed_mentions prevents @everyone abuse
    await channel.send(content, allowed_mentions=ALLOWED_MENTIONS)
```

### Best Practices

- Keep bot tokens secure and rotate them periodically
- Monitor broadcast channel for unusual activity
- Review audit logs (if enabled) for security incidents
- Be cautious who has access to DM your bots

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🌐 Inspiration

Inspired by Vegapunk's satellites from the anime/manga **One Piece** by Eiichiro Oda. Each bot embodies the unique personality and traits of these brilliant artificial intelligences.

---

Made with ❤️ by [FemReiyaDev](https://github.com/FemReiyaDev)
