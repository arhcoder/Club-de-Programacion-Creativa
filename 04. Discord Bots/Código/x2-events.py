# --------------------------------------- #

# ACÁ EL CÓDIGO DE CREACIÓN DE UN BOT ... #

# --------------------------------------- #

# EVENTS:
@bot.event
async def on_ready():
    # Se ejecuta cuando el bot está listo y conectado al servidor;

@bot.event
async def on_message(message):
    # Se ejecuta cuando se recibe un mensaje en el servidor;

@bot.event
async def on_message_edit(before, after):
    # Se ejecuta cuando se edita un mensaje existente;

@bot.event
async def on_message_delete(message):
    # Se ejecuta cuando se elimina un mensaje existente;

@bot.event
async def on_reaction_add(reaction, user):
    # Se ejecuta cuando se agrega una reacción a un mensaje;

@bot.event
async def on_reaction_remove(reaction, user):
    # Se ejecuta cuando se elimina una reacción de un mensaje;

@bot.event
async def on_member_join(member):
    # Se ejecuta cuando un miembro se une al servidor;

@bot.event
async def on_member_remove(member):
    # Se ejecuta cuando un miembro abandona el servidor;

@bot.event
async def on_member_update(before, after):
    # Se ejecuta cuando se actualiza la información de un miembro;

@bot.event
async def on_voice_state_update(member, before, after):
    # Se ejecuta cuando cambia el estado de voz de un miembro;

@bot.event
async def on_guild_join(guild):
    # Se ejecuta cuando el bot se une a un nuevo servidor;

@bot.event
async def on_guild_remove(guild):
    # Se ejecuta cuando el bot es eliminado o expulsado de un servidor;

# Otros eventos disponibles: on_guild_update, on_guild_role_create, on_guild_role_delete,
# on_guild_role_update, on_guild_emojis_update, on_guild_available, on_guild_unavailable, etc.
