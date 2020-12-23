import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.command()
async def mine(ctx):
    await ctx.send('YA, YOURS!')

@bot.command()
async def alec(ctx):
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
    await ctx.send('WOW...literally..WOW')

@bot.command()
async def golf(ctx):
    await ctx.send('with your ass!')




bot.run('NzkxMTc0NjMyMDk0ODI2NTE2.X-LUyw.A5GYsnifcGjQJl3NbPnXaesPFvA')

