import discord
from discord.ext import commands

TOKEN = '' # 1でコピーしたBotのトークンを記述

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} としてログインしました。')

@bot.command()
async def hello(ctx):
    await ctx.send('こんにちは！')

bot.run(TOKEN)