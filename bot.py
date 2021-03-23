import discord
import os
import sys
from discord.ext import commands
from discord.ext.commands.core import command    
from dotenv import load_dotenv
load_dotenv()
trusted = ["674332158973706261"]


bot = commands.Bot(command_prefix=(os.getenv("PREFIX")))

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
