import discord
import sys
import os
import io
import asyncio
import json
from discord.ext import commands


class Mod:
    def __init__(self, bot):
        self.bot = bot
        
        
        
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
            await ctx.send(" Cant delete messages without perms.")
            
            
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
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member = None):
        """Mute a member"""
        if user is None:
            return await ctx.send("Please tag that annoying member to mute them!")
        try:
            await ctx.channel.set_permissions(user, send_messages=False)
            return await ctx.send(f"Lol {user.mention} just got muted. ")
        except commands.errors.MissingPermissions:
            return await ctx.send(":YouTried: You dont have enought permissions.")
        except discord.Forbidden:
            return await ctx.send("00F! I need the **Manage Channel** permission.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, user: discord.Member = None):
        """Unmute a member"""
        if user is None:
            return await ctx.send("Please tag the user in order to unmute them")
        try:
            await ctx.channel.set_permissions(user, send_messages=True)
            return await ctx.send(f"Times up, {user.mention}. You just got unmuted.")
        except commands.errors.MissingPermissions:
            return await ctx.send(":YouTried: Cant unmute people with out perms")
        except discord.Forbidden:
            return await ctx.send("00F! I need the **Manage Channel** permission.")

            
            
def setup(bot): 
    bot.add_cog(Mod(bot))              
