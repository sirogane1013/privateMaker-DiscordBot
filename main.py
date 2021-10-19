import os

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

import settings

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print("Logged in")


@bot.command()
async def mkch(ctx):
    prefix = settings.CHANNEL_PREFIX
    guild = ctx.guild
    author = ctx.author
    author_name = author.display_name
    channel = await guild.create_text_channel(
        prefix + author_name,
        overwrites={
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            author: discord.PermissionOverwrite(read_messages=True),
        })
    await ctx.send(f"Created {channel.mention}")


bot.run(TOKEN)
