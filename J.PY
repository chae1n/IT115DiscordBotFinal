import discord
from discord.ext import commands
import os
import random
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

#Load enviornment variable from .env file
load_dotenv("j.env")

#Define Discord intents
intents = discord.Intents.default()
intents.messages = True

#Retrieve EC2 metadata
ip_address = ec2_metadata.public_ipv4 or ec2_metadata.private_ipv4
region = ec2_metadata.region
availability_zone = ec2_metadata.availability_zone

#Initialize Dicord Client
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix="!", intents=intents)

#Define command to respond to "ping"
@client.command() 
async def ping(ctx): 
    await ctx.send('Pong!') 

#Retrive bot token from env variables
token = os.getenv('TOKEN')

#Display event handler when the bot is ready
@client.event 
async def on_ready(): 
	print("Logged in as a bot {0.user}".format(client))
	print(f'Your EC2 Data are as follows: IP Address: {ip_address}, Region: {region}, Availability Zone: {availability_zone}')

#Event handler when a message is received
@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 

	print(f'Message {user_message} by {username} on {channel}') 

#Ignore message if it is from the bot
	if message.author == client.user: 
		return

#Create message its correlating response for "bottest" channel
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
		elif user_message.lower() == "tell me about my server!":
			await message.channel.send(f'Your EC2 Data are as follows: IP Address: {ip_address}, Region: {region}, Availability Zone: {availability_zone}')
	await client.process_commands(message)
client.run(token)



