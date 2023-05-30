
#* ------------------------------------------------------------------------------------------------- *#

import discord
from discord.ext import commands

intents = discord.Intents.all()

# Se crea un bot:
bot = commands.Bot(command_prefix="!", intents=intents, description="...", help_command="", options="")


#* ------------------------------------------------------------------------------------------------- *#

# EVENTOS DE EJEMPLO:
# CONSULTA MÁS EVENTS EN EL ARCHIVO:
# x2-events.py;

#* ------------------------------------------------------------------------------------------------- *#

# Cuando el bot está listo y en línea:
@bot.event
async def on_ready():
    print("Bot en línea 😎")

# Cuando se envía un mensaje en el server:
@bot.event
async def on_message(message):
    print("Se envió en el server:\n", message)

#* ------------------------------------------------------------------------------------------------- *#


# Se conecta el bot:
bot.run("TOKEN")


#* ------------------------------------------------------------------------------------------------- *#