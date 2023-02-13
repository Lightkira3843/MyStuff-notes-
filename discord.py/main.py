import discord
from discord.ext import commands
from discord import app_commands
import time
from colorama import Back,Fore,Style
import random
import platform
import asyncio
import aiohttp
from discord import ui 
# from .cogs import Games

#---------------------------------------------------------------

# class PersistentViewBot(commands.Bot):
#     def __init__(self):
#         super().__init__(command_prefix=commands.when_mentioned_or('...'), intents=discord.Intents().all())
#     async def setup_hook(self) -> None:
#             self.add_view(Games.cf())
#             pass

# bot = PersistentViewBot()



#-----------------------------------------------------------------
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='...',intents=discord.Intents.all())

        self.extns = [
                    "cogs.Fun",
                    # "cogs.Games",
                    # "cogs.Mod",
                    # "cogs.Utilities"
                    ]

    async def setup_hook(self):
        for ext in self.extns:
            await self.load_extension(ext)
            print(f"{ext} cogs has loaded successfully ")

    async def on_ready(self):
        try:
            prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S GTM",time.gmtime())+ Back.RESET + Fore.WHITE + Style.BRIGHT)
            print( prfx + " Logged in as " + Fore.YELLOW + bot.user.name)
            print( prfx + " Bot ID " + Fore.YELLOW + str(bot.user.id))
            print( prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
            print( prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))
            syncd = await bot.tree.sync()
            print(prfx + " We have currently " + Fore.YELLOW + str(len(syncd)) + " Slash Commands ")
        except Exception as e:
            print(e)

#----------------------------------------------------------------

bot = MyBot()


@bot.tree.command(name='usrinfo',description="User_information")
async def usrinfo(inter: discord.Interaction,member:discord.Member=None):
    if member == None:
        member = inter.user
    roles = [ role for role in member.roles ]
    embed = discord.Embed(title="This is title ",description=f"hey name  {member.mention} id  guild type   this is description of this embed ",color=discord.Color.green())
    embed.set_thumbnail(url=member.avatar)
    embed.set_author(name=inter.guild.name,icon_url=inter.guild.icon)
    embed.add_field(name='this is User name ' ,value=  member.name ,inline=False)
    embed.add_field(name="this is User's id: " ,value=  member.id,inline=False)
    embed.add_field(name="this is User's guild's name: " ,value=  inter.guild , inline=False)
    embed.add_field(name="this is User's guild's id: " ,value=  inter.guild.id , inline=False)
    embed.add_field(name='this is type : ' ,value=  inter.type, inline=False) 
    embed.add_field(name='Status : ', value=  member.status, inline=False)
    embed.add_field(name='Top Roles : ', value= (member.top_role.mention), inline=False)  
    embed.add_field(name=f"Roles { {len(roles)} }: ", value= " ".join(role.mention for role in roles), inline=False)     
    # embed.add_field(name='total number of Roles : ', value= len(roles), inline=False)     
    embed.add_field(name='Created_at : ', value= (member.created_at).strftime("%a, %B %#d,%Y,%I:%M %p"), inline=False) 
    embed.add_field(name='Joined_at : ', value= (member.joined_at).strftime("%a, %B %#d,%Y,%I:%M %p"), inline=False) 

    await inter.response.send_message(embed=embed)


@bot.tree.command(name='srinfo',description="Server_information")
async def srinfo(inter: discord.Interaction):
    roles = [ role for role in inter.guild.roles ]
    embed = discord.Embed(title="This is title ",description=f"hey name  {inter.guild.name} id  guild type   this is description of this embed ",color=discord.Color.green())
    embed.set_thumbnail(url=inter.guild.icon)
    embed.set_author(name=inter.user.name,icon_url=inter.user.avatar)
    embed.add_field(name='this is Server name ' ,value=  inter.guild ,inline=False)
    embed.add_field(name='owner ' ,value=  f"{inter.guild.owner} owner_id = {inter.guild.owner_id} ",inline=False)
    embed.add_field(name="this is Server's id: " ,value=  inter.guild.id,inline=False)
    embed.add_field(name='this is type : ' ,value=  inter.type, inline=False) 
    embed.add_field(name='Active Threads : ', value=  inter.guild.active_threads, inline=False)
    embed.add_field(name='bans : ', value=  inter.guild.fetch_ban, inline=False)
    embed.add_field(name=f"Channels: ", value=  f"""total {len(inter.guild.channels)} = Text {len(inter.guild.text_channels)} |Voice {len(inter.guild.voice_channels)} """, inline=False)
    embed.add_field(name=f"Categories: ", value=  len(inter.guild.categories), inline=False)
    # embed.add_field(name='tot Roles : ', value= (inter.user.top_role.mention), inline=False)  
    embed.add_field(name=f"Roles { {len(roles)} }: ", value= " ".join(role.mention for role in roles), inline=False)     
    embed.add_field(name='total number of Roles : ', value= len(roles), inline=False)     
    embed.add_field(name='Here is the server description : ', value= inter.guild.description, inline=False)     
    embed.add_field(name='total number of members : ', value= inter.guild.member_count, inline=False)     
    embed.add_field(name='Created_at : ', value= (inter.guild.created_at).strftime("%a, %B %#d,%Y,%I:%M %p"), inline=False) 
    embed.add_field(name='today : ', value= time.strftime("%a, %B %#d,%Y,%I:%M %p",time.gmtime()), inline=False) 

    await inter.response.send_message(embed=embed)


