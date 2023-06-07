import discord
import random
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
    
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

# Scraping an image from Pinterest :clown: 
def scrape_images(query):
   search_url = 'https://www.pinterest.com/search/pins/?q={}'.format(query.replace(" ", "%20"))
   response = requests.get(search_url)
   scrape_web = BeautifulSoup(response.text, 'html.parser')
   image_divs = scrape_web.find_all('div', {'class': 'GrowthUnauthPinImage'})
   image_urls = [div.find('img')['src'] for div in image_divs]
   random_image_url = random.choice(image_urls) if image_urls else None
   return random_image_url


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
    image_query = "cute"  # Replace with the desired image search query
    image_url = scrape_images(image_query)
    if image_url:
        await ctx.send(image_url)
    else:
        await ctx.send("No image found.")
    

client.run("MTExMzIyMTQ1NjIxMDQzNjIyOQ.Gq5eN_._DMltRP5DHjh0VuKcVFtu0jH457iWLhBF16NpQ")



