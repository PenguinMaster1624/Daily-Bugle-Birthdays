from Utils.errors import BirthdayNotFoundError 
from discord import app_commands
from discord.ext import commands
from tzdata import zoneinfo
import discord
import sqlite3
import os


class UpdateBirthday(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.db_path = os.getenv('DB_PATH')
        self.bot = bot

    @app_commands.command(name='update_birthday', description='Update your birthday in the database')
    async def update_birthday(self, interaction: discord.Interaction, month: int, day: int) -> None:
        pass


async def setup(bot: commands.Bot):
    await bot.add_cog(UpdateBirthday(bot))