@bot.tree.command(name="math",description="this is a claculator")
@app_commands.describe(exp = "Enter you Expression here ")
async def math(inter: discord.Interaction,exp: str):
    symbols = ['+','-','*','/','%']
    if  any(i in exp for i in symbols):
        try:
            result = eval(exp)
            await inter.response.send_message(result)
        except Exception as e:
            await inter.response.send_message('Invalid Input')
    else:
        await inter.response.send_message('Invalid Input')

@bot.tree.command(name='roll',description="roll the number ;)")
@app_commands.describe(min= "Enter the minimum number: ",max= "Enter the maximun number: ")
async def roll(inter : discord.Interaction,min:int=0 ,max:int=100):
    a = random.randint(min,max)
    await inter.response.send_message(a)



@bot.tree.command(name='chose',description="Enter somethings to choose ")
@app_commands.describe(choise = "Here Enter your Choises to chose  ")
async def chose(inter : discord.Interaction,choise:str):
    chis = choise.split(" ")
    c = random.choice(chis)

    thinking = await inter.channel.send(f":clock1: : Thingking... ")
    for i in range(4):
        await thinking.edit(content=f":clock{i+1}: : Thingking... ")
        await asyncio.sleep(0.2)

    await inter.response.send_message(f"this  has been chosen: {c}")


@bot.tree.command(name='guess',description='Number Gussing game :)')
@app_commands.describe(max = 'Enter the range ')
async def guess(inter : discord.Interaction,max:int=10):
    mx_gus = 999
    num = random.randint(1,max)
    await inter.response.send_message(f"Game is stared\n guess a number b/w 1 to {max} you have {mx_gus} gusses")
    def check(m):
        return m.author == inter.user and m.channel == inter.channel
    for i in range(mx_gus):
        guess = await bot.wait_for("message",check=check)
        try:
            int(guess.content)
            if guess.content == str(num):
                await inter.channel.send(f"you have guessed correctly \n and you took {i+1} gusses ")
                break
            elif guess.content >= str(num):
                await inter.channel.send(f"Lower ;) ")
            elif guess.content <= str(num):
                await inter.channel.send(f"Higher!  ") 
        except:
            await inter.channel.send(f"Invalid Input !")
            break
    else:
        await inter.channel.send(f"you have run out of gusses ")







class SelectMenu(discord.ui.Select):
    def __init__(slef):
        opts = [    discord.SelectOption(label="first option",description="1st this is description",emoji="😁"),
                    discord.SelectOption(label="second options",description="2st this is description"),
                    discord.SelectOption(label="3rd option",description="3st this is description"),
                    discord.SelectOption(label="4th option",description="4st this is description"),]
        super().__init__(placeholder="This is place holder ",options=opts,min_values=3,max_values=4)
    
    async def callback(self, interaction:discord.Integration):
        await interaction.response.send_message(content="Seccessfully done ")



class Select(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectMenu())

@bot.tree.command(name="select",description="first select menu")
async def select(inter : discord.Interaction):
    await inter.response.send_message(content="Here is your Select Menu",view=Select())



class verify(discord.ui.View):
    def __init__(self): 
        super().__init__(timeout=None)
    @discord.ui.button(label="Verify",style=discord.ButtonStyle.green,custom_id='1')
    async def buton1(self,interaction:discord.interactions,Buttion:discord.ui.Button):
        await interaction.response.send_modal(myModale())




