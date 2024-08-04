import discord
from discord.ext import commands
import aykutelmas

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f"Selam {ctx.author}. Ben {bot.user}")
@bot.command()
async def Hallo(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya .save (f"resim/{dosya.filename}")
            await ctx.send (f"Resim gönderdik") 
        sinif,score=aykutelmas.aykut(f"resim/{dosya.filename}") 
        if sinif == "kraga\n":
            await ctx.send(f"bu bir tane kraga dır ve bu bir kraga ")
        
        elif sinif =="seceler\n":
            await ctx.send(f"bu bir sercele dir ")

        elif sinif =="guvercin\n":
            await ctx.send(f"bu bir güvencin dir ")    
    else:
         await ctx.send(f"Daha göndermeyi mi bilmiyorsun git gönder")         
bot.run("MTIwNjE3Njc1MTM0MTAxNTA3MQ.Gif75d.8u6A7zBZnZbwkKLHUKr8hzXZaTNWyWE9Y3nKrg")