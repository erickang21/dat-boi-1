import discord
import sys
import psutil
import platform
import os
import io
import asyncio
import psutil
import time
from discord.ext import commands

class Info:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=['info', 'botinfo'])
    async def info(self, ctx):
        """My info"""
        total_members = 0
        for guild in self.bot.guilds:
            total_members = len(guild.members) + total_members
        em = discord.Embed(color=discord.Color(value=0x00ff00), title='Bot Info')
        em.description = "My sweet, sweet bot info!"
        em.add_field(name='Creator', value='L3NNY#4519')
        em.add_field(name='Servers', value=f'{len(self.bot.guilds)}')
        em.add_field(name='Total Members', value=total_members)
        em.add_field(name='Version', value='0.1.1')
        em.add_field(name='Start Date', value='4/24/2018')
        em.add_field(name='Coding Language', value='Python, discord.py')
        await ctx.send(embed=em)
        
def setup(bot):
    bot.add_cog(Info(bot))
