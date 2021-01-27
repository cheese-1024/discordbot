# discord.py
import os
import discord

with open('token.txt', 'r') as file:
    TOKEN = file.read().replace('\n', '')

with open('server.txt', 'r') as file:
    SERVERNAME = file.read().replace('\n', '')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVERNAME:
            break
    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}( id: {guild.id})'
    )

client.run(TOKEN)
