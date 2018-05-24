import discord
import sys
import os
import io
import datetime
import asyncio
import aiohttp
import random
import json



class Fortnite:
    '''
    Get information about a Fortnite user
    '''

    def __init__(self, bot):
        self.bot = bot
        self.client = pynite.Client(os.getenv('FNTOKEN'), timeout=5)
        
        
        
@commands.command()
async def fortnite(self, ctx):
await ctx.send("https://www.epicgames.com/fortnite/en-US/home")
    
    
 def setup(bot):
    bot.add_cog(Fortnite(bot))
