from discord.ext import commands
import os

class ext_load(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.load_cogs()

	def load_cogs(self):
		for path, subdirs, files in os.walk("extensions"):
			for name in files:
				if name.endswith(".py"):
					name = os.path.join(name)[:-3]
					path = os.path.join(path).replace("/", ".")
					cog = path + "." + name
					try:
						self.bot.load_extension(cog)
						print(cog + " was loaded!")
					except Exception as e:
						print(e)
				else:
					continue

def setup(bot):
	bot.add_cog(ext_load(bot))
