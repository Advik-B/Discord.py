import discord
import func
import os
import optparse
#defining things
prefix = 'py!'


parser = optparse.OptionParser()

parser.add_option('-t' , '--token' , dest='token', help='Token to run the bot [REQUIRED]')

token = str(parser.parse_args()[0]).split(':')[-1].replace("'" , '').replace('}' , '')

while True:
    print('[+] [Info]: Bot is starting!')
    client = discord.Client()
    @client.event 
    async def on_ready():
        print(f'[+] [Info]: Logged in as {client.user}')

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


    try:
        client.run(token)
    except AttributeError:
        print('[+] [Fatal]: Could not get token this program will be stopping')
        exit(-1)
    except discord.errors.LoginFailure:
        print('[+] [Fatal]: Bot Token is invalid')
        exit(-1)
    except NameError:
        print('[+] [Fatal]: The bot token is not provided. Please use --help option for more information')
        exit(-1)
    except RuntimeError:
        print('[+] [Fatal]: The bot token is not provided. Please use --help option for more information')
        exit(-1)