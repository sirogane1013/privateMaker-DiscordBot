import os
from typing import List, Dict, Union

import discord
from discord.ext import commands
from dotenv import load_dotenv

import settings
from utils import get_or_create_category, get_or_create_role, format_channel_name

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print("Logged in")


@bot.command()
async def mkch(ctx):
    guild: discord.Guild = ctx.guild
    author: discord.User = ctx.author
    author_name: str = author.display_name
    channel_name: str = format_channel_name(settings.CHANNEL_PREFIX + author_name)
    category: discord.CategoryChannel = await get_or_create_category(settings.CHANNEL_CATEGORY, guild)
    channel: discord.TextChannel = discord.utils.get(guild.text_channels, name=channel_name, category=category)

    if channel is not None:
        await ctx.send(f"{channel.mention} already exists")
        return

    readable_roles: List[discord.Role] = [await get_or_create_role(n, guild) for n in settings.CHANNEL_READABLE_ROLES]
    overwrites = make_whitelist(readable_roles + [author], guild)
    channel = await guild.create_text_channel(channel_name, category=category, overwrites=overwrites)
    await ctx.send(f"Created {channel.mention}")
    return


def make_whitelist(roles: List[Union[discord.Role, discord.User]], guild: discord.Guild) \
        -> Dict[discord.Role, discord.PermissionOverwrite]:
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
    }
    for role in roles:
        overwrites[role] = discord.PermissionOverwrite(read_messages=True)
    return overwrites


bot.run(TOKEN)
