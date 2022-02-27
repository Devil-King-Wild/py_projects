import os
import qrcode
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

class normal(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} ready")


    # QRCODE MSG

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def qr(self, ctx, qr_url):
        QR_URL = qrcode.make(qr_url)
        QR_URL.save(f"{cogs_temp}/req_qrcode.png")
        await ctx.send(file=File(f"{cogs_temp}/req_qrcode.png"))
        os.remove(f"{cogs_temp}/req_qrcode.png")





def setup(client):
    client.add_cog(normal(client))