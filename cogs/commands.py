import discord
from discord.ext import commands
from discord import app_commands

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
    
    @app_commands.command(name="atdininghall", description="Sets your status to 'in the dining commons'")
    async def at_dining_hall(self, interaction: discord.Interaction):
        db = self.bot.get_cog("Database")
        db.set(interaction.user, True)
        await interaction.response.send_message(f"{interaction.user.mention} is in the dining commons")
    
    @app_commands.command(name="notatdininghall", description="Sets your status to 'not in the dining commons'")
    async def not_at_dining_hall(self, interaction: discord.Interaction):
        db = self.bot.get_cog("Database")
        db.set(interaction.user, False)
        await interaction.response.send_message(f"{interaction.user.mention} is no longer in the dining commons")
    


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))