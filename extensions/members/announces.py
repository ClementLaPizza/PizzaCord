# extensions/members/announces.py

import discord
from discord.ext import commands

class MembersAnnounces(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		print(f"{member.name} rejoint le serveur")

	@commands.Cog.listener()
	async def on_member_leave(self, member):
		print(f"{member.name} quitte le serveur")

def setup(bot):
	bot.add_cog(MembersAnnounces(bot))
