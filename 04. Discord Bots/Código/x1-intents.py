import discord
from discord.ext import commands

intents = discord.Intents()

# Intents básicos:
intents.guilds = True
intents.members = True
intents.messages = True
intents.reactions = True

# Intents adicionales:
intents.emojis = True
intents.voice_states = True
intents.presences = True
intents.guild_messages = True
intents.dm_messages = True
intents.guild_reactions = True
intents.dm_reactions = True
intents.guild_typing = True
intents.dm_typing = True
intents.integrations = True
intents.webhooks = True
intents.invites = True
intents.bans = True
intents.guilds = True
intents.typing = True

# Intents privilegiados:
intents.presences = True
intents.members = True


# Manera de dar todos los intents:
intents = discord.Intents.all()

# Configuración de intents en el bot:
bot = commands.Bot(command_prefix='!', intents=intents)