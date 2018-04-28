import discord
import sys
import os
import io
import asyncio
import json
from discord.ext import commands


class mod:
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
            
            
def setup(bot): 
    bot.add_cog(mod(bot))              
