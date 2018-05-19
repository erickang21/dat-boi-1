import discord
import sys
import os
import io
import asyncio
import aiohttp
import random
import subprocess
import json


class Owner:
    def __init__(self, bot):
       self.bot = bot
       self.sessions = set()


    def dev_check(self, id):
        with open('data/devs.json') as f:
            devs = json.load(f)
            if id in devs:
                return True
        return False
        
        
    @commands.command()
    async def shutdown(self, ctx):
        if not self.dev_check(ctx.author.id):
            return await ctx.send("You cannot use this command because you are not a developer.")
        msg = await ctx.send(f"Going to bed:spinner:")
        await asyncio.sleep(1)
        await msg.edit(content="Cya! Sleeping now...")
        await self.bot.logout()
        
        
        
def setup(bot): 
    bot.add_cog(Owner(bot)) 
