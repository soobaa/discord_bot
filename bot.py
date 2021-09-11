import discord
import os
import random
from keepalive import keep_alive


client = discord.Client()

zubair_wrds = ["fuck", "men", "tf", "men", "hello", "wow", "what"]

zubair_respons = [
  "Whatttttttttttttt",
  "can u shut up already",
  "ok",
  "MENNNNN",
  "loofah haha",
  "House 120",
  "kys"

]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content
  


  if any(word in msg for word in zubair_wrds):
    await message.channel.send(random.choice(zubair_respons))

keep_alive()
client.run(os.environ['TOKEN'])
