# NPL Coder Leaderboard Bot

A Discord bot that manages a leaderboard system integrated with Google Sheets, allowing tracking of user scores across different provinces, districts, and schools.

## Features

- View top performers by score
- View top performing provinces, districts, or schools
- Admin-only commands for managing users and scores
- Google Sheets integration for persistent data storage
- Rich Discord embeds for beautiful data presentation

## Commands

### Public Commands
- `npl help` - Shows all available commands
- `npl top <k>` - Shows the top k users based on scores
- `npl top_place <place> <k>` - Shows top k places based on average scores
  - `place` can be: province, district, or school
  - Example: `npl top_place province 3`

### Admin-Only Commands
These commands require Discord administrator permissions:
- `npl add_user <name> <username> <province> <district> <school>` - Adds a new user to the leaderboard
- `npl increase_score <username> <points>` - Increases a user's score

## Setup

1. Create a Discord Application and Bot
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Add a bot to your application
   - Copy the bot token

2. Set up Google Sheets API
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project
   - Enable Google Sheets API
   - Create service account credentials
   - Download the credentials as `credentials.json`
   - Create a Google Sheet and share it with the service account email

3. Environment Setup
   - Create a `.env` file in the project root with:
     ```
     DISCORD_TOKEN=your_discord_bot_token
     SHEET_ID=your_google_sheet_id
     ```

4. Install Dependencies
   ```bash
   pip install discord.py python-dotenv google-oauth2-credentials gspread pandas
   ```

5. Google Sheet Structure
   The sheet should have the following columns:
   - Name
   - Discord Username
   - Province
   - District
   - School
   - Score

## Running the Bot

1. Make sure `credentials.json` is in the project root
2. Run the bot:
   ```bash
   python bot/main.py
   ```

## Permissions

- Regular users can view the leaderboard and statistics
- Only users with Discord administrator permissions can:
  - Add new users
  - Modify scores

## Contributing

Feel free to submit issues and enhancement requests!
