import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print('{} is connected to the following guild:\n'
          '{} (id: {})'.format(client.user, guild.name, guild.id))
    await client.change_presence(activity=discord.Game(name='with your mom'))


@client.event
async def on_message(message):

    # Commands
    if '.nuke' == message.content.lower():
        await message.channel.send('This command has been temporarily disabled.')
    if message.content.lower().startswith(".join"):
        output = message.content.split()
        if len(output) == 2:
            for i in range(10):
                await message.channel.send("{}, JUAN NOW DUDE".format(output[1]))
        else:
            await message.channel.send("Error: Invalid Input")
    if '.penis' in message.content.lower():
        await message.channel.send("{}'S PENIS SIZE: 8{}>".format(message.content[7:], random.randint(0, 20) * "="))

    # Replies
    if 'horny' in message.content.lower():
        await message.author.send('hey baby, wanna bang?')


client.run(TOKEN)
