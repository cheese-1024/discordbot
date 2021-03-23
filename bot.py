import discord
import os
import sys
from discord.ext import commands
from discord.ext.commands.core import command    
from discord.ext.commands import *
from dotenv import load_dotenv
import bcolors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
load_dotenv()
trusted = ["674332158973706261"]


bot = commands.Bot(command_prefix=(os.getenv("PREFIX")))

@bot.event
async def on_ready():
    print(f'''{bcolors.BOLD + bcolors.OKBLUE}Connected successfully!
Logged in as {bcolors.OKCYAN}{bot.user.name}{bcolors.OKBLUE}, with the ID {bcolors.OKCYAN}{bot.user.id}{bcolors.ENDC}''')
    status = "you grate some cheese 😳"
    await bot.change_presence(activity=discord.Activity(name=status, type=discord.ActivityType.watching))
    print(f'{bcolors.BOLD + bcolors.OKBLUE}Status set to "{bcolors.OKCYAN}watching {status}{bcolors.OKBLUE}"{bcolors.ENDC}')
    print(f"{bcolors.BOLD + bcolors.OKBLUE}------------------------------------------------------{bcolors.ENDC}")

@bot.command(help="returns the arguments")
async def echo(ctx, *, arg):
    id =  ctx.author.id
    if id == 674332158973706261:
        await ctx.send(arg)
    else:
        await ctx.message.add_reaction("🔐")

@bot.command(help="Gets the ping of the bot and returns it in an embed")
async def ping(ctx):
    await ctx.message.add_reaction("🏓")
    botPing = round(bot.latency * 1000)
    if botPing < 130:
        color = 0x33D23F
    elif botPing > 130 and botPing < 180:
        color = 0xff8c00
    else: 
        color = 0xff2200
    embed = discord.Embed(title="Pong! :ping_pong:", description=f"The ping is **{botPing}ms!**")
    await ctx.reply(embed=embed)





bot.run(os.getenv('TKN'))
