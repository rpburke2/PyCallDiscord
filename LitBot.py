import random
from string import Template
from insults import wowDoes
import discord
import inspect
from discord.ext import commands
from Config import discord_token

bot = commands.Bot(command_prefix='.')

##COMMAND LIST##

@bot.command()
async def delete(ctx, name):
    try:
        exec(f"del {name}")
        await ctx.send(f"Command '.{name}' deleted successfully!")
    except:
        await ctx.send(f"Command '.{name}' could not be deleted. Suck an egg, Travis!")

@bot.command()
async def create(ctx, name, message):
    cmd_template = Template("@bot.command()\nasync def $name(ctx): await ctx.send('$msg')")
    try:
        exec(cmd_template.substitute(name=name, msg=message))
        await ctx.send(f"Command '.{name}' created successfully!")
    except:
        await ctx.send(f"Command '.{name}' could not be created. Suck an egg, Travis!")

@bot.command()
async def mine(ctx):
    await ctx.send('YA, YOURS!')

@bot.command()
async def alec(ctx, ):
    await ctx.send('ya know what man... he really does!')

@bot.command()
async def trav(ctx):
    await ctx.send('trav?... havent heard that name in years!')

@bot.command()
async def ian(ctx):
    await ctx.send('vasectomy says what?')

@bot.command()
async def rob(ctx):
    await ctx.send('he thinks he is but he really isnt!')

@bot.command()
async def conrad(ctx):
    await ctx.send('WOW...literally...WOW')

@bot.command()
async def gert(ctx):
    await ctx.send('whats the temp on that laptop bud?!')

@bot.command()
async def golf(ctx):
    await ctx.send('with your ass!')

@bot.command()
async def dead(ctx):
    await ctx.send('that game literally!')

@bot.command()
async def huge(ctx):
    await ctx.send('massive, really.')

@bot.command()
async def wow(ctx):
    await ctx.send('WOW DUDE DOES YOURS!')

@bot.command()
async def nah(ctx):
    await ctx.send('No dude..YOURS!')

@bot.command()
async def iz(ctx):
    await ctx.send('IZZZZZZZZZZZZZZZZZZZZZZZ!')

@bot.command()
async def lcj(ctx):
    await ctx.send('3-10')

@bot.command()
async def does(ctx):
    await ctx.send(random.choice(wowDoes))


bot.run(discord_token)

