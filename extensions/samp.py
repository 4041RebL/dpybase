from discord.ext import commands

# had to create this dummy file cus git wont let me create empty directory

class samp(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
def setup(bot):
	bot.add_cog(samp(bot))
