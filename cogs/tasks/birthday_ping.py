from datetime import date, datetime, time
from discord.ext import commands
from discord.ext import tasks
from zoneinfo import ZoneInfo
import sqlite3
import json
import os


midnight = time.min.replace(tzinfo=ZoneInfo('UTC'))

class BirthdayPing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.db_path = os.getenv('DB_PATH')
        self.birthday_ping.start()
        self.bot = bot


    @tasks.loop(time = midnight)
    async def birthday_ping(self) -> None:
        current_date  = datetime.now(tz=ZoneInfo('UTC')).date().isoformat()
        with sqlite3.connect(self.db_path) as db:
            cursor = db.cursor()
            result: list[tuple[str, ...]] = list(cursor.execute('SELECT * FROM Birthdays'))
        
        dates = {}
        for info in result:
            month, day = map(int, info[1].split('-'))
            dates[info[0]] = date(date.today().year, month, day,).isoformat()

        
        positions = [index for index, value in enumerate(dates.values()) if value == current_date]
        if not positions:
            return
        
        birthday_message = 'Happy birthday'
        for position in positions:
            birthday_message += f' <@{list(dates.keys())[position]}>'

        with open('channels.json', 'r') as file:
            guilds: dict = json.load(file)

        for guild in guilds:
            for channel in guilds[guild]['Channels']:
                channel = await self.bot.fetch_channel(guilds[guild]['Channels'][channel])
                await channel.send(birthday_message)


    @birthday_ping.before_loop
    async def before_birthday_ping_loop(self) -> None:
        await self.bot.wait_until_ready()


async def setup(bot: commands.Bot):
    await bot.add_cog(BirthdayPing(bot))
