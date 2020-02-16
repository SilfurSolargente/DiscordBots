import discord
from discord.ext import commands, tasks
import os
from itertools import cycle
import time

#Donne un préfixe pour invoquer les commandes du bot
client = commands.Bot(command_prefix='./')
#Liste de status à afficher dans l'activité du bot.
status = cycle(["Zap Mania", "Nuking SSBs", "Use './' to make me work"])

@client.event
async def on_ready():
    change_status.start() #Lance la fonction de changement de status au démarrage du bot
    print("Bot is ready") #Signale dans la console de commandes que le bot s'est lancé sans problème.

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status))) #Change le statut du bot dans un cycle selon la liste définie plus haut une fois toutes les 10 secondes.
@client.event
async def on_member_join(member):
    print(f'{member} has joined us !')

@client.event
async def on_member_remove(member):
    print("Oh nooo, "f"{member}"" has left us")
    
@client.command()
async def ping(ctx):
    """shows the bot's latency"""
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command(hidden=True) #Cette commande ne s'affiche pas dans la liste des commandes
@commands.is_owner() #Cette commande ne peut être utilisée que par le propriétaire du bot
async def load(ctx, extension): #Permet de rajouter un fichier cogs au bot
    await ctx.send('Loading new extensions...')
    client.load_extension(f'cogs.{extension}') 
    await ctx.send('Loaded !')

@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension): #Permet d'enlever un fichier cogs au bot
    await ctx.send("Unloading current extensions...")
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Unloaded !')

@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension): #Enlève puis ajoute de nouveau un fichier cogs, utile si l'on a modifié ce dernier sans redémarrer le bots
    await ctx.send("Reloading...")
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("Reloaded !")

@client.command()
async def get_utc(ctx): #Affiche l'heure actuelle en UTC, utile pour un de mes serveurs discord dans lequel les gens doivent régulièrement se référer à cette plage horaire.
    utc_time = (time.asctime(time.gmtime()))
    await ctx.send(f'The current date in UTC is :{utc_time}') #TODO : faire en sorte que l'affichage soit plus lisible

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument): #Se déclenche lorsque l'utilisateur n'a pas donné assez d'arguments pour la commande.
        await ctx.send("Please pass in all required arguments !")
    if isinstance(error, commands.CommandNotFound): #Se déclenche lorsque la commande invoquée n'est pas trouvée dans le script.
        await ctx.send("That command doesn't exist")
    if isinstance(error, commands.MissingPermissions): #Se déclenche si l'utilisateur n'a pas les permissions nécessaire pour utiliser cette commande.
        await ctx.send("You can't do that ! Put the gun down !")
    if isinstance(error, commands.NotOwner): #Se déclenche si l'utilisateur essaie d'utiliser une commande réservé au propriétaire du bot.
        await ctx.send("You aren't my master, stop trying to mess with my circuits !")

for filename in os.listdir('./cogs'): #Charge toutes les extensions pythons du dossier "cogs".
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("Token") #Synchronise le script au bot correspondant au token.
