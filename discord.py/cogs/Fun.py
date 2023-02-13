import discord
from discord.ext import commands
from discord import app_commands
import time
import random
import platform
import asyncio
from discord import ui 


class Fun(commands.Cog):
    def __init__(self,bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name="fun",description="here is the description")
    async def fun(self,interaction: discord.Interaction):
        await interaction.response.send_message(content="hello")


async def setup(bot) -> None:
    await bot.add_cog(Fun(bot))
