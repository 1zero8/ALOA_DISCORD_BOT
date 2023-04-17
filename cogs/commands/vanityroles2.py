import discord
from discord.ext import commands


class arwazvr(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  """Vanityroles commands"""

  def help_custom(self):
    emoji = '<:vanity:1096823683537977354>'
    label = "Vanityroles"
    description = ""
    return emoji, label, description

  @commands.group()
  async def __Vanityroles__(self, ctx: commands.Context):
    """`vanityroles setup` , `vanityroles show` , `vanityroles reset`
"""