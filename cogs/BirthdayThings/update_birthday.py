from Utils.errors import UserNotFoundError
from Utils.logger_config import logger
from datetime import datetime, date
from discord import app_commands
from discord.ext import commands
import discord
import sqlite3
import os


class UpdateBirthday(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.db_path = os.getenv('DB_PATH')
        self.bot = bot

    @app_commands.command(name='update_birthday', description='Update your birthday in the database')
    async def update_birthday(self, interaction: discord.Interaction, month: int, day: int) -> None:
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
                if not user:
                    raise UserNotFoundError(interaction.user.name)
            
            except UserNotFoundError as error:
                logger.error(error)
                await interaction.response.send_message(error, ephemeral=True)

            cursor.execute('UPDATE Birthdays SET birthday = ? WHERE DiscordID = ?', (f'{month}-{day}', interaction.user.id))

        await interaction.response.send_message('Birthday successfully changed')

async def setup(bot: commands.Bot):
    await bot.add_cog(UpdateBirthday(bot))
