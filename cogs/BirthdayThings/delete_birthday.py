from Utils.errors import BirthdayNotFoundError
from Utils.logger_config import logger
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
        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()
            user = list(cursor.execute('SELECT * FROM Birthdays WHERE DiscordID = ?', (interaction.user.id,)))
            
            try:
                if not user:
                    await interaction.response.send_message('You aren\'t in my database, can\'t delete what doesn\'t exist!', ephemeral = True)
                    raise BirthdayNotFoundError(interaction.user.name)
            
            except BirthdayNotFoundError as error:
                logger.error(error)
                return

            cursor.execute('DELETE FROM Birthdays WHERE DiscordID = ?', (interaction.user.id,))
            await interaction.response.send_message('Successfully struck your birthday from my database')


async def setup(bot: commands.Bot):
    await bot.add_cog(DeleteBirthday(bot))
