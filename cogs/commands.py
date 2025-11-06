import discord
from datetime import datetime
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
        await interaction.response.send_message(f"updated status", ephemeral=True)
    
    @app_commands.command(name="notatdininghall", description="Sets your status to 'not in the dining commons'")
    async def not_at_dining_hall(self, interaction: discord.Interaction):
        db = self.bot.get_cog("Database")
        db.set(interaction.user, False)
        await interaction.response.send_message(f"updated status", ephemeral=True)
    
    @app_commands.command(name="currentdiners", description="Gets everyone who is at the dining hall")
    async def current_diners(self, interaction: discord.Interaction):
        e = discord.Embed(color=discord.Colour.blue(), title="Current Diners at the Dining Commons", timestamp=datetime.now())
        db = self.bot.get_cog("Database")
        diners = db.get_all_diners()

        if len(diners) == 0:
            e.description = "Hmm no one seems to be in the dining commons"
        else:
            for diner in diners:
                user = await self.bot.fetch_user(diner)
                e.add_field(name="", value=f"{user.mention} is currently dining", inline=False)
        
        await interaction.response.send_message(embed=e)
    


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
