import discord
from discord.ext import commands

class Database(commands.Cog):
    def __init__(self):
        super().__init__()
        self.store = {}
    
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

async def setup(bot: commands.Bot):
    await bot.add_cog(Database())