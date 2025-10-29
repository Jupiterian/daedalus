# Daedalus Discord Bot

A Discord bot for fetching and displaying scoreboard information from a remote server. Now updated to support Discord.py v2+ with modern slash commands (application commands) and command trees!

## Features

- **Dual Command Support**: Both traditional prefix commands (`d command`) and modern slash commands (`/command`)
- **Scoreboard Tracking**: Fetch and display competition scores
- **Team Statistics**: Get detailed information about specific teams
- **Image-specific Rankings**: View scores for individual challenges/images
- **Export Functionality**: Download complete scoreboards as text files

## Setup

### Prerequisites

- Python 3.8 or higher
- Discord Bot Token (from [Discord Developer Portal](https://discord.com/developers/applications))
- A remote server URL to pull scores from

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd daedalus
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the bot:
   - Open `pub_bot.py`
   - Set your `remote` variable to your scoring server URL
   - Set your `bot_id` variable to your Discord bot token

### Bot Permissions

When inviting the bot to your server, make sure it has:
- `Send Messages` permission
- `Embed Links` permission
- `Attach Files` permission
- `Use Slash Commands` permission

### Running the Bot

```bash
python pub_bot.py
```

When the bot starts, it will automatically sync all slash commands to Discord. You should see:
```
Daedalus is ready!
Synced X command(s)
```

## Available Commands

### Slash Commands (Recommended)

- `/ping` - Test the bot's responsiveness
- `/server` - Display the server location
- `/daedalus` - Display ASCII art logo
- `/help` - Display all available commands
- `/top` - Fetch the top 10 scores
- `/scoreboard <number>` - Fetch the top N scores (default: 10)
- `/team <team_name>` - Fetch score details for a specific team
- `/export` - Export current scores to a text file
- `/image <image_name> <number>` - Fetch top N scores for a specific image
- `/rank <image_name> <team_id>` - Get the rank of a team for a specific image

### Prefix Commands (Legacy Support)

All commands also work with the `d ` prefix:
- `d ping`
- `d server`
- `d top`
- `d scoreboard <number>` or `d sc <number>`
- `d team <team_name>`
- And so on...

## Updates in v2.0

### Discord.py v2+ Support

- ✅ Updated to Discord.py v2.0+ with proper intents
- ✅ Added `app_commands` for slash command support
- ✅ Implemented command tree syncing
- ✅ Added `interaction.response.defer()` for long-running operations
- ✅ Converted all commands to both prefix and slash command formats
- ✅ Fixed deprecated API calls
- ✅ Improved error handling for message size limits

### Key Changes

1. **Intents**: Now properly configured with `message_content` intent
2. **Slash Commands**: All commands available as modern slash commands
3. **Command Tree**: Automatic syncing on bot startup
4. **Interactions**: Proper use of `defer()` and `followup` for async operations
5. **Backwards Compatibility**: Original prefix commands still work

## Migration Notes

If you're upgrading from an older version:

1. Update your Discord.py installation: `pip install -U discord.py>=2.0.0`
2. Ensure your bot has the "Message Content Intent" enabled in the Discord Developer Portal
3. Reinvite your bot with the updated permissions (including slash commands)
4. After starting the bot, slash commands may take up to an hour to appear globally, or instantly in guilds where the bot was restarted

## License

MIT License

Daedalus is a discord bot built to pull and view CSS scores from servers running [Sarpedon](https://github.com/sourque/sarpedon). 

## Installation/Setup
To get started make sure to have a server with python 3 installed and a discord bot setup in the applications folder. You will need to change the server IP and bot token in the pub_bot.py file.
```python
# SPECIFY REMOTE HERE AND YOUR BOT TOKEN HERE
remote = '<SERVER ADDRESS HERE>'
bot_id = '<YOUR TOKEN HERE>'
# YOUR PREFIX
client = commands.Bot(command_prefix = '<YOUR PREFIX HERE>')
```
