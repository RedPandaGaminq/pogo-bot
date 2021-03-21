import os
import discord
from dotenv import load_dotenv
import random
from penis import Penis

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PP_NAMES = ["determined dong", "dangerous dick", "colossal cock", "pleasant penis", "sizable schlong"]

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
        await message.channel.send('This command has been temporarily disabled.')

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
            await message.author.send("YOUR PP SMALL LOL")
        elif len(output) == 2:
            await message.channel.send("{}'S PENIS SIZE: 8{}>".format(message.content[7:], random.randint(0, 20) * "="))
        else:
            await message.channel.send("Error: Invalid Input")

    if '.ppbegin' == message.content.lower():
        pp = Penis(message.author)
        with open("pp.txt", "r+") as pp_data:
            for data in pp_data:
                if pp.user_id in data:
                    await message.channel.send("You already have a penis, idiot")
                    break
            else:
                print(f"{pp.user_id},{pp.length},", file=pp_data)
                pp_name = PP_NAMES[random.randint(0, len(PP_NAMES) - 1)]
                await message.channel.send("The story of your {} begins...".format(pp_name))

    if message.content.lower().startswith(".ppcheck"):
        output = message.content.split()
        if len(output) == 1:
            pp_username = message.author
        else:
            pp_username = message.mentions[0]
        pp_id = str(pp_username.id)
        with open("pp.txt", "r") as pp_data:
            for data in pp_data:
                if pp_id in data:
                    length = int(data.split(',')[1])
                    await message.channel.send(f"{str(pp_username)}'S PENIS:\n8{'=' * length}>\n({length} inches long)")
                    break
            else:
                await message.channel.send("They don't even have a penis LOL")

    # Replies
    if 'horny' in message.content.lower():
        await message.author.send('hey baby, wanna bang?')


client.run(TOKEN)
