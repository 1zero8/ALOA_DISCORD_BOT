import discord
from discord.ext import commands


class devansh00(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """VoiceRoles commands"""
  
    def help_custom(self):
		      emoji = '<:vc:1096825104446533763>'
		      label = "VcRoles"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __VcRoles__(self, ctx: commands.Context):
        """`vcrole bots add` , `vcrole bots remove` , `vcrole bots` , `vcrole config` , `vcrole humans add` , `vcrole humans remove` , `vcrole humans` , `vcrole reset` , `vcrole`"""