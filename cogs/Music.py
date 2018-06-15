import asyncio
import discord
import youtube_dl
from discord.ext import commands

ytdl = youtube_dl.YoutubeDL({
    'format': 'bestaudio/best',
    'default_search': 'auto',
    'source_address': '0.0.0.0',
    'quiet': True
})
ffmpeg_options = {
    'before_options': '-nostdin',
    'options': '-vn'
}

class Download(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data):
        super().__init__(source, 0.5)
        self.data = data
    
    @classmethod
    async def from_search_or_url(cls, video, loop=None):
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(video, download=False))
        if 'entries' in data:
            data = data['entries'][0]
        
        filename = data['url']
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def play(self, ctx, *, search):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                return await ctx.send(":x: **Please get in a voice channel first.**")

            async with ctx.typing():
                try:
                    player = await Download.from_search_or_url(video=search, loop=self.bot.loop)
                    ctx.voice_client.play(player)
                    await ctx.send("Song started playing, atleast I hope so.")
                except Exception as e:
                    return await ctx.send(":thinking: There was a error:\n```py\n{}: {}```".format(type(e).__name__, e))
        else:
            return await ctx.send(":x: **I am already playing audio here, the queue system will come later.**")

def setup(bot):
    bot.add_cog(Music(bot))
