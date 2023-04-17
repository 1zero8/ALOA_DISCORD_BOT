import discord
from discord.ext import commands
import asyncio
from discord.ext.commands.errors import CommandInvokeError
import random
import datetime
import time

alias = {
  "s": 1,
  "m": 60,
  "h": 3600,
  "d": 86400,
}


class Giveaways(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  def convert(self, time):
    unit = time[-1]
    if unit not in alias.keys():
      return -1
    try:
      val = int(time[:-1])
    except:
      return -2
    return val * alias[unit]

  @commands.command(name="giveaway", aliases=["gway", " gw"])
  @commands.cooldown(1, 7, commands.BucketType.user)
  async def _giveaway(self, ctx):
    """
        Shows the giveaway commands
        It shows how to use giveaway commands
        """
    em = discord.Embed(title="Giveaway Commands", color=0x2f3136)
    em.add_field(name="!gstart <time> <winners> <message/prize>",
                 value="Starts a giveaway for the specified amount of time.",
                 inline=False)
    em.add_field(name="!greroll <message_id>",
                 value="Re rolls the winners of the giveaway.",
                 inline=False)
    em.add_field(name="!gend <message_id>",
                 value="Ends the specified giveaway",
                 inline=False)
    await ctx.send(embed=em)

  @commands.command(name="gstart", aliases=["giveawaystart", "gcreate"])
  @commands.cooldown(1, 7, commands.BucketType.user)
  async def _gstart(self, ctx, timee: str, winners: str, *, message):
    """
        Starts the giveaway
        """
    winners = winners.replace("w", " ")
    winners = int(winners)
    time = self.convert(timee)
    if time == -1:
      raise CommandInvokeError('Time enterd incorrectly must be s|m|h|d')
    elif time == -2:
      raise CommandInvokeError('Time should be int')
    em = discord.Embed(
      title=f' {message}',
      description=
      f" <a:dot:1085205573999534161>React with <a:Giveaway:1062597766599151667> to enter\n <a:dot:1085205573999534161>Time: **{timee}**\n <a:dot:1085205573999534161>Hosted by: {ctx.author.mention}\n\n<a:dot:1085205573999534161>[Invite Me]()  [Aloa](https://discord.com/api/oauth2/authorize?client_id=1081937388814745650&permissions=8&scope=bot%20applications.commands)",
      color=0x2f3136)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
    em.set_footer(text=f"{winners} Winners | Ends at • {end}")
    #if requirement.lower() != "none":
    #  role = discord.utils.get(ctx.guild.roles,id=int(requirement))
    #else:
    # role = None

    msg = await ctx.send(
      "<:giveawayy:1085523984092774410>    **GIVEAWAY STARTED**    <:giveawayy:1085523984092774410>",
      embed=em)
    print(msg)
    gchannel = ctx.channel
    await msg.add_reaction("<a:Giveaway:1062597766599151667>")
    await asyncio.sleep(time)
    cache_msg = await gchannel.fetch_message(msg.id)
    if "ended" not in cache_msg.content.lower():
      await self.gend(msg, em, winners, message, gchannel, end)

  async def gend(self, msg, em, winners, message, gchannel, end):
    cache_msg = await gchannel.fetch_message(msg.id)
    if cache_msg.author.id != self.bot.user.id:
      return await gchannel.send("Invalid Message ID.")
    for reaction in cache_msg.reactions:
      if str(reaction.emoji) == "<a:Giveaway:1062597766599151667>":
        users = await reaction.users().flatten()
        print(reaction.users())
        if len(users) == 1:
          await msg.edit(
            content=
            "<:giveawayy:1085523984092774410>   **GIVEAWAY ENDED**    <:giveawayy:1085523984092774410>"
          )
          return await gchannel.send(
            f"Nobody has won the giveaway for : **{message}**")

    try:
      winners2 = random.sample([user for user in users if not user.bot],
                               k=winners)
    except ValueError:
      em.add_field(name="Winners", value="Not enough participants")
      em.description += "\n**Winners:** "
      em.set_footer(text=f"{winners} Winners | Ended at • {end}")
      await msg.edit(
        content=
        "<:giveawayy:1085523984092774410>    **GIVEAWAY ENDED**    <:giveawayy:1085523984092774410>"
      )
      await msg.edit(embed=em)
      return await gchannel.send("Not enough participants")
    else:
      y = ", ".join(winner.mention for winner in winners2)
      x = ", ".join(winner.mention for winner in winners2)
      x += f"** has won the giveaway for: `{message}`**"
      em.add_field(name="Winners", value=f"{y}")
      em.description += f"\n**Winners: ** {y}"
      em.set_footer(text=f"{winners} Winners | Ended at • {end}")
      em.color = 0x2f3136

      await msg.edit(embed=em)
      await msg.edit(
        content=
        "<:giveawayy:1085523984092774410>   **GIVEAWAY ENDED**    <:giveawayy:1085523984092774410>"
      )
      await gchannel.send(x)

  @commands.command(name="reroll", aliases=["re", "greroll"])
  @commands.cooldown(1, 7, commands.BucketType.user)
  async def _reroll(self, ctx, msg_id):
    """
        Get new winners for the giveaway
        Rerolls the winners again to choose new winners
        """
    reroll = await ctx.fetch_message(msg_id)
    if reroll.author.id != self.bot.user.id:
      return await ctx.send("Invalid Message ID.")
    em = reroll.embeds[0]
    message = em.title
    for reaction in reroll.reactions:
      if str(reaction.emoji) == "<a:Giveaway:1062597766599151667>":
        users = await reaction.users().flatten()
        #print(reaction.users())
        if len(users) == 1:
          await reroll.edit(
            content=
            "<:giveawayy:1085523984092774410>    **GIVEAWAY ENDED**    <:giveawayy:1085523984092774410>"
          )
          return await ctx.send(
            f"Nobody has won the giveaway for : **{message}**")
    em = reroll.embeds[0]
    message = em.title
    winners = em.footer.text[0]
    winners = int(winners)
    users = await reroll.reactions[0].users().flatten()
    users.pop(users.index(self.bot.user))
    winners2 = random.sample([user for user in users if not user.bot],
                             k=winners)
    y = ", ".join(winner.mention for winner in winners2)
    em.set_field_at(0, name="Winners", value=f"{y}")
    await reroll.edit(embed=em)
    await ctx.send(f"**The new winner for `{message}` is/are:** {y}")

  @commands.command(name="gend", aliases=["giveawayend", "end"])
  @commands.cooldown(1, 7, commands.BucketType.user)
  async def _end(self, ctx, msg_id):
    """
        Ends the giveaway before time
        """
    msg = await ctx.fetch_message(msg_id)
    if msg.author.id != self.bot.user.id:
      return await ctx.send("Invalid Message ID.")
    if "ended" in msg.content.lower():
      return await ctx.send(
        "That giveaway already ended. You can reroll using: `>reroll`")
    else:
      em = msg.embeds[0]
      winners = em.footer.text[0]
      winners = int(winners)
      message = em.title
      gchannel = ctx.channel
      x = em.description.split("\n")
      x = x[1]
      x = x.split(":")
      x = x[1]
      x = x.replace("*", "")
      time = self.convert(x)
      end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
      end = datetime.datetime.strftime(end, "%d %b %Y %I:%M %p")
      await self.gend(msg, em, winners, message, gchannel, end)


#def setup(bot):
##bot.add_cog(Giveaways(bot))
