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
  continue

@bot.command()
async def fetch(ctx, url):
  try:
    if https:// or http:// in url:
      res = requests.get(url)
      
    else:
      
    
      
