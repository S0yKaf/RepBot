import re

import discord

import config
from Models.User import User
from Commons import verify, update_rank

class RepAdd():

    def __init__(self) -> None:
        pass


    async def init(self, client: discord.Client):
        guilds = client.guilds
        for g in guilds:
            await self.setup_roles(g)

    async def setup_roles(self, guild):
        roles = [r.name for r in guild.roles]
        for r in config.RANKS:
            if r[1] not in roles:
                await guild.create_role(name=r[1])

    async def process(self, message, client: discord.client):
        if not verify(message,client):
            return

        match = re.search("\+rep <(.*)>(?:\s+(\d+))?", message.content)

        if not match or not match.group(1):
            return

        user = match.group(1)
        rep = match.group(2) or 1
        u = User(user, message.mentions.pop().name)
        amount = u.add_rep(rep)
        #await client.get_channel(message.channel.id).send(f"<{user}> has gained +{amount} rep!")
        updated = await update_rank(u, message.guild, client)
        if updated:
            await client.get_channel(message.channel.id).send(f"<{user}> is now a {updated}!")

