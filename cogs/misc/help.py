from discord import app_commands
from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='help', description='Shows what other commands I have')
    async def help(self, interaction: discord.Interaction) -> None:
        pass


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))
