import os
import discord
from dotenv import load_dotenv
import random
import time
import asyncio

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

    # Command: .nuke
    if '.nuke' == message.content.lower():
        number = random.randint(0, 9999)
        success_rate = random.randint(1, 10)
        await message.channel.send('Warning! Prototype Nuke {} has a {}% fail rate! Failure will be devastating!'
                                   .format(number, 100 - success_rate))
        await message.channel.send("Are you sure you want to launch Nuke {}?".format(number))

        def check(m):
            return 'yes' in m.content.lower() or 'no' in m.content.lower()

        try:
            message = await client.wait_for('message', timeout=30, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("{}, maybe say 'yes' or 'no' DUDE...".format(message.author.mention))
        else:
            if 'yes' in message.content.lower():
                for i in range(10):
                    await message.channel.send("WARNING! LAUNCHING NUKE {}!".format(number))
                for i in range(10, 0, -1):
                    await message.channel.send(i)
                    time.sleep(1)
                if random.randint(1, 100) in range(1, success_rate + 1):
                    await message.channel.send("NUKE LAUNCH SUCCESSFUL!")
                    for i in range(20):
                        await message.channel.send("@everyone")
                else:
                    await message.channel.send("Launch failed...")
                    for i in range(20):
                        await message.author.send("YOU HAVE BEEN NUKED!")
            else:
                await message.channel.send("Lame... goodbye")

    # Command: .join
    if message.content.lower().startswith(".join"):
        output = message.content.split()
        if "@everyone" in output:
            await message.author.send("Look buddy, you better CUT THAT OUT.")
        elif len(output) == 2:
            for i in range(10):
                await message.channel.send("{}, JUAN NOW DUDE".format(output[1]))
        else:
            await message.channel.send("Error: Invalid Input")

    # Command: .penis
    if message.content.lower().startswith(".penis"):
        output = message.content.split()
        if "@everyone" in output:
            await message.author.send("YOUR PP SMALL OMEGALUL")
        elif len(output) == 2:
            await message.channel.send("{}'S PENIS SIZE: 8{}>".format(message.content[7:], random.randint(0, 20) * "="))
        else:
            await message.channel.send("Error: Invalid Input")

    # Command: .ppbegin
    if '.ppbegin' == message.content.lower():
        pp_names = ["determined dong", "dangerous dick", "colossal cock", "pleasant penis"]
        pp_name = pp_names[random.randint(0, 3)]
        await message.channel.send("The story of your {} begins...".format(pp_name))

    # Reply: 'horny'
    if 'horny' in message.content.lower():
        await message.author.send('hey baby, wanna bang?')


client.run(TOKEN)
