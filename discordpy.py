import os
import time
import discord
import json
from discord import app_commands
import requests

API_URL = requests.get("https://xwilkinx.com/data/deadswitch3/accmgr.txt").text
GID=1182811150132461619

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def relTime(tzstr):
  tz = int(tzstr.replace("GMT","").replace("+",""))
  gmt = time.gmtime()
  return (gmt[3]+tz,gmt[4])

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  await tree.sync(guild=discord.Object(id=GID))

@tree.command(name = "challenges",description="A command to view current clan challenges.",guild=discord.Object(id=GID))
async def challenges(ctx):
  requestObj = requests.get(f"{API_URL}getChallenges/type=clan")
  embed=discord.Embed(title="Current clan challenges.", color=0xff0000)
  if requestObj.status_code > 399:
    await ctx.response.send_message(f"{ctx.user.mention} An error has occured while trying to fetch challenges. ({requestObj.status_code}) Please try again later.")
  else:
    await ctx.response.send_message(f"{ctx.user.mention} Here are the current clan challenges.\n{requestObj.text}",embed=embed)


@tree.command(name = "tz_set",description="A command to set your own timezone.",guild=discord.Object(id=GID))
@app_commands.describe(tz="Your timezone, relative to GMT, e.g. 5 or -2.")
async def tz_set(ctx, tz: int):
  timezones = open("timezones.json", "r")
  table = json.load(timezones)
  timezones.close()
  if tz >= 0:
    table[str(ctx.user.id)] = f"GMT+{tz}"
    await ctx.response.send_message(f"{ctx.user.mention} Your timezone has been set to GMT+{tz}")
  else:
    table[str(ctx.user.id)] = f"GMT-{abs(tz)}"
    await ctx.response.send_message(f"{ctx.user.mention} Your timezone has been set to GMT-{abs(tz)}")
  timezones = open("timezones.json", "w")
  json.dump(table, timezones)
  timezones.close()

@tree.command(name = "tz_get",description="A command to get an users timezone",guild=discord.Object(id=GID))
@app_commands.describe(user="The user to get the timezone of, defaults to yourself")
async def tz_get(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.user
  timezones = open("timezones.json", "r")
  table = json.load(timezones)
  timezones.close()
  rt = relTime(table[str(user.id)])
  h = rt[0]
  m = rt[1]
  if m < 10: m = f"0{m}"
  await ctx.response.send_message(f"*{user.global_name}\'s* timezone is {table[str(user.id)]}. It is currently {h}:{m} for them.")



@tree.command(name = "request",guild=discord.Object(id=GID))
@app_commands.describe(name="Their in-game DS3 name.",
                       user="Their name on discord.",
                       level="Their DS3 level. NOT INCLUDING PRESTIGE.",
                       prestige="Their DS3 prestige rank.",
                       tz="Their timezone, e.g. GMT+5 or EST-2")
async def request(ctx,name:str,user:str,level:int,prestige:int,tz:str):
  embed=discord.Embed(title="Member request", color=0xff0000)
  embed.set_author(name=ctx.user.name)
  embed.add_field(name="Name", value=name, inline=False)
  embed.add_field(name="Discord Name", value=user, inline=False)
  embed.add_field(name="Level", value=f"P{prestige}, L{level}", inline=False)
  embed.add_field(name="Timezone", value=tz, inline=False)
  await client.get_channel(1183046532275109909).send(embed=embed)
  await ctx.response.send_message(f"{ctx.user.mention} Your request has been sent.")

try:
  token = os.getenv("TOKEN") or ""
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
    else:
        raise e