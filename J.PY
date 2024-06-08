import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
load_dotenv("j.env")
intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)
@client.command() 
async def ping(ctx): 
    await ctx.send('Pong!') 
token = os.getenv('TOKEN')
@client.event 
async def on_ready(): 
	print("Logged in as a bot {0.user}".format(client))
@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 

	print(f'Message {user_message} by {username} on {channel}') 

	if message.author == client.user: 
		return

	if channel == "bottest": 
		print(f'Message {user_message}')
		if user_message.lower() == "hello" or user_message.lower() == "hi": 
			await message.channel.send(f'Hello {username}') 
			return
		elif user_message.lower() == "bye": 
			await message.channel.send(f'Bye {username}') 
		elif user_message.lower() == "tell me a joke": 
			jokes = [1,2,3] 
			await message.channel.send(random.choice(jokes)) 
	await client.process_commands(message)
client.run(token)

