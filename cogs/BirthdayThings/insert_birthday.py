from Utils.errors import UserExistsError
from Utils.logger_config import logger
from datetime import date, datetime
from discord import app_commands
from discord.ext import commands
import calendar
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
            try:
                if user:
                    raise UserExistsError(interaction.user.name)

            except UserExistsError as error:
                logger.error(error)
                await interaction.response.send_message(error, ephemeral=True)
                return

            cursor.execute('INSERT INTO Birthdays(DiscordID, birthday) VALUES (?, ?)', (interaction.user.id, f'{month}-{day}'))
        
        await interaction.response.send_message(f'Birthday successfully logged into database as {calendar.month_name[month]} {day}', ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(InsertBirthday(bot))
