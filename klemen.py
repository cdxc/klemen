# This example requires the 'message_content' intent.

import discord
from discord.ext import commands, tasks



import matplotlib.pyplot as plt
import numpy as np

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
    x = np.linspace(-5,5,100)
    y = eval(arg)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')

    ax.spines['right'].set_color('blue')
    ax.spines['left'].set_color('blue')
    ax.spines['bottom'].set_color('green')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x,y, 'r-o')
    plt.savefig("fig", bbox_inches='tight')
    #plt.show()
    await ctx.send(file=discord.File('fig.png'))



with open('token', 'r') as tokenfile: token = tokenfile.read()
client.run(token)

