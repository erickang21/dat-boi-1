import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import random
import textwrap
import inspect
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('+'),description="A bot made my L3NNY\n\nHelp Commands",owner_id=411683912729755649)


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    while True:
        await bot.change_presence(activity=discord.Game(name=f"+help"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name=f"on discord."))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name=f"with {len(bot.guilds)} servers boi!"))
        await asyncio.sleep(10)


@bot.command()
async def ping(ctx):
    """Get the bot's Websocket latency."""
    color = discord.Color(value=0x11f95e)
    em = discord.Embed(color=color, title='Pong! Websocket Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)

if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
