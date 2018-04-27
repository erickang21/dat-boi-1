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


class Fun:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=["xmas"])
    async def christmas(self,ctx):
        now=datetime.datetime.utcnow()
        xmas=datetime.datetime(now.year, 12, 25)
        if xmas<now:
            xmas=xmas.replace(year=now.year+1)
        delta=xmas-now
        weeks, remainder=divmod(int(delta.total_seconds()), 604800)
        days, remainder2=divmod(remainder, 86400)
        hours, remainder3=divmod(remainder2, 3600)
        minutes, seconds=divmod(remainder3, 60)
        embed=discord.Embed(color=0x11f95e)
        embed.add_field(name=":gift::christmas_tree::santa:Time left until Christmas:santa::christmas_tree::gift:", 
            value=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
        await ctx.send(embed=embed)
    
    
    @commands.command()
    async def expose(self, ctx, user: discord.Member = None):
        '''Expose someone!'''
        if user is None:
            return await ctx.send(":no_entry_sign: **You need to mention a user.**")
        try:
            roasts = ["likes https://pornhub.com/, I found it in their history", "is super gay.", "likes your mom.", "copies code from my creator.", "is Adolf Hitler's son.", "is 97% gay :gay_pride_flag:", "is triple gay."]
            await ctx.send(f"{user.mention} {random.choice(roasts)}")
        except commands.errors.BadArgument:
            return await ctx.send(f":no_entry_sign: **{user}**, is not a valid username or mention")
            
            
    @commands.command()
    async def gayrate(self, ctx, user: discord.Member = None):
        '''See how gay you are.'''
        if user is None:
            return await ctx.send(":no_entry_sign: **You need to mention a user.**")
        try:
            roasts = ["is 1% gay :gay_pride_flag:", "is 2% gay :gay_pride_flag:", "is 3% gay :gay_pride_flag:", "is 4% gay :gay_pride_flag:", "is 5% gay :gay_pride_flag:", "is 6%  gay :gay_pride_flag:", "is 7% gay :gay_pride_flag:", "is 8% gay :gay_pride_flag:", "is 9% gay :gay_pride_flag:", "is 10% gay :gay_pride_flag:", "is 11% gay :gay_pride_flag:", "is 12% gay :gay_pride_flag:", "is 13% gay :gay_pride_flag:", "is 14% gay :gay_pride_flag:", "is 15% gay :gay_pride_flag:", "is 16% gay :gay_pride_flag:", "is 17% gay :gay_pride_flag:", "is 18% gay :gay_pride_flag:", "is 19% gay :gay_pride_flag:", "is 20% gay :gay_pride_flag:", "is 21% gay :gay_pride_flag:", "is 22% gay :gay_pride_flag:", "is 23% gay :gay_pride_flag:"]
            await ctx.send(f"{user.mention} {random.choice(roasts)}")
        except commands.errors.BadArgument:
            return await ctx.send(f":no_entry_sign: **{user}**, is not a valid username or mention")
            
            
def setup(bot):
    bot.add_cog(Fun(bot))
