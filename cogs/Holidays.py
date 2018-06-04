mport discord
import sys
import os
import io
import datetime
import asyncio
import aiohttp
import random
import json
from discord.ext import commands



    @commands.command(aliases=['ny'])
    async def newyear(self, ctx):
        now = datetime.datetime.utcnow()
        ny = datetime.datetime(now.year, 1, 1)
        if ny < now:
            ny = ny.replace(year=now.year + 1)
        delta = ny - now
        weeks, remainder = divmod(int(delta.total_seconds()), 604800)
        days, remainder2 = divmod(remainder, 84000)
        hours, remainder3 = divmod(remainder2, 3600)
        minutes, seconds = divmod(remainder3, 60)
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name=f":confetti_ball:{self.bot.get_emoji(450881603149889539)}Time left until New Year{self.bot.get_emoji(450881603149889539)}:confetti_ball:", value=f'{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.')
        await ctx.send(embed=embed)
        
        
 def setup(bot):
    bot.add_cog(Holiday(bot))       
