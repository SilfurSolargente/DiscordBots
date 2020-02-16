import discord
from discord.ext import commands

class moderation(commands.Cog):
    
    def __init__(self, client): #Relie le cogs au script principal
        self.client = client
    
    @commands.command()
    @commands.has_permissions(manage_messages=True) #Vérifie que l'utilisateur invoquant la commande a le droit de supprimer des messages.
    async def clear(self, ctx, amount=1): #Efface des messages.
        "clears messages"
        await ctx.channel.purge(limit = amount)

    @commands.command()
    @commands.has_permissions(kick_members=True) #Vérifie que l'utilisateur invoquant la commande à la permission de kick.
    async def kick(self, ctx, member:discord.Member, *, reason = None):
        """Kicks an user"""
        await member.guild.kick(member, reason = reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    @commands.has_permissions(ban_members=True) #Vérifie que l'utilisateur invoquant la commande a le droit de bannir d'autres membres du serveur.
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans an user"""
        await member.ban(reason = reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """unbans an user"""
        banned_users = await ctx.guild.bans()
        memberName, memberDiscriminator = member.split('#') #Regarde séparémment le nom d'utilisateur et son discriminant ("Silfur#9920, Silfur et 9920 sont stocké dans deux variables différentes.")

        for ban_entry in banned_users: #Regarde dans la liste des utilisateurs bannis.
            user = ban_entry.user

            if (user.name, user.discriminator) == (memberName, memberDiscriminator): #Si un nom ET un discriminateur correspondent à celui suivant la commande sont dans la liste, l'utilisateur visé sera débanni.
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}.')
                return


def setup(client):
    client.add_cog(moderation(client)) #Lie ce script au script principal.


    