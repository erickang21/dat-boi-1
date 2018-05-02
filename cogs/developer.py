import discord
from discord.ext import commands
import subprocess
import io
import textwrap
import traceback
from contextlib import redirect_stdout


class Developer:
    def __init__(self, bot):
       self.bot = bot
       self.sessions = set()
       
       
       
       
    @commands.command()
    @commands.is_owner()
    async def shutdown(ctx):
        await ctx.send("Shutting down...")
        await self.bot.logout()
        
        
        
def setup(bot):
    bot.add_cog(Developer(bot))
        
