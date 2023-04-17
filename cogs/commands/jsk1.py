import discord
from discord.ext import commands
import json


class devansh13(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  """Jsk commands"""

  def help_custom(self):
    emoji = '<:jsk:1058764209887924386>'
    label = "Jsk"
    description = ""
    return emoji, label, description

  @commands.group()
  async def __Jsk__(self, ctx: commands.Context):
    """`jsk` , `jsk rtt` , `jsk curl` , `jsk debug` , `jsk sync` , `jsk py` , `jsk permtrace` , `jsk retain` , `jsk tasks` , `jsk timeit` , `jsk dis` , `jsk sql` , `jsk py_inspect` , `jsk hide` , `jsk voice` , `jsk git` , `jsk show` , `jsk cancel` , `jsk shell` , `jsk load` , `jsk unload` , `jsk invite` , `jsk shutdown` , `jsk pip` , `jsk repeat`"""
