from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
	bot.load_extension("on_boot.ext_load")

bot.run(os.environ.get("TOKEN"))
