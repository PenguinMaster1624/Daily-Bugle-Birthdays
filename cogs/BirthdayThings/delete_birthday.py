from Utils.errors import BirthdayNotFoundError
from discord import app_commands
from discord.ext import commands
import discord
import sqlite3
import os


class DeleteBirthday(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.db_path = os.getenv('DB_PATH')
        self.bot = bot

    @app_commands.command(name='delete_birthday', description='Strike your birthday from the database')
    async def delete_birthday(self, interaction: discord.Interaction) -> None:
        pass


async def setup(bot: commands.Bot):
    await bot.add_cog(DeleteBirthday(bot))
