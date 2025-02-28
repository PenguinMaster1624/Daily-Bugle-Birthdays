from Utils.logger_config import logger
from datetime import date, datetime
from discord import app_commands
from discord.ext import commands
import discord
import sqlite3
import os


class InsertBirthday(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.db_path = os.getenv('DB_PATH')
        self.bot = bot

    @app_commands.command(name='insert_birthday', description='Insert your birthday into the database')
    async def insert_birthday(self, interaction: discord.Interaction, month: int, day: int) -> None:
        try:
            date(year=datetime.now().year, month=month, day=day)
        
        except ValueError as error:
            logger.error(error)
            await interaction.response.send_message(error, ephemeral=True)
            return

        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()

            user = list(cursor.execute('SELECT * FROM Birthdays WHERE DiscordID = ?', (interaction.user.id,)))
            if user:
                await interaction.response.send_message('Your birthday already exists in the database. Use the `/update` command if you want to update it')
                return
            
            cursor.execute(f'INSERT INTO Birthdays(?,?,?)', (interaction.user.id, interaction.user.name, f'{month}-{day}'))


async def setup(bot: commands.Bot):
    await bot.add_cog(InsertBirthday(bot))
