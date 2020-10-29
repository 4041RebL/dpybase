from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
	print("The bot is ready!")

	bot.load_extension("on_boot.ext_load")

bot.run(os.environ.get("TOKEN"))
