from discord.ext import commands


class normal(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} ready")

    #commands
    @commands.command()
    async def dawdadaw(self, ctx):
        await ctx.send('Pong!')







def setup(client):
    client.add_cog(normal(client))