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

    def handle_uptime(self):
        uptime = ""
        second = time.time() - self.bot.starttime
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        day, hour = divmod(hour, 24)
        week, day = divmod(day, 7)

        if week > 0:
            if week >= 1:
                uptime += "%d weeks, " % (week)
            else:
                uptime += "%d week, " % (week)
        else:
            uptime += ""

        if day > 0:
            if day >= 1:
                uptime += "%d days, " % (day)
            else:
                uptime += "%d day, " % (day)
        else:
            uptime += ""

        if hour > 0:
            if hour >= 1:
                uptime += "%d hours, " % (hour)
            else:
                uptime += "%d hour, " % (hour)
        else:
            uptime += ""

        if minute > 0:
            if minute >= 1:
                uptime += "%d minutes, " % (minute)
            else:
                uptime += "%d minute, " % (minute)
        else:
            uptime += ""

        if second > 0:
            uptime += "%d seconds" % (second)
        else:
            uptime += "%d second" % (second)

            return uptime

    @commands.command(aliases=['info', 'botinfo'])
    async def stats(self, ctx):
        """Stats for me"""
        total_members = 0
        for guild in self.bot.guilds:
            total_members = len(guild.members) + total_members
        em = discord.Embed(color=discord.Color(value=0x00ff00), title='Bot Info')
        em.description = "My sweet, sweet info!"
        em.add_field(name='Bot Creator', value='0.1.1')
        em.add_field(name='Coders', value='**1:** TheEmperor™#2644\n**2:** CyRIC#0847\n**3:** Ice#1234')
        em.add_field(name='Servers', value=f'{len(self.bot.guilds)}')
        em.add_field(name='Total Members', value=total_members)
        em.add_field(name='Version', value='0.1.1')
        em.add_field(name='Start Date', value='2/13/2018')
        em.add_field(name='Coding Language', value='Python, discord.py')
        em.add_field(name='Current Uptime', value=self.handle_uptime())
        await ctx.send(embed=em)
        
        
    @commands.command()
    async def serverstats(self, ctx):
        """Just server stats"""
        guild = ctx.guild
        roles = [x.name for x in guild.roles]
        role_length = len(roles)
        channels = len(guild.channels)
        time = str(guild.created_at.strftime("%b %m, %Y, %A, %I:%M %p"))         
        em = discord.Embed(description= "The Statistics for this server", title='Server Stats', colour=0xffffff)
        em.set_thumbnail(url=guild.icon_url)
        em.add_field(name='__Server __', value=str(guild.name))
        em.add_field(name='__Owner__', value=str(guild.owner))
        em.add_field(name='__Owner ID__', value=guild.owner_id) 
        em.add_field(name='__Members__', value=str(guild.member_count))
        em.add_field(name='__Total Channels__', value=str(channels))
        em.add_field(name='__Region__', value='%s' % str(guild.region))
        em.add_field(name='__ Total Roles__', value='%s' % str(role_length))
        em.add_field(name="__Total Roles (Listed)__", value=', '.join(roles))
        em.set_footer(text='Created - %s' % time)        
        await ctx.send(embed=em)
        
        
def setup(bot):
    bot.add_cog(Info(bot))
