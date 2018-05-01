import discord
import sys
import os
import io
import asyncio
import psutil
import time
import textwrap
from discord.ext import commands


class Info:
    def __init__(self, bot):
        self.bot = bot
        self.starttime = self.bot.starttime



    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, member : discord.Member=None):
        """Returns a avatar"""
        member = member or ctx.author
        av = member.avatar_url
        if ".gif" in av:
            av += "&f=.gif"
        em = discord.Embed(url=av)
        em.colour = (discord.Colour(0xed791d))
        em.set_author(name=str(member), icon_url=av)
        em.set_image(url=av)
        try:
            await ctx.send(embed=em)
        except:
            return

    @commands.command(aliases=['servericon'], no_pm=True)
    async def serverlogo(self, ctx):
        """Returns the server's logo"""
        icon = ctx.guild.icon_url
        em = discord.Embed(url=icon)
        em.colour = (discord.Colour(0xed791d))
        em.set_author(name=ctx.guild.guilder.name, icon_url=icon)
        em.set_image(url=icon)
        try:
            await ctx.send(embed=em)
        except:
            return
            
    @commands.command(aliases=['ui'], no_pm=True)
    async def userinfo(self, ctx, *, member : discord.Member=None):
        '''Get information about a member of a guild'''
        guild = ctx.guild or None
        user = member or ctx.message.author
        avi = user.avatar_url
        time = ctx.message.created_at
        desc = '{0} is chilling in {1} mode.'.format(user.name, user.status)
        em = discord.Embed(description=desc, timestamp=time)

        if guild:
            member_number = sorted(guild.members, key=lambda m: m.joined_at).index(user)+1
            roles = sorted(user.roles, key=lambda c: c.position)
            for role in roles:
                if str(role.color) != "#000000":
                    color = role.color
            rolenames = ', '.join([r.name for r in roles if r.name != "@everyone"]) or 'None'
            em.add_field(name='Nick', value=user.nick, inline=True)
            em.add_field(name='Member No.',value=str(member_number),inline = True)

        if 'color' not in locals():
            color = 0
        em.color = color
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y'))

        if guild:
            em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y'))
            em.add_field(name='Roles', value=rolenames, inline=True)

        em.set_footer(text='User ID: '+str(user.id))
        em.set_thumbnail(url=avi)
        em.set_author(name=user, icon_url=guild.icon_url)

        await ctx.send(embed=em)
        
        
def setup(bot): 
    bot.add_cog(Info(bot)) 
