import discord
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime

class Database(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot
        self.store = {}
        self.clear_diners.start()
    
    def set(self, user: discord.User, locked_in: bool):
        self.store[user.id] = {
            "timestamp": datetime.now(),
            "lockedIn": locked_in
        }
    
    def get(self, user: discord.User) -> bool:
        return self.store[user.id]

    def remove(self, user: discord.User):
        del self.store[user.id]

    def get_all_diners(self) -> list[int]:
        result = []
        for user, info in self.store.items():
                result.append((user, info))
        return result
    @tasks.loop(seconds=30)
    async def clear_diners(self):
        """Clear the current diners after 90 mins to maintain accuracy"""
        print("clearing diners")
        for key in self.store.keys():
            user_entered_dc = self.store[key]["timestamp"]
            locked_in = self.store[key]["timestamp"]
            if not locked_in:
                if (datetime.now() - user_entered_dc).total_seconds() > 90 * 60: # 90 mins
                    del self.store[key]
            else:
                if (datetime.now() - user_entered_dc).total_seconds() > 6 * 60 * 60: # 6 hours
                    del self.store[key]

    
async def setup(bot: commands.Bot):
    await bot.add_cog(Database(bot))