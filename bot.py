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


def dev_check(id):
    with open('data/devs.json') as f:
        devs = json.load(f)
    if id in devs:
        return True
    return False
        
        
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
    """lemme join dat c00l club""" 
    await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=438487038032085025&permissions=8&scope=bot")
  
   
    @bot.command(hidden=True, name='eval')
async def _eval(ctx, *, body: str):

    if not dev_check(ctx.author.id):
        return await ctx.send("Hey, I see you. Only developers can use eval. :laughing:")

    env = {
        'bot': bot,
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        try:
            await ctx.message.add_reaction('\u2705')
        except:
            pass

        if ret is None:
            if value:
                await ctx.send(f'```py\n{value}\n```')
        else:
            await ctx.send(f'```py\n{value}{ret}\n```')     
    
    
if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
