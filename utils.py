import discord
from discord.utils import get


async def get_or_create_category(name: str, guild: discord.Guild) -> discord.CategoryChannel:
    category = get(guild.categories, name=name)
    if category is None:
        return await guild.create_category(name=name)
    else:
        return category


async def get_or_create_role(name: str, guild: discord.Guild) -> discord.Role:
    role = get(guild.roles, name=name)
    if role is None:
        return await guild.create_role(name=name)
    else:
        return role


def format_channel_name(text: str):
    return text.lower().replace(" ", "-")
