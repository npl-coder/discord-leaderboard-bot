import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Embed
from bot import responses

# Load token from .env
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

def has_admin_permission(message: Message) -> bool:
    if not message.guild:  # If message is in DM
        return False
    return message.author.guild_permissions.administrator

# Message Functionality


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty because intents were not enabled.")
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response = responses.get_responses(user_message, has_admin_permission(message))
        if isinstance(response, Embed):
            await message.author.send(embed=response) if is_private else await message.channel.send(embed=response)
        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


async def help_command(message: Message) -> None:
    """Sends a help response to the user."""
    try:
        response = responses.get_help()  # This is likely returning an Embed

        # If response is an Embed, send it correctly
        if isinstance(response, Embed):
            await message.channel.send(embed=response)
        else:
            await message.channel.send(response)  # If it’s a string, send normally

    except Exception as e:
        print(f"Error sending help message: {e}")

# Handling the startup

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# Handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}] {username}: {user_message}")

    # Check if message starts with "npl"
    if user_message.lower().startswith("npl"):
        if 'help' in user_message.lower():
            print('help triggered!')
            await help_command(message)
        else:
            await send_message(message, user_message)


# Main entry point


def main() -> None:
    client.run(token=token)


if __name__ == "__main__":
    main()
