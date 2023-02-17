import discord
from discord.ext import commands

app = commands.Bot(command_prefix = '/', intents=discord.Intents.all())

token = 'MTA3NTcwMDkwMzkwODIxMjc2Nw.Gq7hVZ.qbNnbOoodyLMW75BoJ8w1nrhY9HmF9t48KoeGI'

@app.event
async def on_ready():
    print('작동, 시작이야!')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def check(ctx):
    await ctx.send("후후.. 잘 작동하고 있어.")

@app.command()
async def 체크(ctx):
    await ctx.send("후후.. 잘 작동하고 있어.")

app.run(token)