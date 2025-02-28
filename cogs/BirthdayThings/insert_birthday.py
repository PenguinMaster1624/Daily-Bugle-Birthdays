from discord import app_commands
from discord.ext import commands
from tzdata import zoneinfo
import discord
import sqlite3
import os

class InsertBirthday(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.db_path = os.getenv('DB_PATH')
        self.bot = bot

    @app_commands.command(name='insert_birthday', description='Insert your birthday into the database')
    async def insert_birthday(self, interaction: discord.Interaction, month: int, day: int) -> None:
        pass


async def setup(bot: commands.Bot):
    await bot.add_cog(InsertBirthday(bot))
