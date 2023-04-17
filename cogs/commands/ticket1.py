import discord
from discord.ext import commands
import json


class devansh16(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  """Ticket commands"""

  def help_custom(self):
    emoji = '<:ticket:1096823525333024819>'
    label = "Ticket"
    description = ""
    return emoji, label, description

  @commands.group()
  async def __Tickets__(self, ctx: commands.Context):
    """`sendpanel`"""
