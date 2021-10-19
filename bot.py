import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.content == 'Ping':
        response = 'Pong'
        await message.channel.send(response)

client.run('ODk5ODIxMTIyMjIzMjM1MDcy.YW4VuQ.Xjmkq4LqomHj6VsGahiMsFoA1OY')
