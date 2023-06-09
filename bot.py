import discord
import random
import requests
from discord.ext import commands
import os
    
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
async def oppars(ctx):
        # The path to the images
        image_folder = "male_kdrama_actors"

        # Get a random image from the folder
        # os.listdir(image_folder) returns a list of all the images under the folder
        image_file = random.choice(os.listdir(image_folder))

        # Construct the full path to the image
        # Combines the image_folder path with the image_file name, you can see the URL on Discord
        image_path = os.path.join(image_folder, image_file)

        # Send the image as a file attachment
        # Creates a file object from the image_path
        sent_message = await ctx.send(file=discord.File(image_path))
        await sent_message.add_reaction("❤️")

@client.command()
async def noonas(ctx):
        image_folder = "female_kdrama_actors"
        image_file = random.choice(os.listdir(image_folder))
        image_path = os.path.join(image_folder, image_file)
        sent_message = await ctx.send(file=discord.File(image_path))
        await sent_message.add_reaction("❤️")

client.run("")




