import os
import discord
from dotenv import load_dotenv
import random
from penis import Penis
import time
import asyncio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PP_NAMES = ["determined dong", "dangerous dick", "colossal cock", "pleasant penis", "sizable schlong"]
pp_dict = {}


def load_pp_data():
    with open("pp.txt", "r") as pp_list_data:
        for line in pp_list_data:
            split_line = line.split(",")
            pp_dict[split_line[0]] = [int(split_line[1]), split_line[2]]
    pp_list_data.close()


def save_pp_data():
    with open("pp.txt", "w") as pp_list_data:
        for user_id in list(pp_dict.keys()):
            print("{},{},".format(user_id, pp_dict[user_id][0]), file=pp_list_data)


client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print('{} is connected to the following guild:\n{} (id: {})'
          .format(client.user, guild.name, guild.id))
    await client.change_presence(activity=discord.Game(name='with your mom'))
    load_pp_data()


@client.event
async def on_message(message):

    # Command: .nuke
    if '.nuke' == message.content.lower():

        def check(m):
            return 'yes' in m.content.lower() or 'no' in m.content.lower()

        number = random.randint(0, 9999)
        success_rate = random.randint(1, 10)
        await message.channel.send('Warning! Prototype Nuke {} has a {}% fail rate! Failure will be devastating!'
                                   .format(number, 100 - success_rate))
        await message.channel.send("Are you sure you want to launch Nuke {}?".format(number))

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
                if random.randint(1, 100) <= success_rate:
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
        pp = Penis(message.author)
        if pp.user_id in list(pp_dict.keys()):
            await message.channel.send("You already have a penis, idiot")
        else:
            pp_dict[pp.user_id] = [pp.length, "\n"]
            save_pp_data()
            pp_name = PP_NAMES[random.randint(0, len(PP_NAMES) - 1)]
            await message.channel.send("The story of your {} begins...".format(pp_name))

    # Command: .ppcheck
    if message.content.lower().startswith(".ppcheck"):
        output = message.content.split()
        if len(output) == 1:
            pp_username = message.author
        else:
            pp_username = message.mentions[0]
        pp_id = str(pp_username.id)
        if pp_id in list(pp_dict.keys()):
            length = int(pp_dict[pp_id][0])
            megalengths = length // 1000
            await message.channel.send(f"{str(pp_username)}'S PENIS:\n"
                                       f"8{'**{}**'.format('=' * megalengths) if megalengths > 0 else ''}"
                                       f"{'=' * (length - (megalengths * 1000))}>\n"
                                       f"({length} inches long)")
        else:
            await message.channel.send("They don't even have a penis LOL")

    # Command: .pproulette
    if message.content.lower().startswith(".pproulette"):

        def check(m):
            return 'yes' in m.content.lower() or 'no' in m.content.lower()

        roulette_user = message.author.id
        await message.channel.send("Are you sure you want to play russian roulette with your schlong?\n"
                                   "20% Chance to have your penis size get sent to 2 inches\n"
                                   "80% Chance to escape unscathed and have your penis size double\n")
        try:
            message = await client.wait_for('message', timeout=30, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("{}, maybe say 'yes' or 'no' DUDE...".format(message.author.mention))
        else:
            if 'yes' in message.content.lower() and message.author.id == roulette_user:
                number = random.randint(1, 5)
                if number == 1:
                    pp_dict[str(message.author.id)][0] = 2
                    await message.channel.send("YOUR PENIS DIDN'T MAKE IT LOL\nPENIS SENT BACK TO TWO INCHES")
                else:
                    pp_dict[str(message.author.id)][0] *= 2
                    await message.channel.send("You are safe... for now...\n(penis size doubled)")
                save_pp_data()

    # Reply: 'horny'
    if 'horny' in message.content.lower():
        await message.author.send('hey baby, wanna bang?')


client.run(TOKEN)
