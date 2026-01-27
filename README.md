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

## 📢 Broadcast Messages

Send a message to all 6 bots at once by DM-ing any of them!

### How to Use

1. **Configure Broadcast Channel**:
   - Set the `BROADCAST_CHANNEL_ID` in your `.env` file
   - This is the channel where all bots will send their broadcast messages
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
   - Type your message and send
   - All 6 bots will simultaneously send your message to the configured channel
   - You'll receive a confirmation reply: "Broadcast sent to all bots."
   - Bots will then return to their normal status cycling

### Example

```
You → DM Shaka: "Hello everyone!"
↓
All 6 bots → Send "Hello everyone!" to broadcast channel
↓
Shaka → DM reply: "Broadcast sent to all bots."
↓
All bots → Continue status cycling
```

### Important Notes

- The broadcast channel ID is not sensitive and can be shared
- Anyone who can DM the bots can trigger broadcasts (no authentication required)
- Messages are sent simultaneously by all bots
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
This project follows the guidelines in `AGENTS.md`:
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

- **NEVER** commit `.env` files to version control
- **NEVER** share bot tokens publicly
- Regenerate tokens immediately if exposed
- The `.env` file is already in `.gitignore`

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🌐 Inspiration

Inspired by Vegapunk's satellites from the anime/manga **One Piece** by Eiichiro Oda. Each bot embodies the unique personality and traits of these brilliant artificial intelligences.

---

Made with ❤️ by [FemReiyaDev](https://github.com/FemReiyaDev)
