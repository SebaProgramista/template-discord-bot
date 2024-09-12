from discord.ext import commands
import discord

from dotenv import load_dotenv
import os
import json

from config import Config
from utils.database_manager import SessionManager

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
    
    async def setup_hook(self):
        for i in os.listdir("cogs"):
            if i.endswith(".py"):
                await self.load_extension(f'cogs.{i[:-3]}')

        await self.tree.sync()

    async def on_ready(self):
        print("Bot was started")

bot = Bot()

# Set emojis
bot.CHANNEL = Config.get("CHANNEL", "EMOJIS")

bot.run(Config.get("BOT_TOKEN"))
