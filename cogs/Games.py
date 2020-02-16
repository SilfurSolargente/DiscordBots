import discord
from discord.ext import commands
import random
import time

class games(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    #8ball game
    @commands.command(aliases = ['8ball'])
    async def _8ball(self, ctx, *, question):
        "./8ball [Your question] to have the bot answer you !"
        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes, definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    "Don't count on it.",
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.',
                    'It seems to me RNGesus does not like you']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def rps(self, ctx, *, choice):
        "./rps [Your Hand] to play Rock Paper Scissors with Dodomi !"
        botList = ['Rock', 'Paper', 'Scissors']
        botChoice = random.choice(botList)
        await ctx.send ("Alright prepare to loose\nRock...")
        time.sleep(1)
        await ctx.send ("Paper...")
        time.sleep(1)
        await ctx.send ("Scissors !")
        if ((choice == "Rock" or choice =="rock") and botChoice == "Rock"):
            await ctx.send("I chose rock too, tie !\nLet's rematch !")
        elif ((choice == "Paper" or choice =="paper") and botChoice == "Paper"):
            await ctx.send("I chose paper aswell, tie I guess\nLet's play again, I want to beat you !")
        elif ((choice == "Scissors" or choice =="scissors") and botChoice == "Scissors"):
            await ctx.send("Ah we both went with scissors, ex aequo !\nCan we play again ?")
        elif ((choice == "Rock" or choice =="rock") and botChoice == "Scissors"):
            await ctx.send("I chose scissors ! Oooh, you win...")
        elif ((choice == "Rock" or choice =="rock") and botChoice == "Paper"):
            await ctx.send("I chose Paper, I win, as always !")
        elif ((choice == "Paper" or choice=="paper") and botChoice == "Rock"):
            await ctx.send("Dammit I had rock, you win")
        elif ((choice == "Paper" or choice=="paper") and botChoice == "Scissors"):
            await ctx.send("Ha ! I had scissors, I'm the best")
        elif ((choice == "Scissors" or choice=="scissors") and botChoice == "Paper"):
            await ctx.send("Noooo, I chose paper... Hmpf, you win this time")
        elif ((choice == "Scissors" or choice=="scissors") and botChoice == "Rock"):
            await ctx.send("And I beat your scissors with my rock, I win !")
        else:
            await ctx.send("Something went wrong, did you pick something ?")
            

def setup(client):
    client.add_cog(games(client))
