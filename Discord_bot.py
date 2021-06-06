import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
  print(" bot is ready")


@client.command()
async def hello(ctx):
  await ctx.send("YO MF")

@client.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called


@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx,member: discord.Member,*, reason=None):
    await member.kick(reason=reason)


client.run("TOCKEN")
