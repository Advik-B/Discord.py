import discord
import func
import os

#defining things
prefix = 'py!'
client = discord.Client()

@client.event 
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event #epic
async def on_message(message):
    msg = message.content
    _msg = str(message.content)
    if message.author == client.user:
        return
    
    if  _msg.startswith(f'<@!{client.user.id}>') or _msg.startswith(f'<@{client.user.id}>'):
        await message.reply(f'<@!{message.author.id}> My prefix is `{prefix}`')

    if  _msg.startswith(prefix):
        code = _msg.split('```py')[-1].replace('```' , '').replace(prefix , '')
        try:
            out = func.evaluate(code)
        except func.EvalError:
            out = 'Umm..... `input()` or something similar is not supported :broken_heart:'
        await message.reply(out)


client.run(os.getenv('TOKEN'))
