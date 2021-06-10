import discord, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(Notice(bot))

class Notice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_color = 0x75B8FF

    @commands.command(name="notice")
    async def notice(self, ctx, text_message):
        embed = discord.Embed(title=":satellite: Notice!", description=text_message, color=self.embed_color)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)