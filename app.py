import discord
import asyncio

import config
import modules

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot is ready!")
    for m in modules.plugins:
        await m.init(client)


@client.event
async def on_message(message):
    for m in modules.plugins:
        await m.process(message, client)


client.run(config.BOT_KEY)
