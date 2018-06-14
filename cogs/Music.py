import discord
from discord.ext import commands
import asyncio
import os
import aiohttp
import youtube_dl


YOUTUBE_DL_OPTIONS = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto'
}


ffmpeg_options = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(YOUTUBE_DL_OPTIONS)

if not discord.opus.is_loaded():
    discord.opus.load_opus('libopus.so')

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    def get_duration(self):
        return self.data.get('duration')

    @classmethod
    async def from_url(cls, url, *, loop=None):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] #if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music:
    def __init__(self, bot):
       self.bot = bot
       
       
       
@commands.command()
async def play(self, ctx, url):
    """Play a song of your choice"""
    player = await YTDLSource.from_url(url, loop=self.bot.loop)
    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None, loop=self.bot.loop).result())
    
    

def setup(bot):
    bot.add_cog(Music(bot))
