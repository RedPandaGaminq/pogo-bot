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
    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name} (id: {guild.id})')
    await client.change_presence(activity=discord.Game(name='with your mom'))


@client.event
async def on_message(message):

    # Commands
    if '.nuke' == message.content.lower():
        await message.channel.send('This command has been temperarily disabled.')
    if '.join' in message.content.lower():
        for i in range(10):
            await message.channel.send("{}, JUAN NOW DUDE".format(message.content[6:]))
    if '.penis' in message.content.lower():
        await message.channel.send("{}'S PENIS SIZE: 8{}>".format(message.content[7:], random.randint(0, 20) * "="))
    
    # Replies
    if 'horny' in message.content.lower():
        await message.channel.send('Check your DMs for a surprise ;)')
        await message.author.send('hey baby, wanna bang?')


client.run(TOKEN)
