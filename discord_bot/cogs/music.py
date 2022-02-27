import discord
import os
from discord.ext import commands

#SCRIPT_RUNNING_DIR
py_run = os.path.dirname(os.path.realpath(__file__))
slic_backslash = r'baz "\"'[5:]
slic2_backslash_ = slic_backslash[:-1]
slash = r"/"
py_run_dir = py_run.replace(f"{slic2_backslash_}", f"{slash}")

class music(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} ready")

    #commands
    @commands.command()
    async def play(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
            voice_channel.play(discord.FFmpegPCMAudio(f"{py_run_dir}assets/songs/song.mp3"))

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()







def setup(client):
    client.add_cog(music(client))