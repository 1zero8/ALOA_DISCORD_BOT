import discord
from discord.ext import commands


class shree1227(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Raidmode commands"""
  
    def help_custom(self):
		      emoji = '<:automod:1096824098962817316>'
		      label = "Automod"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Automod__(self, ctx: commands.Context):
        """`automod` , `antispam on` , `antispam off` , `antilink off` ,  `antilink on`"""