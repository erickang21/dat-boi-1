import discord
import sys
import os
import io
import asyncio
from discord.ext import commands

class Math:
    def __init__(self, bot):
       self.bot = bot
                         
    @commands.command()
    async def add(self, ctx, num: int, num2: int):
        '''Add those numbers!'''
        if num is None:
            await ctx.send("+add [number] [number]")
        else:
            await ctx.send(num + num2)

    @commands.command()
    async def subtract(self, ctx, num: int, num2: int):
        '''Subtract those numbers!'''
        if num is None:
            await ctx.send("+subtract [number] [number]")
        else:
            await ctx.send(num - num2)

    @commands.command()
    async def multiply(self, ctx, num: int, num2: int):
        '''Multiply numberbers with the big X'''
        if num is None:
            await ctx.send("+multiply [number] [number]")
        else:
            await ctx.send(num * num2)
     
    @commands.command()
    async def divide(self, ctx, num: int, num2: int):
        '''Divide those numbers'''
        if num is None:
            await ctx.send("+divide [number] [number]")
        else:
            await ctx.send(num / num2)
       
def setup(bot): 
    bot.add_cog(Math(bot))  
