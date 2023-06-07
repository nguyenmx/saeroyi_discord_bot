import discord
import random
from discord.ext import commands
    
my_pickup_list = []

def read_file(file_name, list):
  # Open the file in read mode
  with open(file_name, "r", encoding="utf-8") as file:
    # Iterate over each line in the file
    for line in file:
        # Add each line into a list
        list.append(line)

def pick_random(list):
   random_element = random.choice(list)
   return random_element

read_file('pick_up_lines.txt', my_pickup_list)


client = commands.Bot(command_prefix = "=", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def rizz(ctx):
    await ctx.send(pick_random(my_pickup_list))

@client.command()
async def oppar(ctx):
    await ctx.author.send("ello!")


client.run("MTExMzIyMTQ1NjIxMDQzNjIyOQ.GbECHT.UmKj6u81DduwbE7d0erAOIv7ie0AnAIW8X-oJg")



