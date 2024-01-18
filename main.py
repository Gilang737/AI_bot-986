import discord, random, requests, os
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'file disimpan atas nama {file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)

            if hasil[0] == 'merkurius\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah planet merkurius')
            elif hasil[0] == 'venus\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah planet venus')   
            elif hasil[0] == 'bumi\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah planet bumi')  
            elif hasil[0] == 'mars\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah planet mars') 
            elif hasil[0] == 'jupiter\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah planet jupiter')   
            elif hasil[0] == 'saturnus\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah planet saturnus')   
            elif hasil[0] == 'uranus\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah planet uranus')   
            elif hasil[0] == 'neptunus\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah planet neptunus')    
            else:
                await ctx.send('Gambar tidak terdeteksi')
                
    else:
        await ctx.send("ANDA TIDAK MENGIRIM APAPUN")



bot.run("MTEzNDEwNTc2Mzk4MDI0NzA1Mg.GGb6M6.QZM-2xBsNJYIgMijizZuUMLVLQnCiB-tQcpwvk")
