import discord
import os
from discord.ext import commands
from discord.ext.commands.core import command    
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix=(os.getenv("PREFIX")))

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)



bot.run(os.getenv('TOKEN'))
