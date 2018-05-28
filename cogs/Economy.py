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



class Economy:
    def __init__(self, bot):
        self.bot = bot
  
    
    @commands.command()
    async def daily(self, ctx):
        await ctx.send("You got $400!")
        
        
        
def setup(bot):
    bot.add_cog(Economy(bot))
