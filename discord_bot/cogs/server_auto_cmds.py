from discord.ext import commands


class normal(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} ready")

    # JOIN MSG

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has reached at hell.")

    #LEAVE MSG

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has passed away.")


    #commands
    @commands.command()
    async def PING(self, ctx):
        await ctx.send('Pong!')







def setup(client):
    client.add_cog(normal(client))