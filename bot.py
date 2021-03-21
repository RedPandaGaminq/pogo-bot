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
    print('{} is connected to the following guild:\n{} (id: {})'
          .format(client.user, guild.name, guild.id))
    await client.change_presence(activity=discord.Game(name='with your mom'))


@client.event
async def on_message(message):

    # Commands
    if '.nuke' == message.content.lower():
        number = random.randint(0, 9999)
        await message.channel.send('Warning! Prototype Nuke {} has a 99% fail rate! Failure will be devastating!'
                                   .format(number))
        await message.channel.send("Are you sure you want to launch Nuke {}?".format(number))

        def check(m):
            return m.content.lower() == 'yes' or m.content.lower == 'no'

        message = await client.wait_for('message', check=check)
        if message.content.lower() == 'yes':
            for i in range(10):
                await message.channel.send("WARNING! LAUNCHING NUKE {}!".format(number))
            for i in range(10, 0, -1):
                await message.channel.send(i)
            if random.randint(1, 100) == 1:
                await message.channel.send("NUKE LAUNCH SUCCESSFUL!")
                for i in range(20):
                    await message.channel.send("@everyone")
            else:
                await message.channel.send("Launch failed... you will now be punished for wasting so much money...")
                for i in range(20):
                    await message.author.send("YOU HAVE BEEN NUKED!")
        else:
            await message.channel.send("Lame... goodbye.")

    if message.content.lower().startswith(".join"):
        output = message.content.split()
        if "@everyone" in output:
            await message.author.send("Look buddy, you better CUT THAT OUT.")
        elif len(output) == 2:
            for i in range(10):
                await message.channel.send("{}, JUAN NOW DUDE".format(output[1]))
        else:
            await message.channel.send("Error: Invalid Input")

    if message.content.lower().startswith(".penis"):
        output = message.content.split()
        if "@everyone" in output:
            await message.author.send("YOUR PP SMALL OMEGALUL")
        elif len(output) == 2:
            await message.channel.send("{}'S PENIS SIZE: 8{}>".format(message.content[7:], random.randint(0, 20) * "="))
        else:
            await message.channel.send("Error: Invalid Input")

    if '.ppbegin' == message.content.lower():
        pp_names = ["determined dong", "dangerous dick", "colossal cock", "pleasant penis"]
        pp_name = pp_names[random.randint(0, 3)]
        await message.channel.send("The story of your {} begins...".format(pp_name))

    # Replies
    if 'horny' in message.content.lower():
        await message.author.send('hey baby, wanna bang?')


client.run(TOKEN)
