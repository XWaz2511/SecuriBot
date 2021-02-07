# Importation des librairies (os, dotenv, commands de discord.ext, datetime de datetime et discord.py).
import os
import dotenv as de
from discord.ext import commands
from datetime import datetime
import discord

# Chargement du fichier contenant les variables d'environnement du bot.
de.load_dotenv(dotenv_path="/root/bot-discord/.env")

# Démarrage du bot et insertion de cet évènement dans les logs.
print("\n{}: Bot starting...".format(str(datetime.now())))
logs_file = open("logs.txt", "a")
logs_file.write("\n{}: Bot starting...".format(str(datetime.now())))
logs_file.close()
intents = discord.Intents.all()
intents.members=True
bot = commands.Bot(command_prefix="#", help_command=None, Intents=intents)


# Insert, quand une commande est utilisée, l'heure à laquelle elle a été utilisée, l'id et le nom de l'utilisateur, le nom de la commande et ses arguments, ainsi que l'id et le nom du channel et du serveur dans lequel la commande a été utilisée.
def insert_in_logs(user_id, user_name, command_name, command_args, channel_id, channel_name, guild_id, guild_name):
    user_id = str(user_id)
    user_name = str(user_name)
    command_name = str(command_name)
    command_args_final = []
    channel_id = str(channel_id)
    channel_name = str(channel_name)
    guild_id = str(guild_id)
    guild_name = str(guild_name)
    
    if len(command_args) > 0:
        for arg in command_args:
            command_args_final.append(str(arg) + ",")
        command_args_final = ''.join(str(elt) for elt in command_args_final)
        logs_file = open("logs.txt", "a")
        logs_file.write("\n{}: L'utilisateur {} ({}) a utilisé la commande {} avec le(s) argument(s) {} dans le channel {} ({}) du serveur {} ({}).".format(str(datetime.now()), user_id, user_name, command_name, command_args_final, channel_id, channel_name, guild_id, guild_name))
        print("\n{}: L'utilisateur {} ({}) a utilisé la commande {} avec le(s) argument(s) {} dans le channel {} ({}) du serveur {} ({}).".format(str(datetime.now()), user_id, user_name, command_name, command_args_final, channel_id, channel_name, guild_id, guild_name))
        logs_file.close()
    else: 
        logs_file = open("logs.txt", "a")
        logs_file.write("\n{}: L'utilisateur {} ({}) a utilisé la commande {} sans arguments dans le channel {} ({}) du serveur {} ({}).".format(str(datetime.now()), user_id, user_name, command_name, channel_id, channel_name, guild_id, guild_name))
        print("\n{}: L'utilisateur {} ({}) a utilisé la commande {} sans arguments dans le channel {} ({}) du serveur {} ({}).".format(str(datetime.now()), user_id, user_name, command_name, channel_id, channel_name, guild_id, guild_name))
        logs_file.close()


# Indique que le bot est bien démarré et l'insert dans les logs.   
@bot.event
async def on_ready():
    print("\n{}: Bot successfully started !".format(str(datetime.now())))
    logs_file = open("logs.txt", "a")
    logs_file.write("\n{}: Bot successfully started !".format(str(datetime.now())))
    logs_file.close()    


# Affiche de l'aide pour toutes les commandes disponibles avec le bot.
@bot.command(name="help")
async def display_help(ctx):
    user_id = str(ctx.message.author.id)
    user_name = str(ctx.message.author.name)
    command_name = "#help"
    command_args = []
    channel_id = str(ctx.message.channel.id)
    channel_name = str(ctx.message.channel.name)
    guild_id = str(ctx.message.guild.id)
    guild_name = str(ctx.message.guild.name)
    insert_in_logs(user_id, user_name, command_name, command_args, channel_id, channel_name, guild_id, guild_name)
    await ctx.message.channel.send("**Commandes disponibles :**\n\n**Commandes bientôt disponibles :**\n\n> `#anonymisation`: Fournit des liens permettant de télécharger des logiciels pour anonymiser votre PC.")


bot.run(os.getenv("BOT_TOKEN"))