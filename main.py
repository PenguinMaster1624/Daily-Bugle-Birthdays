from Utils.PackageChecker import package_check
from Utils.errors import OutdatedPackageError
from Utils.logger_config import logger
from discord.ext import commands
import discord
import os




class BirthdayBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        activity = discord.Activity(name="/help", type=discord.ActivityType.listening)
        super().__init__(command_prefix='BirthdayBot.', help_command=None, intents=intents, activity=activity)

    async def setup_hook(self) -> None:
        for folder in os.listdir('./cogs'):
            for file in os.listdir('./cogs/' + folder):
                if file.endswith('.py'):
                    await self.load_extension(f'cogs.{folder}.{file[:-3]}')

        await self.tree.sync()

    async def on_ready(self) -> None:
        try:
            await package_check()
            print('Pybot at your service')

        except OutdatedPackageError as error:
            logger.warning(error)

if __name__ == '__main__':
    Bot = BirthdayBot()
    Bot.run(token=os.getenv('BOT'), log_handler=None)
