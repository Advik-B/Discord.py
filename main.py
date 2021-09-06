import time
import discord
import os
import requests
import json
import discord.ext
import subprocess

f= open('./token' , 'r')
prefix = 'py!'
client = discord.Client()

@client.event 
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event #epic
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return
    
    if f'<@!{client.user.id}>' in msg or f'<@{client.user.id}>' in msg:
        await message.reply(f'<@!{message.author.id}> My prefix is `{prefix}`')

client.run(f.read())

f.close()