import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from time import gmtime, strftime

loop = asyncio.new_event_loop()

asyncio.set_event_loop(asyncio.new_event_loop())

chat_filter = ["NIGGER", "BLACK", "MIGUEL", "ATUM"]
bypass_list = ['98809268219699200']
Nazi_Member = ['98468200508833792']

Client = discord.Client()
client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    channel = client.get_channel("464051159586439168")
    await client.send_message(channel, "```fix\nOlá Maltinha! O Alceo entrou no discord! kinda... :3 \n \nTry me! Type '.help' for more```")
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    if message.content == "Xico":
        await client.send_message(message.channel, "Comia-te todo malandro <3")
    if message.content == ".help":
        await client.send_message(message.channel, "```fix\nOlá o meu nome é Alceo e eu sirvo para avisar a malta dos horários do Trivia e para não dizerem palavras marotas com N1GGER N1GGER N1GGER. \nSe escrevers 'Xico' no chat podes ter uma surpresa! :3 \n \nCurrent Commands -> .trivia .help```")
    if message.content == ".trivia":
        await client.send_message(message.channel, "```glsl\n# TRIVIA TIMETABLE \n \nCash Show US - 01:00 - 02:30 \nCash Show AU - 12:00 \nCash Show UK - 20:30 \nCash Show DE - 11:00 - 20:00 \nCash Show FR - 11:30 - 19:30 \n\nHQ UK - 15:00 - 21:00 \nHQ US - 01:00 - 02:00```")
        await client.send_message(message.channel, "For more: https://triviatrckr.io/")
    if message.content == "!apa":
        await client.send_message(message.channel, "Nice to see you again Apa! :PAPAFACE:")
    if message.author.id == '98468200508833792':
        await client.send_message(message.channel, ":NAZIFLAGARONY:")
    if message.author.id == '128962977456979968':
        await client.send_message(message.channel, "Aiii Xicoo :$")    
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return

HQ_US = ["00:45","00:46","00:47","00:48","00:49","00:50","00:51","00:52","00:53","00:54"]
CS_UK = ["19:15","19:16","19:17","19:18","19:19","19:20","19:21","19:22","19:23","19:24"]
CS_AU = ["10:45","10:46","10:47","10:48","10:49","10:50","10:51","10:52","10:53","10:54"]
CS_US = ["01:15","01:16","01:17","01:18","01:19","01:20","01:21","01:22","01:23","01:24"]
CSHQ_US = ["23:45","23:46","23:47","23:48","23:49","23:50","23:51","23:52","23:53","23:54"]

Trivia_ID = '<@&463820461009272843>'

async def background_loop():
    await client.wait_until_ready()
    channel = client.get_channel("421099103418843136")
    while not client.is_closed:
        if strftime("%H:%M", gmtime()) in HQ_US:
            await client.send_message(channel, "%s Tá quase na hora do HQ US! It's time to get some MONEY!" % Trivia_ID)
        elif strftime("%H:%M", gmtime()) in CS_UK:
            await client.send_message(channel, "%s Tá quase na hora do Cash Show UK! It's time to get some MONEY!" % Trivia_ID)
        elif strftime("%H:%M", gmtime()) in CS_AU:
            await client.send_message(channel, "%s Tá quase na hora do Cash Show AU! It's time to get some MONEY!" % Trivia_ID)
        elif strftime("%H:%M", gmtime()) in CS_US:
            await client.send_message(channel, "%s Tá quase na hora do Cash Show US! It's time to get some MONEY! ly Xicão!" % Trivia_ID)
        elif strftime("%H:%M", gmtime()) in CSHQ_US:
            await client.send_message(channel, "%s Maltinha Cash Show US e HQ US tá ai a chegar! It's time to get some MONEY!" % Trivia_ID)
        await asyncio.sleep(600)

client.loop.create_task(background_loop())

client.run("NDY0MjI0MDk3NzYxNzU1MTU2.Dh7_hA.iEv8lE5DWxnpmxfzq89fdj0W4CU")




