import discord
import sys
import os
import io
import datetime
import asyncio
import aiohttp
import random
import json
import idioticapi
from discord.ext import commands


class Fun:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=["xmas"])
    async def christmas(self,ctx):
        now = datetime.datetime.utcnow()
        xmas = datetime.datetime(now.year, 12, 25)
        if xmas < now:
            xmas = xmas.replace(year=now.year + 1)
        delta = xmas - now
        weeks, remainder = divmod(int(delta.total_seconds()), 604800)
        days, remainder2 = divmod(remainder, 86400)
        hours, remainder3 = divmod(remainder2, 3600)
        minutes, seconds = divmod(remainder3, 60)
        embed = discord.Embed(color=0x11f95e)
        embed.add_field(name=":gift::christmas_tree::santa:Time left until Christmas:santa::christmas_tree::gift:", 
            value=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Fun(bot))
