import discord
from discord.ext import commands
from Drone import Drone

bot = commands.Bot(command_prefix="°")


@bot.event
async def on_ready():
    global appli
    appli = await bot.application_info()
    print("Logged in! bot invite: https://discordapp.com/api/oauth2/authorize?client_id=" +
          str(appli.id) + "&permissions=0&scope=bot")


@bot.command()
async def test(ctx):
    drone = Drone()


bot.run(open("Token.txt").read())
