import asyncio
import os
import random
import shutil
import discord
from discord import Intents
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import time
import requests
##
bot = commands.Bot(command_prefix='+')
bot.remove_command("help")
##
@bot.event
async def on_ready():
    print('=======================')
    print('Bot is online!')
    print('=======================')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for +obfuscate"))
##
@bot.command()
async def obfuscate(ctx):
    try:
        #e = os.path.basename(ctx.message.attachments[0])
        #print(ctx.author.name + " is obfuscating a file " + os.path.splitext(e))
        message = ctx
        if ctx.author.bot:
            return
        if not ctx.message.attachments:
            await ctx.send("Please send a file")
            return 
        await ctx.message.attachments[0].save("script.lua")
        a = await ctx.send("**Obfuscating...**")
        time.sleep(0.5)
        os.system("obfuscate.sh")
        time.sleep(0.5)
        await ctx.send(file=discord.File("output.lua"))
        await a.edit(content="**Obfuscated!**")
    except a:
        ctx.send(a)
##
bot.run("256ahruwgsuawveahHquHwuYqhUaYayHaU")
