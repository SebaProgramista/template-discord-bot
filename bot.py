from discord.ext import commands
import discord

from dotenv import load_dotenv
import os
import json

from config import Config
from utils.database_manager import SessionManager
from utils.logger_manager import LoggerManager

logger_manager = LoggerManager(Config.get("DEBUG_MODE"))
logger = logger_manager.logger

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
    
    async def setup_hook(self):
        for i in os.listdir("cogs"):
            if i.endswith(".py"):
                await self.load_extension(f'cogs.{i[:-3]}')
                logger.info(f"Loaded {i[:-3]} cog")

        await self.tree.sync()

    async def on_ready(self):
        for guild in self.guilds:
            logger.info(f"Connected to {guild.name}")

bot = Bot()

# Set emojis
bot.CHANNEL = Config.get("CHANNEL", "EMOJIS")

bot.run(Config.get("BOT_TOKEN"))
