import discord
from discord.ext import commands


class devansh69(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  """Fun commands"""

  def help_custom(self):
    emoji = '<:Fun:1097039454599909456>'
    label = "Fun"
    description = ""
    return emoji, label, description

  @commands.group()
  async def __Fun__(self, ctx: commands.Context):
    """` tickle` , `kiss` , `hug` , `slap` , `pat` , `feed` , `pet` , `howgay` , `slots` , ` penis` , `meme` , `cat` , `iplookup`"""
