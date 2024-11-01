import wikiquotes
import discord
from discord.ext import commands, tasks

from risanje import risanje
import re


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='', intents=intents, help_command=None)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')
#    channel = client.get_channel(1300753195769004042) #  Gets channel from internal cache
#   while (1):
#        await channel.send(input("M: ")) 

@client.command()
async def status(ctx,arg):
    activity = discord.Game(name=arg)
    await client.change_presence(status=discord.Status.idle, activity=activity)

@client.command()
async def echo(ctx, arg):
    print(ctx)
    print(arg)
    if arg != "":
        print("arg je neki")
        await ctx.send(arg)

@client.command()
async def citat(ctx,arg):
    results = wikiquotes.search(arg, "english")
    await ctx.send(wikiquotes.random_quote(arg, "english") + '\n ~ '+ results[0])
    

@client.command()
async def pomagi(ctx):
    await ctx.send("ne lol") 
    await ctx.send("mogoce jutri") 

@client.command()
async def narisi(ctx, *, arg):
    dfsearch = re.search(r"interval_x=\((\d+),(\d+)\)", arg) 
    if xsearch:
        xmin = int(xsearch.group(1))
        xmax = int(xsearch.group(2))
    else:
        xmin = -10
        xmax = 10

    ysearch = re.search(r"interval_y=\((\d+),(\d+)\)", arg) 
    if zfsearch:
        ymin = int(ysearch.group(1))
        ymax = int(ysearch.group(2))
    else:
        ymin = -10
        ymax = 10

    funsearch = re.search(r"[^\s]+", arg)

    if funsearch:
        fun = funsearch.group(0)

    risanje(fun,xmin,xmax,ymin,ymax)
    await ctx.send(file=discord.File('fig.png'))

with open('token', 'r') as token: client.run(token.read())
