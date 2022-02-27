import discord
import os
import asyncio
from assets.modules.LSBSteg import *
from discord.ext import commands, tasks
from discord import Embed, File
from itertools import cycle
from cryptography.fernet import Fernet

#SCRIPT_RUNNING_DIR
py_run = os.path.dirname(os.path.realpath(__file__))
slic_backslash = r'baz "\"'[5:]
slic2_backslash_ = slic_backslash[:-1]
slash = r"/"
py_run_dir = py_run.replace(f"{slic2_backslash_}", f"{slash}")


#MAIN_TEMP_FOLDER
patrick_temp = f"{py_run_dir}/main_cache"


#MAIN

#MAIN_PREFIX
main_prefix = "$"
client = commands.Bot(command_prefix=f'{main_prefix}')


#REMOVED_CMDS
client.remove_command("help")

#READY

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    test_area = client.get_channel(898825076332433448)
    change_status.start()
    await test_area.send("READY")
    print("ready")
    bot_ready_embed = Embed(title="title here")
    #await test_area.send(embed=bot_ready_embed)



#COGS

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("cogs reloaded")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



#BOT STATUS

playing_status = cycle(["Is mayo an instrument?", "I can't see my forehead!", "Sandy's a girl?"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(name=next(playing_status)))


#ERROR HANDER

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(' Missing Required Argument. btw You guys talk funny! Say more words.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permssion -___- LOL')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('is this for me? if it is i don,t want it :(')
    if isinstance(error, commands.CommandOnCooldown):
        cool_down_msg= "[[ hey go slow buddy ]] pls wait for {:.2f}s".format(error.retry_after)
        await ctx.send(cool_down_msg)




#TEST/MS MSG

@client.command()
async def ping(ctx):
    em_ping = Embed(title=f'pong :cloud_lightning: ', description=f'{round(client.latency * 1000)} MS', color=discord.Color.green())
    await ctx.send(embed=em_ping)

#MEME MSG

@client.command()
async def meme(ctx):
    message = await ctx.send("hello")
    await asyncio.sleep(1)
    await message.edit(content="█")
    await message.edit(content="██")
    await message.edit(content="███")
    await message.edit(content="████")
    await message.edit(content="█████")
    await message.edit(content="██████")
    await message.edit(content="███████")
    await message.edit(content="████████")
    await message.edit(content="█████████")
    await message.edit(content="██████████")
    await message.edit(content="███████████")
    await message.edit(content="████████████")





#hide_text_to_img

@client.command()
async def hide(ctx, secr):
    await ctx.author.avatar_url.save(f"{patrick_temp}/normal_img.png")
    steg = LSBSteg(cv2.imread(f"{patrick_temp}/normal_img.png"))
    img_enco = steg.encode_text(secr)
    cv2.imwrite(f"{patrick_temp}/normal_img.png", img_enco)
    await ctx.send(file=File(f"{patrick_temp}/normal_img.png"))
    os.remove(f"{patrick_temp}/normal_img.png")





#encryo_text

@client.command()
async def enc(ctx, text_to_hide):
    b = bytes(text_to_hide, 'utf-8')
    key = Fernet.generate_key()
    sli_key_main = f"{key}"
    sli_key = sli_key_main[2:]
    em_key = Embed(title="KEY", description=f"{sli_key[:-1]}", color=discord.Color.red())
    em_key.set_footer(text="helped by cryptography")
    await ctx.author.send(embed=em_key)
    f = Fernet(key)
    token = f.encrypt(b)
    sli_token_main = f"{token}"
    sli_token = sli_token_main[2:]
    em_token = Embed(title=":small_red_triangle_down:ENCRYPTED MSG:small_red_triangle_down: ",
                     description=f"{sli_token[:-1]}", color=discord.Color.red())
    em_token.add_field(name="hey", value=f'{ctx.author} check ur DM for key', inline=True)
    em_token.set_footer(text="helped by cryptography")
    await ctx.send(embed=em_token)
    await ctx.message.delete()





@client.command()
async def dec(ctx, key, token):
    b_key = f'{key}'.encode('utf-8')
    f = Fernet(b_key)
    b_token = f'{token}'.encode('utf-8')
    pure_text=f.decrypt(b_token)
    sli_pure_text = f"{pure_text}"
    sli_pure_text_main = sli_pure_text[2:]
    em_MASG = Embed(title="MSG", description=f"{sli_pure_text_main[:-1]}", color=discord.Color.red())
    em_MASG.set_footer(text="helped by cryptography")
    await ctx.author.send(embed=em_MASG)
    await ctx.message.delete()


@client.command()
async def help(ctx):
    em_help = Embed(title=f'HELP', description=f"prefix is {main_prefix}\n start with this {main_prefix} for cmds", color=discord.Color.blue())
    em_help.add_field(name="SCIENCE YARD", value='qr - to make custom qrcode \n hide - to hide text to img', inline=True)
    em_help.set_footer(text="with love <3 patrick")
    await ctx.send(embed=em_help)







client.run('### API KEY HERE ###')


####################################################################\END\#################################################################################



