from discord.ext import commands
from discord.utils import get
import discord

import random
import math
from datetime import datetime

from sqlalchemy import asc, desc
from sqlalchemy.exc import SQLAlchemyError

class OnMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.logger = self.bot.logger
        
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        
        self.logger.message(f"{message.author}({message.author.id}) sent a message in {message.channel}: \"{message.content}\"")
        
        if message.content.lower() == "hello":
            await message.reply("Hello!")

async def setup(bot: commands.Bot):
    await bot.add_cog(OnMessage(bot))