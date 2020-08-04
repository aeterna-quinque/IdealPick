import json
import discord
import vk_api
import youtube_dl
from vk_api import audio

from discord.ext import commands
from random import randint as random_number

# Bot's Token
TOKEN = '***'

# Prefix for the commands
guild = commands.Bot(command_prefix='!')

# Connecting to JSON file
with open('heroes1.json') as f:
    heroes = json.load(f)


# Vk guild profile information
#path = 'C:\Users\user\Desktop\DiscordBot\music'
#login = '***'
#password = '***'
#vk_id = 'https://vk.com/***'

#players = {}



@guild.event
async def on_ready():
    print(f"{guild.user.name}: -I'm ready for work!")


@guild.command()
async def random(ctx: commands.Context, rand=None):
    types_of_rand = ["full", "pos"]

    if rand not in types_of_rand:
        helper_text = discord.Embed(title="Helper",
                                    description="Please clarify what kind of random you want to get",
                                    colour=discord.Colour.from_rgb(135, 206, 250))
        helper_text.add_field(name="\n\n\nPossible kinds of random:",
                              value="-full - completely random 5 heroes\n"
                                    "-pos - random hero for each position",
                              inline=False)
        helper_text.add_field(name="Example:\n",
                              value="!random pos",
                              inline=False)
        helper_text.add_field(name="Result",
                              value="1 - Faceless Void\n"
                                    "2 - Shadow Fiend\n"
                                    "3 - Omniknight\n"
                                    "4 - Winter Wyvern\n"
                                    "5 - Treant Protector",
                              inline=False)
        helper_text.set_thumbnail(url='https://i.pinimg.com/originals/48/ac/0d/48ac0d1f2b44afa0584c96edd0296829.png')
        await ctx.send(embed=helper_text)

    if rand == types_of_rand[0]:
        names_list = []
        for i in heroes["heroes"]:
            names_list.append(i["name"])
        result = []
        for i in range(5):
            n = random_number(0, len(names_list))
            while names_list[n] in result:
                n = random_number(0, len(names_list))
            result.append(names_list[n])
        result_box = discord.Embed(description=f"{result[0]}\n{result[1]}\n{result[2]}\n{result[3]}\n{result[4]}",
                                   colour=discord.Colour.from_rgb(135, 206, 250))
        await ctx.send(embed=result_box)

    if rand == types_of_rand[1]:
        pos = ['1', '2', '3', '4', '5']
        result = []
        for i in range(5):
            pos_list = []
            for j in heroes["heroes"]:
                if pos[i] in list(j["pos"]):
                    pos_list.append(j["name"])
            n = random_number(0, len(pos_list))
            result.append(pos_list[n])
        result_box = discord.Embed(description=f"1 - {result[0]}\n"
                                               f"2 - {result[1]}\n"
                                               f"3 - {result[2]}\n"
                                               f"4 - {result[3]}\n"
                                               f"5 - {result[4]}",
                                   colour=discord.Colour.from_rgb(135, 206, 250))
        await ctx.send(embed=result_box)

"""
@guild.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await guild.connect(channel)


@guild.command(pass_context=True)
async def vk_play(ctx, song):
    vk_session = vk_api.VkApi(login=login, password=password)
    vk_session.auth()
    vk = vk_session.get_api()
    vk_audio = audio.VkAudio(vk_session)
    vk_audio.search(song)
"""

guild.run(TOKEN)
