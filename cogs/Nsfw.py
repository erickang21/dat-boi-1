import discord
from discord.ext import commands
import aiohttp
import random

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
          await ctx.send("You tried to put nsfw in a non-nsfw channel.")
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
        em = discord.Embed(color=0x11f95e)
        em.set_author(name="Boob Image")
        em.set_image(url=image_url)
        await ctx.send(embed=em)
        
        
        
        @commands.command()
        @commands.guild_only()
        @commands.cooldown(1, 0.5, BucketType.user)
        async def hentai(ctx):
            textchannel = ctx.message.channel
            await textchannel.trigger_typing()
            time.sleep(0.5)
            ch = ctx.message.channel
            if ch.is_nsfw():
                page = await bot.http._session.get('https://nekos.life/api/v2/img/Random_hentai_gif')
                neko = await page.json()
                em = discord.Embed(title="Heres your hentai", color=0x11f95e)
                em.set_image(url=neko['url'])
                await ctx.send(embed=em)

            else:
                embed = discord.Embed(title="You tried hentai in a non-nsfw channel. :face_palm:", color=0x11f95e)
                await ctx.send(embed=embed)


def setup(bot): 
    bot.add_cog(Nsfw(bot)) 
