import discord
import random
from discord import Member, Embed
from discord.ext import commands
from discord.utils import get
#from discord.member import Status

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command(aliases=['8ball', 'bj_from'])
async def _8ball(ctx, *, question):
    response = ['Johnny Depp',
                'Seth Rogen',
                'Danny DeVito',
                'Monica Lewinsky',
                'Jake Paul',
                'Belle Delphine',
                'James McGill',
                'CardiB',
                'Big Shaq',
                'Ryan Gosling']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')

@client.command()
async def nom(ctx):
    await ctx.send(f"{client.user.id} {client.guilds}")

@client.command()
async def jood(ctx, member):
    #guild = member.guilds
    #await ctx.send(f'{member.activity}')
    return member.activity

    #for guild in client.guilds:

    #member = query_members(uery=None, *, limit=5, user_ids=None, cache=True)
    # mem = None
    # # for usr in client.users:
    # #     if usr.name == client.users.name:
    # #         mem = usr
    # jood = 'Afloralfungi'

    # #if(mem.name == 'Afloralfungi'):


    # # if member.name == '>_<':
    # #     await ctx.send('This is jude')
    # # else:
    # #     await ctx.send("Not jude")
    # for member in client.guilds.fetch_members(limit=150):
    #     print(member.name)
    #     await ctx.send(f"{mem}")


client.run('NzgyNjQ1NzIzNDUxNzUyNDU4.X8PNoQ.orn-fMZ_-oiJGoegsVVMykHhrcE')