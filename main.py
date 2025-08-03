import discord
from discord.ext import commands
from dotenv import load_dotenv
import os



load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents = intents)

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am Muhittin!")

@client.command()
async def whatsup(ctx):
    await ctx.send("I am good, whatsupp to you?")


client.run(TOKEN)

