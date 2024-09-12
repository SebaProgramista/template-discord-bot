from discord.ext import commands
from discord import app_commands
from discord.utils import get
from discord.ui import View, Button
import discord

from config import Config

from datetime import datetime

class ConfigGroup(app_commands.Group):
    def __init__(self, bot: commands.Bot):
        super().__init__(name="config")
        self.bot = bot
    
    @app_commands.command(name="delay", description="set xp gain delay")
    async def delay(self, interaction: discord.Interaction, value: int):
        embed = discord.Embed(description=f"**{self.bot.CHANNEL} Are you sure you want to change the delay from `{Config.get('DELAY', 'SERVER_CONFIG')}` to `{value}`?**")
        embed.set_author(name="Changing delay")

        btn_confirm = Button(
            label="Confirm", emoji="✔️")
        btn_cancel = Button(
            label="Cancel", emoji="✖️")
        
        # Callback function for the confirm button
        async def btn_confirm_callback(interaction: discord.Interaction):
            embed = discord.Embed(description=f"**{self.bot.CHANNEL} Successful changing delay from to from `{Config.get('DELAY', 'SERVER_CONFIG')}` to `{value}`**", color=discord.Color.from_rgb(86, 191, 102))
            embed.set_author(name="Changing delay")

            Config.set("DELAY", value, "SERVER_CONFIG")

            await interaction.response.edit_message(embed=embed, view=None)
            return

        # Callback function for the cancel button
        async def btn_cancel_callback(interaction: discord.Interaction):
            embed = discord.Embed(description=f"**{self.bot.CHANNEL} Canceled changing delay!**", color=discord.Color.from_rgb(191, 86, 86))
            embed.set_author(name="Changing delay")

            await interaction.response.edit_message(embed=embed, view=None)
            return
        
        btn_confirm.callback = btn_confirm_callback
        btn_cancel.callback = btn_cancel_callback

        view = View()
        view.add_item(btn_confirm)
        view.add_item(btn_cancel)

        await interaction.response.send_message(embed=embed, view=view)

    @app_commands.command(name="xp", description="set xp gain")
    async def xp(self, interaction: discord.Interaction, min_value: int, max_value: int):
        embed = discord.Embed(description=f"**{self.bot.CHANNEL} Are you sure you want to change the xp gains from `{Config.get('XP_GAIN_MIN', 'SERVER_CONFIG')}-{Config.get('XP_GAIN_MAX', 'SERVER_CONFIG')}` to `{min_value}-{max_value}`?**")
        embed.set_author(name="Changing xp gains")

        btn_confirm = Button(
            label="Confirm", emoji="✔️")
        btn_cancel = Button(
            label="Cancel", emoji="✖️")
        
        # Callback function for the confirm button
        async def btn_confirm_callback(interaction: discord.Interaction):
            embed = discord.Embed(description=f"**{self.bot.CHANNEL} Successful changing xp gains from `{Config.get('XP_GAIN_MIN', 'SERVER_CONFIG')}-{Config.get('XP_GAIN_MAX', 'SERVER_CONFIG')}` to `{min_value}-{max_value}`**", color=discord.Color.from_rgb(86, 191, 102))
            embed.set_author(name="Changing xp gains")

            Config.set("XP_GAIN_MIN", min_value, "SERVER_CONFIG")
            Config.set("XP_GAIN_MAX", max_value, "SERVER_CONFIG")

            await interaction.response.edit_message(embed=embed, view=None)
            return

        # Callback function for the cancel button
        async def btn_cancel_callback(interaction: discord.Interaction):
            embed = discord.Embed(description=f"**{self.bot.CHANNEL} Canceled changing xp gains!**", color=discord.Color.from_rgb(191, 86, 86))
            embed.set_author(name="Changing xp gains")

            await interaction.response.edit_message(embed=embed, view=None)
            return
        
        btn_confirm.callback = btn_confirm_callback
        btn_cancel.callback = btn_cancel_callback

        view = View()
        view.add_item(btn_confirm)
        view.add_item(btn_cancel)

        await interaction.response.send_message(embed=embed, view=view)

async def setup(bot: commands.Bot):
    bot.tree.add_command(ConfigGroup(bot))