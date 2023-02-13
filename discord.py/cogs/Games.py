import discord
from discord.ext import commands
from discord import app_commands
import time
import random
import platform
import asyncio
from discord import ui 

class Games(commands.Cog):
    def __init__(self,bot: commands.Bot):
        self.bot = bot




async def head_tail(interactions,choises):
    c = random.choice(['head','tail'])
    if c == choises:
        await interactions.response.send_message(f"its {c} and you won !!")
    elif c != choises:
        await interactions.response.send_message(f"it's {c} and you lose :( ")


class cf(discord.ui.View):
    def __init__(self): 
        super().__init__(timeout=None)
    @discord.ui.button(label="Head",style=discord.ButtonStyle.green,custom_id='1')
    async def buton1(self,interaction:discord.interactions,Buttion:discord.ui.Button):
        await head_tail(interaction,"head")
    @discord.ui.button(label="Tail",style=discord.ButtonStyle.green,custom_id='2')
    async def buton2(self,interaction:discord.interactions,Buttion:discord.ui.Button):
        await head_tail(interaction,"tail")




@app_commands.command(name='coinflip')
# @app_commands.choices(choises=[app_commands.Choice(name='Head',value='Head'),app_commands.Choice(name='Tail',value='Tail')])
async def coinflip(inter : discord.Interaction):
    await inter.response.send_message("HEAD or TAIL ? ",view=cf())




async def setup(bot:commands.Bot) ->None:
	await bot.add_cog(Games(bot))
	print("mod cog is loaded!!")

