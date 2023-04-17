import discord
from discord.ext import commands


class arwazgiveaway(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  """Giveaways commands"""

  def help_custom(self):
    emoji = '<:giveaway:1096824279850569869>'
    label = "Giveaways"
    description = ""
    return emoji, label, description

  @commands.group()
  async def __Giveaway__(self, ctx: commands.Context):
    """`gstart` , `greroll` , `gend`"""
