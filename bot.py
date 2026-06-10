import os
import subprocess
import asyncio
import sqlite3
import discord
import requests
import shutil
from discord import command.ext

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
  print("Bot Active & Running")
  check = os.system("pip show requests >/dev/null")
  if check == 0:
    pass
  else:
    subprocess.run(["pip install requests"])
  

@bot.command()
async def fetch(ctx, url):
  try:
    if https:// or http:// in url:
      if "." not in url:
        ctx.send("Error: Invaild Domain ({url}) ✗")
      else:
        res = requests.get(url)
        data = res.text()
        em = discord.Embed(
          title="Website Fetched √
        ctx.send(embed=em)
        ctx.send
    else:
      
    
      
