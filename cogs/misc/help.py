from discord import app_commands
from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='help', description='Shows what other commands I have')
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title='Birthday Bot Commands', description='So I\'m a bot related to birthdays. These are the commands I have, and there is a plan that I\'d ping people as it strikes midnight on their birthday.', color=discord.Color.orange())
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)
        embed.add_field(name='`/insert_birthday <month_num> <day_num>`', value='You can insert your birthday into the database for future pinging on it.', inline=True)
        embed.add_field(name='`/update_birthday <month_num> <day_num>`', value='Use this in case you accidentally put in the wrong birthday. It circumvents having to delete it and put it back in.', inline=True)
        embed.add_field(name='`/delete_birthday <month_num> <day_num>`', value='In case you just don\'t want your birthday in the database anymore. Not much else to it.', inline=True)
        embed.add_field(name='`/help`', value='Displays this. There *might* be more at a later date but it\'s unlikely.', inline=True)
        embed.set_footer(text='I am still a work in progress')

        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))