class myModale(ui.Modal,title="this is title"):
    Name = ui.TextInput(label="Nmae: ",placeholder="My Name is ...",style=discord.TextStyle.short)
    Age = ui.TextInput(label="Age: ",placeholder="Age ?...",style=discord.TextStyle.short)
    About = ui.TextInput(label="About1: ",placeholder="I am ...",style=discord.TextStyle.long)
    About2 = ui.TextInput(label="About2: ",placeholder="...",style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        embed= discord.Embed(title="Verifcation " ,description="you muct veerify yourself ",color=discord.Color.green())
        embed.set_author(name=interaction.guild.name,url=interaction.guild.icon,icon_url=interaction.guild.icon)
        embed.set_thumbnail(url=interaction.user.avatar)
        embed.add_field(name="Name",value=f" {self.Name}",inline=False)
        embed.add_field(name="Age",value=f" {self.Age}",inline=False)
        embed.add_field(name="About1",value=f" {self.About}",inline=False)
        embed.add_field(name="About2",value=f" {self.About2}",inline=False)
        await interaction.response.send_message(embed=embed,ephemeral=True)



@bot.tree.command(name="verify",description="this is Verify...")
async def Verify(inter:discord.Interaction):
    embad= discord.Embed(title="Verifcation",description="you much verify yourself")
    embad.set_author(name=inter.guild.name,url=inter.guild.icon,icon_url=inter.guild.icon)
    embad.set_thumbnail(url=inter.user.avatar)
    embad.add_field(name="information",value="click below to verify yourself",inline=True)
    await inter.response.send_message(embed=embad,view=verify())





@bot.tree.command(name="chatgpt",description="Ask Anything?")
async def gpt(inter:discord.Interaction,quest:str):
    Api_key="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"
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-davinci-003",
            "prompt" : quest,
            "temperature" : 0.9,
            "max_tokens" : 50,
            "presence_penalty": 0,
            "frequency_penalty":0,
            "best_of":1,
        }
        headers = {"Authorization": f"""Bearer {Api_key}"""}
        async with session.post("https://api.openai.com/v1/completions",json=payload,headers=headers) as resp:
            response = await resp.json()
            embed = discord.Embed(title="ChatGPT Responce",description=response["choices"][0]["text"])
            await inter.response.send_message(embed=embed)






















# @app_commands.command(name="mindtst",description="this is a claculator")
# @app_commands.describe(rng = "Enter you Expression here ",exp=" + , - , * , / : ")
# async def mindtst(inter: discord.Interaction,rng:int,exp:str):
#     a = random.randint(1,rng)
#     b = random.randint(1,rng)
#     c = [a*b,a+b,a-b,a/b]
#     if exp == '+':
#         await inter.response.send_message(f'{a}+{b} = ?')
#         def check(m):
#             return m.author == inter.user and m.channel == inter.channel

#         ans = await bot.wait_for("message",check=check)
#         if c == ans:
#             await inter.channel.send(f'Congo r u ri8 {a}+{b} = {c[1]}')
#         else:
#             await inter.channel.send(f'you are wrong :( right ans is {c[1]}')

#     if exp == '-':
#         await inter.response.send_message(f'{a}+{b} = ?')
#         def check(m):
#             return m.author == inter.user and m.channel == inter.channel

#         ans = await bot.wait_for("message",check=check)
#         if c == ans:
#             await inter.channel.send(f'Congo r u ri8 {a}-{b} = {c[2]}')
#         else:
#             await inter.channel.send(f'you are wrong :( right ans is {c[2]}')

#     if exp == '*':
#         await inter.response.send_message(f'{a}*{b} = ?')
#         def check(m):
#             return m.author == inter.user and m.channel == inter.channel

#         ans = await bot.wait_for("message",check=check)
#         if c == ans:
#             await inter.channel.send(f'Congo r u ri8 {a}*{b} = {c[0]}')
#         else:
#             await inter.channel.send(f'you are wrong :( right ans is {c[0]}')

#     if exp == '/':
#         await inter.response.send_message(f'{a}+{b} = ?')
#         def check(m):
#             return m.author == inter.user and m.channel == inter.channel

#         ans = await bot.wait_for("message",check=check)
#         if c == ans:
#             await inter.channel.send(f'Congo r u ri8 {a}/{b} = {c[3]}')
#         else:
#             await inter.channel.send(f'you are wrong :( right ans is {c[3]}')

#     else:
#         await inter.response.send_message('Invalid Input ')








TOKEN="MTA1NjkzNjI3MjgzODUyOTE0NA.G0obt_.tTa2yKkEIgBLOgDYtTpB-Vas-01P-tQHDHHxAY"



# app_commands.bot = bot
# bot.tree = app_commands.tree()

bot.run(TOKEN,reconnect=True)


# class start(discord.Client):
#     def __init__(self):
#         super().__init__(intents=discord.Intents.all())
#         self.synced = False

#     async def on_ready(self):
#         await tree.synced(guild=discord.object(id=discord.Intents.))