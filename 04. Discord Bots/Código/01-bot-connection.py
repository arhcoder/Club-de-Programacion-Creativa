
#* ------------------------------------------------------------------------------------------------- *#

''' Librería para manejar la API de Discord '''
''' Instala con "pip install discord" '''

import discord
from discord.ext import commands

#* ------------------------------------------------------------------------------------------------- *#

#* Los INTENTS son una cosa bien importante en Discord;
#* Son una lista de "permisos" de acciones que se le dan
#* o no a un bot para interactuar:

intents = discord.Intents.all()

#* Ejemplos de Intents:
# intents.typing = False
# intents.presences = False
#? CONSULTA MÁS INTENTS EN EL ARCHIVO:
#? x1-intents.py;

#* ------------------------------------------------------------------------------------------------- *#


#? Se crea un bot:
bot = commands.Bot(command_prefix="*", intents=intents)


#* ------------------------------------------------------------------------------------------------- *#

'''
    Acá todo lo que haga nuestro bot...
'''

#* ------------------------------------------------------------------------------------------------- *#


#! Se conecta el bot:
#! Esto pondrá al bot en línea dentro de Discord:
bot.run("TOKEN")


#* ------------------------------------------------------------------------------------------------- *#