import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
	print(f"{bot.user} is ready and online!")

bot.load_extension("extensions")

bot.run(os.getenv('DISCORD_TOKEN'))
