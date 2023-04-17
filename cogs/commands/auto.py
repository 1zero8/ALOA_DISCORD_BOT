import discord
from discord.ext import commands


class arwazauto(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  """Autoroles commands"""

  def help_custom(self):
    emoji = '<:Autorole:1096826045971320882>'
    label = "Autorole"
    description = ""
    return emoji, label, description

  @commands.group()
  async def __Autorole__(self, ctx: commands.Context):
    """`autorole bots add` , `autorole bots remove` , `autorole bots` , `autorole config` , `autorole humans add` , `autorole humans remove` , `autorole humans` , `autorole reset all` , `autorole reset bots` , `autorole reset humans` , `autorole reset` , `autorole`"""
