## Info
With this blank-file you can easily create Discord Bot for your server!
This blank-file proudly written on python. So if you can code on python, you can add new features for you bot!
## How to compile?
### Pre-requests
### Getting the bot token
1. Open a [Discord Developer Page](https://discord.com/developers/applications) and create application.
2. Create name for bot.
3. Go to "Bot" page and press reset token.
4. Copy the token and paste it to tokens library (tokens.py).
5. Compile bot.
### Getting an OpenAI for ChatGPT feature (optional)
1. Open [OpenAI Developer Board](https://platform.openai.com/account/api-keys).
2. Generate an API key.
3. Paste it to tokens library (tokens.py).
4. Compile bot with ChatGPT feature.

## ‼ If you trying to compile this bot on Windows, use MSYS2. ‼
To build this bot, type:
> make

If you want use a ChatGPT feature, type:
> make chatgpt

If you having issues with bot(like a endless reboots), try to use Bot Runner for Windows.

To compile it, type:

> make bot_launcher
## How to add bot to server?
1. Open a [Discord Developer Page](https://discord.com/developers/applications).
2. Go to OAuth2 -> URL Generator
3. In scopes press **bot** and **application.command**
4. In bot permissions press **Administrator**
5. Copy link and paste it to your browser.
6. Add bot to your server.
## Usage
There's a small list of all availible commands for base bot.

You can edit all of this commands by opening .py file of the command.
| Command | Description |
|-------------|-------------|
| /commands (commandslist.py) | List all availble commands. |
| /stats (botstats.py) | Bot statistics. |
| /randompic (picrandomizer.py) | Send random pic. |
| /rps (rock-paper-scissors-game.py) | Rock-paper-scissors minigame. |
| /wordoftheday (wordoftheday.py) | Word of the day. |
| /hug {usertag} (actionsuser.py) | Hug user. |
| /kiss {usertag} (actionsuser.py) | Kiss user. |
| /embed (emptyembedmessage.py) | Send empty embed message (customizable feature). |
## Adding features
If you want to add your features to bot, use *emptyembedmessage.py* and *addictionalfunctions.py* until you compile the bot.
