import discord
from datetime import datetime
from discord.ext import commands
from discord import app_commands

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
        
    
    @app_commands.command(name="atdc", description="Sets your status to 'in the dining commons'")
    async def at_dining_hall(self, interaction: discord.Interaction, locked_in: bool = False):
        db = self.bot.get_cog("Database")
        db.set(interaction.user, locked_in)
        await interaction.response.send_message(f"updated status", ephemeral=True)
    
    @app_commands.command(name="notatdc", description="Sets your status to 'not in the dining commons'")
    async def not_at_dining_hall(self, interaction: discord.Interaction):
        db = self.bot.get_cog("Database")
        db.remove(interaction.user)
        await interaction.response.send_message(f"updated status", ephemeral=True)
    
    @app_commands.command(name="dc", description="Gets everyone who is at the dining hall")
    async def current_diners(self, interaction: discord.Interaction):
        e = discord.Embed(color=discord.Colour.blue(), title="Current Diners at the Dining Commons", timestamp=datetime.now())
        db = self.bot.get_cog("Database")
        diners = db.get_all_diners()

        if len(diners) == 0:
            e.description = "Hmm no one seems to be in the dining commons"
        else:
            for diner_info in diners:
                user = await self.bot.fetch_user(diner_info[0])
                if diner_info[1]["lockedIn"]:
                    e.add_field(name="", value=f"{user.mention} is currently dining but is locked in", inline=False)
                else:
                    e.add_field(name="", value=f"{user.mention} is currently dining", inline=False)
        
        await interaction.response.send_message(embed=e)
    


async def setup(bot: commands.Bot):
    await bot.add_cog(Commands(bot))
