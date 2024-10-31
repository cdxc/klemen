import discord
from discord.ext import commands, tasks

import matplotlib.pyplot as plt
import numpy as np

from risanje import narisi

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='', intents=intents)

@client.event
async def on_ready():
    print(f'logged in as {client.user}')
#    channel = client.get_channel(1300753195769004042) #  Gets channel from internal cache
#   while (1):
#        await channel.send(input("M: ")) 

@client.command()
async def echo(ctx, arg):
    print(ctx)
    print(arg)
    if arg != "":
        print("arg je neki")
        await ctx.send(arg)

@client.command()
async def graph(ctx, arg):
    narisi(arg, -10,10,-10,10)
    await ctx.send(file=discord.File('fig.png'))



with open('token', 'r') as tokenfile: token = tokenfile.read()
client.run(token)

