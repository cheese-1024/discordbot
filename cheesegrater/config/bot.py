# .py
import os
import discord
import random
cmdpre = "//"
with open('token.txt', 'r') as file:
    TOKEN = file.read().replace('\n', '')
with open('server.txt', 'r') as file:
    GUILD = file.read().replace('\n', '')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}( id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    pog_quotes = [
        'Pog',
        'POGGERS',
        'ME WHEN POG :O',
        'POGCHAMP',
    ]

    if message.content == '//test':
        response = random.choice(pog_quotes)
        await message.channel.send(response)
        
client.run(TOKEN)


