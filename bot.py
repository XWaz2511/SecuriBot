# Importation des librairies (os, dotenv, commands de discord.ext, datetime de datetime et discord.py).
import os
from dotenv import load
from discord.ext import commands
from datetime import datetime
import discord

# Chargement du fichier contenant les variables d'environnement du bot.
load("/root/home/xwaz/securibot/.env")

# Démarrage du bot et insertion de cet évènement dans les logs.
print("\n{}: Bot starting...".format(str(datetime.now())))
logs_file = open("logs.txt", "a")
logs_file.write("\n{}: Bot starting...".format(str(datetime.now())))
logs_file.close()
intents = discord.Intents.all()
intents.members=True
bot = commands.Bot(command_prefix="#", help_command=None, Intents=intents)


# A insérer dans chaque commande, affiche un message d'informations (si il y en a un) quand une commande est envoyée.
async def display_information_message(ctx):
    information_message = str(os.getenv("INFORMATION_MESSAGE"))
    if len(information_message) > 0:
        await ctx.message.channel.send(information_message)
    else:
        pass


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
    command_args = command_args
    if len(command_args) > 0:
        command_args = command_args.split(" ")
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


# Récupère un problème rapporté par un utilisateur, inscrit l'évènement dans les logs, l'affiche sur la console et l'enregistre dans le fichier reports_file.txt.
@bot.command(name="report")
async def report_problem(ctx, *, args):
    user_id = str(ctx.message.author.id)
    user_name = str(ctx.message.author.name)
    command_name = "#report"
    command_args = str(args)
    channel_id = str(ctx.message.channel.id)
    channel_name = str(ctx.message.channel.name)
    guild_id = str(ctx.message.guild.id)
    guild_name = str(ctx.message.guild.name)
    insert_in_logs(user_id, user_name, command_name, command_args, channel_id, channel_name, guild_id, guild_name)
    await display_information_message(ctx)
    reports_file = open("reports.txt", "a")
    reports_file.write("{}: Problème reporté par l'utilisateur {} ({}): {}.\n\n".format(str(datetime.now()), user_id, user_name, args))
    reports_file.close()
    await ctx.message.channel.send("> Merci ! Votre message a bien été envoyé ! Le problème sera traité au plus vite.")


# récupère une suggestion, la stocke dans le fichier suggestions.txt et enregistre le tout dans les logs.
@bot.command(name="suggestion")
async def report_problem(ctx, *, args):
    user_id = str(ctx.message.author.id)
    user_name = str(ctx.message.author.name)
    command_name = "#suggestion"
    command_args = str(args)
    channel_id = str(ctx.message.channel.id)
    channel_name = str(ctx.message.channel.name)
    guild_id = str(ctx.message.guild.id)
    guild_name = str(ctx.message.guild.name)
    insert_in_logs(user_id, user_name, command_name, command_args, channel_id, channel_name, guild_id, guild_name)
    await display_information_message(ctx)
    suggestions_file = open("suggestions.txt", "a")
    suggestions_file.write("{}: Suggestion soumise par l'utilisateur {} ({}): {}.\n\n".format(str(datetime.now()), user_id, user_name, args))
    suggestions_file.close()
    await ctx.message.channel.send("> Merci ! Votre suggestion a bien été soumise à l'équipe de développement ! Nous vous remercions infiniment pour aider au développement et à l'amélioration de SecuriBot.")


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
    await display_information_message(ctx)
    await ctx.message.channel.send("**Commandes disponibles :**\n\n> `#report votre_problème`: Permet de signaler un problème avec SecuriBot.\n\n> `#suggestion votre_suggestion`: Vous permet de soummettre une suggestion pour aider à améliorer SecuriBot.\n\n**Commandes bientôt disponibles :**\n\n> `#anonymisation`: Fournit des liens permettant de télécharger des logiciels pour anonymiser votre PC.")


bot.run(os.getenv("BOT_TOKEN"))