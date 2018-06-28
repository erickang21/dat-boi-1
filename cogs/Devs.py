import discord
import sys
import os
import io
import asyncio
import aiohttp
import random
import subprocess
import json
import inspect
import traceback
from discord.ext import commands


    @commands.command()
    async def shutdown(self, ctx):
        """Shuts DOWN the bot. Cya!"""
        if not self.dev_check(ctx.author.id):
            return await ctx.send("HALT! This command is for the devs only. Sorry. :x:")
        msg = await ctx.send(f"Dying")
        await asyncio.sleep(1)
        await msg.edit(content="I died. ")
        await self.bot.logout()
        
  
def setup(bot): 
    bot.add_cog(Devs(bot)) 
