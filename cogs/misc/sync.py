from discord import app_commands
from discord.ext import commands
import discord


class SyncCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='sync', description='A command only the bot owner can use, refreshes slash command list')
    async def sync(self, interaction: discord.Interaction) -> None:
        if await self.bot.is_owner(interaction.user) is False:
            await interaction.response.send_message('You need to be the bot owner to use this command!', ephemeral=True)
            return
        
        await self.bot.tree.sync(guild=interaction.guild)
        await interaction.response.send_message('Guild commands synced!', ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SyncCommands(bot))