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
    
    
     @commands.group(invoke_without_command=True)
    @commands.guild_only()
    async def userinfo(self, ctx, *, member: discord.Member = None):
        """Shows info about a member."""

        if member is None:
            member = ctx.author

        e = discord.Embed()
        roles = [role.name.replace('@', '@\u200b') for role in member.roles]
        shared = sum(1 for m in self.bot.get_all_members() if m.id == member.id)
        voice = member.voice
        if voice is not None:
            vc = voice.channel
            other_people = len(vc.members) - 1
            voice = f'{vc.name} with {other_people} others' if other_people else f'{vc.name} by themselves'
        else:
            voice = 'Not connected.'

        e.set_author(name=str(member))
        e.add_field(name='ID', value=member.id)
        e.add_field(name='Servers', value=f'{shared} shared')
        e.add_field(name='Created', value=member.created_at)
        e.add_field(name='Voice', value=voice)
        e.add_field(name='Roles', value=', '.join(roles) if len(roles) < 10 else f'{len(roles)} roles')
        e.colour = member.colour

        if member.avatar:
            e.set_thumbnail(url=member.avatar_url)

        await ctx.send(embed=e)
    
    
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
            
            
            
def setup(bot):
    bot.add_cog(Fun(bot))
