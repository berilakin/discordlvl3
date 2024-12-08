
import discord
from discord.ext import commands
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def about(ctx):
    await ctx.send('Bu discord.py kütüphanesi ile oluşturulmuş echo-bot!')
    await ctx.send("istediğiniz sayıyı toplayabilirim")
    

@client.command()
async def add(ctx,sayi1 = 0, sayi2 = 0):
    ilk_sayi = int(input("ilk sayınız ne olsun?"))
    ilk_sayi == sayi1
    ikinci_sayi = int(input("ikinci sayınız ne olsun?")) 
    ikinci_sayi == sayi2
    await ctx.send(sayi1+sayi2)


client.run("x")
