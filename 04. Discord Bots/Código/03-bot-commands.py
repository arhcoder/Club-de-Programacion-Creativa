import discord
from discord.ext import commands

# Se crea un bot con todos los permisos:
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="*", intents=intents, description="Bot chido")

# Se crea un event para que se sepa cuando el bot está ya en línea:
@bot.event
async def on_ready():
    print("Bot en línea 😎")

#* ------------------------------------------------------------------------------------------------- *#
'''
    PROGRAMANDO COMANDOS DE EJEMPLO:

    Se va a crear un comando llamado "hola", al que el bot responderá con un "hola" de regreso...

    NOTA: Como el comando (función) se llamará "hola", y arriba se especificó que el prefijo es "*";
    Dentro de Discord se llamará el comando escribiendo en un chat "*hola";
'''

@bot.command()
async def hola(mensaje):

    # Responde al mensaje con un hey:
    await mensaje.reply("Hey!")

    # Envía en mensaje en el mismo chat, con un "hola":
    await mensaje.send("Hola :3")

    # Imprime todo lo que tiene el mensaje:
    print(mensaje.message)

    # Envía un mensaje extrayéndo el nombre de quien mandó el mensaje:
    await mensaje.send(f"¿Cómo estás {mensaje.author.name}?")


# Se conecta el bot:
bot.run("TOKEN")


#* ------------------------------------------------------------------------------------------------- *#