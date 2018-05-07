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
        
    @commands.command(aliases=['info', 'botinfo'])
    async def stats(self, ctx):
        """Stats for me"""
        total_members = 0
        for guild in self.bot.guilds:
            total_members = len(guild.members) + total_members
        em = discord.Embed(color=discord.Color(value=0x00ff00), title='Bot Info')
        em.description = "My Infomation"
        em.add_field(name='Creator', value='L3NNY#4519')
        em.add_field(name='Developers', value='**1:** dat banana boi#1982\n**2:** CyRIC#0847')
        em.add_field(name='Servers', value=f'{len(self.bot.guilds)}')
        em.add_field(name='Total Members', value=total_members)
        em.add_field(name='Version', value='0.0.2')
        em.add_field(name='Start Date', value='4/24/2018')
        em.add_field(name='Coding Language', value='Python')
        em.add_field(name='Coding Libary', value='discord.py')
        await ctx.send(embed=em)
        
        
    @commands.command()
    async def blame(self, ctx, *, text=None):
        await ctx.trigger_typing()
        try:
            await ctx.send(file=discord.File(await self.client.blame(str(text)), "blame.png"))
        except Exception as e:
            await ctx.send(f"An error occured with IdioticAPI. \nMore details: \n{e}")    
                        
                
    @commands.command()
    async def gay(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(file=discord.File(await self.client.rainbow(user.avatar_url), "gay.png"))
        except Exception as e:
            await ctx.send(f"An error occured with IdioticAPI. \nMore details: \n{e}")
            
            
def setup(bot):
    bot.add_cog(Fun(bot))
