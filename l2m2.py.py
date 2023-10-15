import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def tell_me_about_pollutions(ctx):
    await ctx.send(f"Увожаемый пользователь, если вы будете переробатывать пластик, то получите скидку в магазине Фаворит")


bot.run("MTE1ODAxOTQ2MTM3MTEzNDA5Mw.G2fbVq.GituiZCBMBOugZ4edXEdaimFQllDUrIBwuyszw")