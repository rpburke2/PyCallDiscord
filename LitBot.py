import discord
import inspect
from discord.ext import commands
from Config import discord_token

bot = commands.Bot(command_prefix='!')

##COMMAND LIST##

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
async def litcmd(ctx,):
    msg = "|   !alec   |   !ian   |   !rob   |   !trav   |   !gert   |   !conrad   |   !mine   |   !dead   |   !golf   |"
    await ctx.send(msg)


bot.run(discord_token)

