import discord
import youtube_dl
from discord.ext import commands

TOKEN = 'NDUyMzQxOTA3MDEyNzE0NTI2.DhyTUg.gkEgwtzKbQTRRbTqDaqy2i2yn9k'
client = commands.Bot(command_prefix = 's1!')

players = {}

@client.event
async def on_ready():
    print('sadness 01 - Online!')
             await client.change_presence(game=discord.Game(name='XXXTENTACION - 24/7 [BOT SADNESS 01]'))

@client.command(pass_context=True)
async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
             await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
             await voice_client.disconect()

@client.command(pass_context=True)
async def play (ctx, url):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

client.run(TOKEN)
