import discord
from discord.ext import commands
from discord.ext import tasks

class Database(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
        self.store = {}
        self.clear_diners.start()
    
    def set(self, user: discord.User, in_dining_commons: bool):
        self.store[user.id] = in_dining_commons
    
    def get(self, user: discord.User) -> bool:
        return self.store[user.id]

    def get_all_diners(self) -> list[int]:
        result = []
        for user, dining in self.store.items():
            if dining:
                result.append(user)
        return result
    @tasks.loop(hours=3)
    async def clear_diners(self):
        """Clear the current diners after three hours to maintain accuracy"""
        self.store = {}

    
async def setup(bot: commands.Bot):
    await bot.add_cog(Database(bot))