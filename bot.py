import discord
import os
import io
import traceback
import sys
import asyncio
import random
import aiohttp
import random
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('+'),description="A bot made my L3NNY\n\nHelp Commands",owner_id=411683912729755649)


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(game=discord.Game(name="+help"))


@bot.command()
async def test(ctx):
await ctx.send("Im online and working boi!")


if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
