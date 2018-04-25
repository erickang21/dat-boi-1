import discord
import sys
import os
import io
import asyncio
import json
from discord.ext import commands


class Moderation:
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.db


    @commands.command()
    @commands.has_permissions(administrator = True)
    async def msg(self, ctx, user: discord.Member, *, msg: str):
        """Message someone as me!"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send("The message has been sent! hehehe....")
        except commands.MissingPermissions:
            await ctx.send("rip. you dont have enough perms. xd")
        except:
            await ctx.send(":x: Format: _msg (user tag) (message)")
            
            
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, num: int):
        """Deletes messages. _purge [number]""" 
        try: 
            if num is None:
                await ctx.send("_purge [number]")
            else:
                try:
                    float(num)
                except ValueError:
                    return await ctx.send("The number is invalid. Make sure its a number! _purge [number]")
                await ctx.channel.purge(limit=num+1)
                msg = await ctx.send("Done. ( ͡° ͜ʖ ͡°) ", delete_after=4)
        except discord.Forbidden:
            await ctx.send("I don't have **Manage Messages** permission.")
        except commands.errors.MissingPermissions:
            await ctx.send("Cant delete messages without perms.")
            

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member):
        """Kicks a member out of your server."""
        try:
            await user.kick()
            await ctx.channel.send(f"The administrator is putting their boot on. They kick the boot into {user.mention}'s bottom. {user.mention} has been kicked. ")
        except discord.Forbidden:
            await ctx.send("00F! I need the **Kick Members** permission.")
        except discord.ext.commands.MissingPermissions:
            await ctx.send("Can't kick people without permissions.")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member):
        """Ban a member out of your server."""
        try:
            await user.ban()
            await ctx.channel.send(f"The administrator is getting the ban hammer out of the case. He swings it at {user.mention}. Ouch! {user.mention} has been banned.")
        except discord.Forbidden:
            await ctx.send("00F! I need the **Ban Members** permission.")
        except discord.ext.commands.MissingPermissions:
            await ctx.send("Can't ban people without permissions.")

    @commands.command()
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, user: discord.Member = None):
        '''Mutes a user'''
        if user is None:
            return await ctx.send("Please tag that annoying user to mute them!")

        try:
            await ctx.channel.set_permissions(user, send_messages=False)
            await ctx.send(f"{user.mention} has been muted. FINALLY!")
        except discord.Forbidden:
            return await ctx.send(":x: I don't have **Manage Channel** permmition.")

    @commands.command()
    @commands.has_permissions(mute_members=True)
    async def unmute(self, ctx, user: discord.Member = None):
        '''Un-mutes a user'''
        if user is None:
            return await ctx.send("Please tag a user to unmute them!")

        try:
            await ctx.channel.set_permissions(user, send_messages=True)
            await ctx.send(f"{user.mention} is now un-muted. Hope they learned their lesson.")
        except discord.Forbidden:
            await ctx.send(":x: Couldn't unmute the user. I need the **Manage Channels** permission.")
            
            
def setup(bot): 
    bot.add_cog(mod(bot))              
