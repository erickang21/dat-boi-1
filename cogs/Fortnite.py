import discord
import sys
import os
import io
import datetime
import asyncio
import aiohttp
import random
import json
from discord.ext import commands



class Fortnite:
    def __init__(self, bot):
        self.bot = bot
  
    
    @commands.command()
    async def fortnite(self, ctx):
        await ctx.send("https://www.epicgames.com/fortnite/en-US/home")
        
        
    @commands.command()
    async def profile(self, ctx, *, name: str):
        info = await self.client.get_user(name)
        embed = style_embed(ctx, title='Info about {}'.format(info.username))
        embed.add_field(name='User id', value=str(info.id))
        stats = await info.stats.get()
        embed.add_field(name='Solo stats', value='Score: {score}\nMatches: {matches}\nTop 12: {top12}\n Wins: {wins}\nTime:{time}\nTop 5: {top5}\nKills: {kills}'.format(
            score=stats['solo']['score'],
            matches=stats['solo']['matches'],
            top12=stats['solo']['top12'],
            wins=stats['solo']['wins'],
            time=stats['solo']['time'],
            top5=stats['solo']['top5'],
            kills=stats['solo']['kills']
        ), inline=False)
        embed.add_field(name='Duo stats', value='Score: {score}\nMatches: {matches}\nTop 12: {top12}\n Wins: {wins}\nTime:{time}\nTop 5: {top5}\nKills: {kills}'.format(
            score=stats['duo']['score'],
            matches=stats['duo']['matches'],
            top12=stats['duo']['top12'],
            wins=stats['duo']['wins'],
            time=stats['duo']['time'],
            top5=stats['duo']['top5'],
            kills=stats['duo']['kills']
        ), inline=False)
        embed.add_field(name='Squad stats', value='Score: {score}\nMatches: {matches}\nTop 12: {top12}\n Wins: {wins}\nTime:{time}\nTop 5: {top5}\nKills: {kills}'.format(
            score=stats['squad']['score'],
            matches=stats['squad']['matches'],
            top12=stats['squad']['top12'],
            wins=stats['squad']['wins'],
            time=stats['squad']['time'],
            top5=stats['squad']['top5'],
            kills=stats['squad']['kills']
        ), inline=False)
        embed.add_field(name='Total stats', value='Score: {score}\nMatches: {matches}\nTop 12: {top12}\n Wins: {wins}\nTime:{time}\nTop 5: {top5}\nKills: {kills}\nTop 3: {top3}\nTop 6: {top6}\nTop 10: {top10}\n Top 25: {top25}'.format(
            score=stats['all']['score'],
            matches=stats['all']['matches'],
            top12=stats['all']['top12'],
            wins=stats['all']['wins'],
            time=stats['all']['time'],
            top5=stats['all']['top5'],
            kills=stats['all']['kills'],
            top3=stats['all']['top3'],
            top6=stats['all']['top6'],
            top10=stats['all']['top10'],
            top25=stats['all']['top25']
        ), inline=False)
        await ctx.send(embed=embed)
    
    
def setup(bot):
    bot.add_cog(Fortnite(bot))
