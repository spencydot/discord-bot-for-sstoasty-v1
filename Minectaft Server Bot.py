import discord
from discord.ext import commands
from mcstatus import MinecraftServer
import random
import time
import pandas as pd
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

MinecraftServerStatus = "Server Status - Offline"
client = commands.Bot(command_prefix = '.')
dclient = discord.Client()
guild = discord.Guild
channel = client.get_channel(815924800550862858)
version = "1.17 - Caves and Clifs"

LogLocation = "C:/Users\VirusVault\Desktop\MinecraftServer\logs\latest.log"
@client.command()
async def ServerConsole(ctx):
    f = open(LogLocation, "r")
    lines = f.read().splitlines()
    last_line = lines[-4:]
    formatted_string = "\n". join(last_line). join("``")
    await ctx.send(formatted_string)

@client.command()
async def ServerStatus(ctx):
    print("SERVER CALLED")
    await client.wait_until_ready()
    channel = client.get_channel(id)
    #MinecraftEmbed = await ctx.send(f.read)   
    while True:
        print("PRINTING RESPONCSE")
        try:
            server = MinecraftServer.lookup("_______________:25565")
            status = server.status()
            client.get_channel("815924800550862858")
            print("ONLINE")

            embed=discord.Embed(
            title="Minecraft Server Status",
            url="https://i.pinimg.com/originals/2a/b1/c3/2ab1c37cfdff720c6de2ddb07328f145.jpg",
            color=discord.Color.red())
            embed.set_author(name="", url="", icon_url="https://i.pinimg.com/originals/2a/b1/c3/2ab1c37cfdff720c6de2ddb07328f145.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/816297797942378550/856303496662745108/image0.png")
            embed.add_field(name="**Status**", value="Online : "+version, inline=False)
            embed.add_field(name="**How to join**", value='To join the server you need to get your self whitelisted, Dm ٴٴ@SPENCY#2356 and he will give you more info. Dont have Minecraft? [Here](https://tlauncher.org/en/) The russians have figured that out! :flag_ru::thumbsup: ', inline=False)
            embed.add_field(name="**Server IP**", value="||_______________||", inline=False)
            embed.set_footer(text="This is a whitelisted server pepeHacker")
            await ctx.send(embed=embed)
            
        except:
            client.get_channel("815924800550862858")
            print("OFFLINE")
            embed=discord.Embed(
            title="Minecraft Server Status",
            url="https://i.pinimg.com/originals/2a/b1/c3/2ab1c37cfdff720c6de2ddb07328f145.jpg",
            color=discord.Color.red())
            embed.set_author(name="", url="", icon_url="https://i.pinimg.com/originals/2a/b1/c3/2ab1c37cfdff720c6de2ddb07328f145.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/816297797942378550/856303496662745108/image0.png")
            embed.add_field(name="**Status**", value="Offline: "+version, inline=False)
            embed.add_field(name="**How to join**", value='To join the server you need to get your self whitelisted, Dm ٴٴ@SPENCY#2356 and he will give you more info. Dont have Minecraft? [Here](https://tlauncher.org/en/) The russians have figured that out! :flag_ru:', inline=False)
            embed.add_field(name="**Server IP**", value="||_______________||", inline=False)
            embed.set_footer(text="This is a whitelisted server pepeHacker")
            await ctx.send(embed=embed)
        break

@client.event
async def on_message(message):
    if str(message.channel) == "minecraft🌳" and message.content != "":
        print("DELETING")
        await client.process_commands(message)
#        await message.channel.purge(limit=1,)

client.run('')