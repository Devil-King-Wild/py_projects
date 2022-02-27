import discord
import requests
import os
from discord import Embed, File
from discord.ext import commands

#SCRIPT_RUNNING_DIR
py_run = os.path.dirname(os.path.realpath(__file__))
slic_backslash = r'baz "\"'[5:]
slic2_backslash_ = slic_backslash[:-1]
slash = r"/"
py_run_dir = py_run.replace(f"{slic2_backslash_}", f"{slash}")


#COGS_TEMP_FOLDER
cogs_temp = f"{py_run_dir}/cogs_cache"




#MAIN

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} ready")

    #THIS_PERSON_DOES_NOT_EXIST

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def person(self, ctx):

        does_not_url = requests.get("https://thispersondoesnotexist.com/image")
        with open(f"{cogs_temp}/person_not.png", "wb") as person_png:
            person_png.write(does_not_url.content)
        em_not_persn = discord.Embed(title="HUMAN", color=discord.Color.blue())
        file = discord.File(f"{cogs_temp}/person_not.png", filename="person_not.png")
        em_not_persn.set_image(url="attachment://person_not.png")
        em_not_persn.set_footer(text="genrated by thispersondoesnotexist")
        await ctx.send(file=file, embed=em_not_persn)
        os.remove(f"{cogs_temp}/person_not.png")



    #THIS_CAT_DOES_NOT_EXIST

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx):
        does_not_url = requests.get("https://thiscatdoesnotexist.com/")
        with open(f"{cogs_temp}/cat_not.png", "wb") as person_png:
            person_png.write(does_not_url.content)
        em_not_ct = discord.Embed(title="CAT", color=discord.Color.blue())  # creates embed
        file = discord.File(f"{cogs_temp}/cat_not.png", filename="cat_not.png")
        em_not_ct.set_image(url="attachment://cat_not.png")
        em_not_ct.set_footer(text="genrated by thiscatdoesnotexist")
        await ctx.send(file=file, embed=em_not_ct)
        os.remove(f"{cogs_temp}/cat_not.png")





def setup(client):
    client.add_cog(fun(client))