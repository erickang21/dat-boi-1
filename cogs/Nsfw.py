import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import lists
from lists import blist, plist, alist


class Nsfw:
    '''
    xd
    '''
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def boobs(self, ctx):
        '''Get boobs off the internet'''
        if not ctx.channel.is_nsfw():
          await ctx.send("Tried to put nsfw in a non-nsfw channel.")
          return
        """Random"""
        api_base = 'http://api.oboobs.ru/boobs/'
        number = random.randint(1, 10303)
        url_api = api_base + str(number)
        async with aiohttp.ClientSession() as session:
           async with session.get(url_api) as data:
                data = await data.json()
                data = data[0]
        image_url = 'http://media.oboobs.ru/' + data['preview']
        em = discord.Embed(color=passcolor)
        em.set_author(name="Random image")
        em.set_image(url=image_url)
        em.set_footer(text=f"Requested by ur mom")
        await ctx.send(embed=em)


def setup(bot): 
    bot.add_cog(Nsfw(bot)) 
