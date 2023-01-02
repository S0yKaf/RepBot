import discord

import config
from Models.User import User


async def update_rank(user: User, guild, client):

    rank = config.RANKS[user.rank][1]
    member = guild.get_member(int(user.name.removeprefix("@")))
    member_roles = [r.name for r in member.roles]
    if rank in member_roles:
        return
    role = discord.utils.get(guild.roles, name=rank)
    for r in config.RANKS:
        # I don't want to fuck with how to pass these as arguments all at once,
        # idk why I can't just give it an array, fuckers...
        old_role = discord.utils.get(guild.roles, name=r[1])
        await member.remove_roles(old_role)

    await member.add_roles(role)
    return rank

def verify(message, client):
    role_names = [r.name for r in message.author.roles]

    for role in config.ALLOWED_ROLES:
        if role in role_names:
            return True

    return False
