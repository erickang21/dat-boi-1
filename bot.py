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
        await bot.change_presence(activity=discord.Game(name=f"V 0.0.1"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name=f"with {len(bot.guilds)} servers boi!"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(name=f"on discord."))
        await asyncio.sleep(10)


@bot.event
async def on_guild_join(guild):
    lol = bot.get_channel(438526627824271362)
    em = discord.Embed(color=discord.Color(value=0x11f95e))
    em.title = "I have joined new server!"
    em.description = f"Server: {guild}"
    await lol.send(embed=em)
    await ctx.send(f"Hello my peeps. Im a discord created my L3NNY#4519 try me out by doing ``+help``")

      
@bot.event
async def on_guild_remove(guild):
    lol = bot.get_channel(438526627824271362)
    em = discord.Embed(color=discord.Color(value=0xf44242))
    em.title = "I have left a server."
    em.description = f"Server: {guild}"
    await lol.send(embed=em)   
        
        
@bot.command()
async def ping(ctx):
    """Get the bot's Websocket latency."""
    color = discord.Color(value=0x11f95e)
    em = discord.Embed(color=color, title='Pong! Websocket Latency:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)

    
@bot.command()
async def invite(ctx):
    """Invite me to dat club of yours"""
await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=438487038032085025&permissions=8&scope=bot")    
    
if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
