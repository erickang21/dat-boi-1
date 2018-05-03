import discord
from discord.ext import commands
import asyncio
import aiohttp
import os
import json

class ClashRoyale:

    def __init__(self, bot):
        self.bot = bot
        with open('data/config.json') as f:
            config = json.load(f)
            if 'CR_TAG' not in config:
                tag = None
            else:
                tag = config['CR_TAG']
        self.tag = os.environ.get('CR_TAG') or tag
        self.client = crasync.Client()


    @commands.command()
    async def profile(self, ctx, tag=None):
        '''Fetch a Clash Royale Profile!'''
        em = discord.Embed(title="Profile")
        em.color = await ctx.get_dominant_color(ctx.author.avatar_url)
        if tag == None:
            tag = self.tag
            if tag == None:
                em.description = "Please add `CR_TAG` to your config."
                return await ctx.send(embed=em)
        try:
            profile = await self.client.get_profile(tag)
        except:
            em.description = "Either API is down or that's an invalid tag."
            return await ctx.send(embed=em)

        em.title = profile.name
        em.description = f"#{tag}"
        em.url = f"http://cr-api.com/profile/{tag}"
        try:
            em.set_author(name="Profile", icon_url=profile.clan_badge_url)
        except:
            em.set_author(name='Profile')

        await ctx.send(embed=em) 



    @commands.command()
    async def crsave(self, ctx, tag=None):
        """Save Clash Royale your tag"""
        #crdb = self.getcoll("clashroyale")
        authorID = str(ctx.author.id)
        if not tag:
            return await ctx.send(f'Please provide a tag `Usage: crsave tag`')
        tag = tag.strip('#').replace('O', '0')
        if not self.check_tag:
            return await ctx.send('Invalid Tag. Please make sure your tag is correct then try again')
        await self.save_tag(tag, authorID)
        await ctx.send(f':white_check_mark: Your tag `#{tag}` has been successfully saved to your discord account.')
        
        
    @commands.command()
    async def crprofile(self, ctx, tag: str=None):
        '''Gets your Clash Royale Profile using Tag'''
        authorID = str(ctx.author.id)
        if not tag:
            if await self.get_tag(authorID) == 'None':
                await ctx.send(f'Please provide a tag or save your tag using `{ctx.prefix}crsave <tag>`')
            tag = await self.get_tag(authorID)
        profile = await self.client.get_player(tag)

        chests = self.get_chests(ctx, profile)[0]
        special = self.get_chests(ctx, profile)[1]

        hasClan = True
        try:
            clan = await profile.get_clan()
        except Exception as e:
            hasClan = False

        embeds = []

        em = discord.Embed(color=discord.Color.gold())
        em.title = profile.name
        em.description = f'{tag}\'s info'
        em.add_field(name='Trophies', value=profile.trophies)
        em.add_field(name='Personal Best', value=profile.stats.maxTrophies)
        em.add_field(name='Arena', value=profile.arena.name)
        em.add_field(name='League', value=profile.arena.arena)
        em.add_field(name='Rank', value=profile.rank)
        em.add_field(name='Wins', value=profile.games.wins)
        em.add_field(name='Wins', value=profile.games.wins)
        em.add_field(name='Losses', value=profile.games.losses)
        em.add_field(name='Draws', value=profile.games.draws)
        em.add_field(name='Cards Found', value=profile.stats.cardsFound)
        em.add_field(name='Favorite card:', value=profile.stats.favorite_card.name)
        em.add_field(name='Chest Cycle:', value=chests, inline=False)
        em.add_field(name='Chests Until:', value=special, inline=False)
        em.set_footer(text=f'Clash Royale Profile')
        embeds.append(em)
         
        
def setup(bot):
    bot.add_cog(ClashRoyale(bot))
