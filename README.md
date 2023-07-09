# Saeroyi Discord Bot
This bot can be invited to Discord servers where it will read messages and generate random pictures of Korean drama actors. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Configuration](#configuration)
- [Contributing](#contributing)


## Installation
1. Clone the repository: `git clone https://github.com/your-username/your-repository-name.git`
2. Install the dependencies: `npm install`

## Usage

1. Rename `config.example.json` to `config.json` and update the required configuration values.
2. Start the bot: `npm start`

## Commands

- **=rizz**: Generates a random pick-up line.
- **=oppars**: Generates a photo of a random male actor.
- **=noonas**: Generates a photo of a random female actor.

## Configuration

In order to use the bot, you need to set up a `config.json` file with the following configuration:

{
  "token": "YOUR_DISCORD_BOT_TOKEN",
  "prefix": "!"
}
token: Your Discord bot token. You can obtain this by creating a bot application on the Discord Developer Portal.
prefix: The prefix character(s) used to invoke commands for your bot.
Make sure to update the configuration values accordingly.

Contributing
If you'd like to contribute to this project, you can follow these steps:

Fork the repository.
Create a new branch for your feature: git checkout -b feature/your-feature-name.
Commit your changes: git commit -am 'Add your feature'.
Push to the branch: git push origin feature/your-feature-name.
Submit a pull request.
Please ensure that your code follows the existing coding style and include relevant tests if applicable.




