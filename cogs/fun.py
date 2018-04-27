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
            roasts = ["is 1% gay :gay_pride_flag:", "is 2% gay :gay_pride_flag:", "is 3% gay :gay_pride_flag:", "is 4% gay :gay_pride_flag:", "is 5% gay :gay_pride_flag:", "is 6%  gay :gay_pride_flag:", "is 7% gay :gay_pride_flag:", "is 8% gay :gay_pride_flag:", "is 9% gay :gay_pride_flag:", "is 10% gay :gay_pride_flag:", "is 11% gay :gay_pride_flag:", "is 12% gay :gay_pride_flag:", "is 13% gay :gay_pride_flag:", "is 14% gay :gay_pride_flag:", "is 15% gay :gay_pride_flag:", "is 16% gay :gay_pride_flag:", "is 17% gay :gay_pride_flag:", "is 18% gay :gay_pride_flag:", "is 19% gay :gay_pride_flag:", "is 20% gay :gay_pride_flag:", "is 21% gay :gay_pride_flag:", "is 22% gay :gay_pride_flag:", "is 23% gay :gay_pride_flag:", "is 24% gay :gay_pride_flag:", "is 25% gay :gay_pride_flag:", "is 26% gay :gay_pride_flag:", "is 27% gay :gay_pride_flag:", "is 28% gay :gay_pride_flag:", "is 29% gay :gay_pride_flag:", "is 30% gay :gay_pride_flag:", "is 31% gay :gay_pride_flag:", "is 32% gay :gay_pride_flag:", "is 33% gay :gay_pride_flag:", "is 34% gay :gay_pride_flag:", "is 35% gay :gay_pride_flag:", "is 36% gay :gay_pride_flag:", "is 37% gay :gay_pride_flag:", "is 38% gay :gay_pride_flag:", "is 39% gay :gay_pride_flag:", "is 40% gay :gay_pride_flag:", "is 41% gay :gay_pride_flag:", "is 42% gay :gay_pride_flag:", "is 43% gay :gay_pride_flag:", "is 44% gay :gay_pride_flag:". "is 45% gay :gay_pride_flag:", "is 46% gay :gay_pride_flag:", "is 47% gay :gay_pride_flag:", "is 48% gay :gay_pride_flag:", "is 49% gay :gay_pride_flag:", "is 50% gay :gay_pride_flag:", "is 51% gay :gay_pride_flag:", "is 52% gay :gay_pride_flag:", "is 53% gay :gay_pride_flag:", "is 54% gay :gay_pride_flag:", "is 55% gay :gay_pride_flag:", "is 56% gay :gay_pride_flag:", "is 57% gay :gay_pride_flag:", "is 58% gay :gay_pride_flag:", "'is 59% gay :gay_pride_flag:", "is 60% gay :gay_pride_flag:", "is 61% gay :gay_pride_flag:", "is 61% gay :gay_pride_flag:", "is 62% gay :gay_pride_flag:", "is 63% gay :gay_pride_flag:", "is 64% gay :gay_pride_flag:", "is 65% gay :gay_pride_flag:", "is 66% gay_pride_flag:", "is 67% gay :gay_pride_flag:", "is 68% gay :gay_pride_flag:", "is 69% gay :gay_pride_flag:", "is 70% gay :gay_pride_flag:", "is 71% gay :gay_pride_flag:", "is 72% gay :gay_pride_flag:", "is 73% gay :gay_pride_flag:", "is 74% gay :gay_pride_flag:", "is 75% gay :gay_pride_flag:" ]
            await ctx.send(f"{user.mention} {random.choice(roasts)}")
        except commands.errors.BadArgument:
            return await ctx.send(f":no_entry_sign: **{user}**, is not a valid username or mention")
            
            
def setup(bot):
    bot.add_cog(Fun(bot))
