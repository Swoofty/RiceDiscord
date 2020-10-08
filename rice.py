import discord
import os
from os import environ

class RiceClient(discord.Client):        
    async def on_message(self, message):
        if message.author.id == self.user:
            return
        messageHolder = message.content
        messageHolder = messageHolder.lower()
        if message.author.id == environ[enzo_id]:
            if messageHolder == 'melee' or 'melty' or 'ultimate' or 'trash' or 'bad game' or 'opinion' or 'chungus':
                for member in client.get_all_members():
                    if member.id == environ[enzo_id]:
                        await member.ban(reason = 'Banned for saying keyword', delete_message_days = 0)
        if message.content.startswith('!banenzo'):
            for member in client.get_all_members():
                if member.id == environ[enzo_id]:
                    await member.ban(reason = 'Banned by {message.author.name} via command', delete_message_days = 0)

client = RiceClient()
client.run(environ['bot_key'])