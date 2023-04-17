import discord
from discord.ext import commands


class devansh4(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Owner commands"""
  
    def help_custom(self):
		      emoji = '<:owner:1096823121065021520>'
		      label = "Owner"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Owner__(self, ctx: commands.Context):
        """`eval` , `slist` , `restart` , `sync` , `np` , `np add` , `np remove` , `np list` , `bl show` , `bl add` , `bl remove` , `bdg` , `bdg add` , `bdg remove` , `dm` , `nick` , `globalban`"""