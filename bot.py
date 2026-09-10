import discord
from discord.ext import commands
from config import TOKEN
from logic import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

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
async def detect(ctx):
    await ctx.send("Algılama başladı.")
    if ctx.message.attachments:
       await ctx.send("Görsel algılandı.")
       for attachment in ctx.message.attachments:
           filename = attachment.filename
           filepath = f"images/{filename}"
           await attachment.save(filepath)
           name, score = get_class("converted_keras (5)/keras_model.h5",
                                    "converted_keras (5)/labels.txt",
                                    filepath)
           await ctx.send(f"Bu görsel %{int(score * 100)} {name.strip()} nesnesine benziyor.")
    else:
     await ctx.send("Komutu çalıştırmak için bir görsel ekleyin.")




     
bot.run(TOKEN)         