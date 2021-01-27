# discord.py
import os

import discord

with open('token.txt', 'r') as file:
    TOKEN = file.read().replace('\n', '')
with open('server.txt', 'r') as file:
    SERVERNAME = file.read().replace('')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
