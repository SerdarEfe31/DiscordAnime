import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def anime(ctx):
    sec=random.choice(["one piece","naruto","hxh","attack on titan","Bakugan","Bleach TYBW","Bleach","Chainsaw Man","Naruto Shipudden"])
    await ctx.send(f'anime önerisi: {sec}')

@bot.command()
async def favcharacter(ctx):
    sec=random.choice(["Luffy","Naruto","Denji","Reze","Aizen","Ywach","Ulquirra"])
    await ctx.send(f'Karakter Önerisi: {sec}')
@bot.command()
async def keslan(ctx):
    sec=random.choice(["Tamam Abi","Pardon Cano","Kusura Bakma Cano"])
    await ctx.send(f'Özür Dileme Seçeneği: {sec}')
@bot.command()
async def merhabacanonasilsin(ctx):
    sec=random.choice(["Çok Teşekkür Ederim Cano","Sen Nasilsin Cano","Sen Nasilsin İt Osuruğu"])
    await ctx.send(f'Ben İyiyim: {sec}')
import random

@bot.command()
async def engüçlükimanimeden(ctx):
    sec = random.choice(["Naruto", "Goku", "Saitama", "Osuruk Böceği Luffy"])
    
    if sec == "Osuruk Böceği Luffy":
        await ctx.send(f'Çok Kötü: {sec}')
    else:
        await ctx.send(f'Kesinlikle: {sec}')
    


bot.run("Don't Look At Here Copy Your Token To Here")
