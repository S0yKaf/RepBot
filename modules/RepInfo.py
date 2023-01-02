import re

import discord

import config
from Models.User import User

class RepInfo():

    def __init__(self) -> None:
        pass


    async def init(self, client: discord.Client):
        pass

    async def process(self, message, client: discord.client):
        match = re.search("\\?rep <(.*)>", message.content)
        if not match or not match.group(1):
            return

        match = match.group(1)
        user = User(match)

        status = f"""
```yaml
Rank: {config.RANKS[user.rank][1]}
Reputation: {user.rep}
Discount: {config.RANKS[user.rank][2]}%

```
"""
        await client.get_channel(message.channel.id).send(status)

