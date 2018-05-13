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
       

    @commands.command()
    async def power(self, ctx, a: int, b: int):
        '''Raise A to the power of B'''
        if a > 100 or b > 100:
            return await ctx.send("Numbers are too large.")
        em = discord.Embed(color=discord.Color.green())
        em.title = "Result"
        em.description = f'❓ Problem: `{a}^{b}`\n✅ Solution: `{a ** b}`'
        await ctx.send(embed=em)


def setup(bot): 
    bot.add_cog(Math(bot))  
