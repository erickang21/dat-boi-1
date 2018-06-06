import discord
import sys
import os
import io
import asyncio
import time
import textwrap
from discord.ext import commands



class Info:
    def __init__(self, bot):
        self.bot = bot 
        
        
        
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def avatar(self, ctx, *, member: discord.Member = None):
        '''Gets someones profile picture'''
        member = member or ctx.author
        av = member.avatar_url
        if ".gif" in av:
            av += "&f=.gif"
        em = discord.Embed(title="Avatar", url=av, color=0x11f95e)
        em.set_author(name=str(member)
        em.set_image(url=av)
        await ctx.send(embed=em)
        
        
    @commands.command()
    async def userinfo(self, ctx, user: discord.Member = None):
        """Get a users info"""
        if user is None:
            user = ctx.author
        color = discord.Color(value=0x11f95e)
        em = discord.Embed(color=color, title=f'{user.name}')     
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %B %d, %Y'))
        em.add_field(name='ID', value=f'{user.id}')
        em.add_field(name="Highest Role", value=user.top_role)
        em.add_field(name='Currently Playing', value=user.activity if user.activity else 'None')
        em.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=em)  
        
        
        
def setup(bot):
    bot.add_cog(Info(bot))
