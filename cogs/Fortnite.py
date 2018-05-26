import discord
import sys
import os
import io
import datetime
import asyncio
import aiohttp
import random
import json
from discord.ext import commands



class Fortnite:
    def __init__(self, bot):
        self.bot = bot
  
    
    @commands.commands()
    async def fortnite(self, ctx):
        await ctx.send("https://www.epicgames.com/fortnite/en-US/home")
    
    
def setup(bot):
    bot.add_cog(Fortnite(bot))
