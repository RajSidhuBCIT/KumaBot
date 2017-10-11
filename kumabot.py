import discord
import asyncio
import random

client = discord.Client();

@client.event
async def on_ready():
	print('Logged in as: ')
	print(client.user.name)
	print(client.user.id)
	print('----------')

@client.event
async def on_message(message):
	if message.content.startswith('!flameme'):
		flame = random.choice(["insult1", "insult2", "insult3"])
		await client.send_message(message.channel, flame)
	elif message.content.startswith("!praiseme"):
		await client.send_message(message.channel, "U aite")
client.run('UniqueClientToken') #token removed as it is sensitive data