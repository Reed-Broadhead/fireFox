from dotenv import load_dotenv
import os
load_dotenv()

import discord
from discord.ext import commands
from discord import app_commands
import random 
from modles_commands import changeScore, new_player, wlRatio, leaderBoard, deckCheck, setDeck


client = commands.Bot(command_prefix = '!', intents = discord.Intents.default())

@client.event
async def on_ready():
    print("Bot is up and Ready!")
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



@client.tree.command(name="roll")
async def roll(interaction: discord.Interaction):
    is_allowed = False
    for x in interaction.user.roles:
        if x.name == "testRole":
            is_allowed = True

    await interaction.response.send_message(f"hey! {'leader' if is_allowed else 'suke'} ",
    ephemeral=True)


# hello 
@client.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"hey {interaction.user.mention} {interaction.user.name}!",
    ephemeral=True)

trueFactNames = ["john", "lucas", "lynn", "ian"]
trueFactStatments = ["loves gay midget porn", "is gay", "loves weiners"]

# true fact 
@client.tree.command(name="true_facts")
async def true_facts(interaction: discord.Interaction):
    await interaction.response.send_message(f"{random.choice(trueFactNames)} {random.choice(trueFactStatments)}",
    ephemeral=True)


# change score 
@client.tree.command(name="change_score")
@app_commands.describe(wol = "w for wins: l for loses", name = "name of player", amount = "can both add and subtract")
@app_commands.choices(wol= [
    discord.app_commands.Choice(name="wins", value="w"),
    discord.app_commands.Choice(name="loses", value="l"),
])
async def change_score(interaction: discord.Interaction, wol: str, name: str, amount: int):
    changeScore(wol, name, amount)
    await interaction.response.send_message(f"{amount} { 'wins' if wol == 'w' else 'loses' } were added to {name}'s record",
    ephemeral=True)


# add player 
@client.tree.command(name="add_player")
@app_commands.describe(nname = "name of new player")
async def add_player(interaction: discord.Interaction, nname: str):
    new_player(nname)
    await interaction.response.send_message(f"{nname} has been added to the roster",
    ephemeral=True)


# win loses ration 
@client.tree.command(name="wl_ratio")
@app_commands.describe(nname = "what players ratio would you like to see?")
async def wl_ratio(interaction: discord.Interaction, nname: str):
    await interaction.response.send_message(f"{nname}'s w:l ratio: {wlRatio(nname)}",
    ephemeral=True)

# leader board 
@client.tree.command(name="leader_board")
async def leader_board(interaction: discord.Interaction):
    await interaction.response.send_message("\n".join(leaderBoard()))

# deck check
@client.tree.command(name="deck_check")
async def deck_check(interaction: discord.Interaction):
    is_allowed = False
    for x in interaction.user.roles:
        if x.name == "testRole":
            is_allowed = True
    await interaction.response.send_message("\n".join(deckCheck()) if is_allowed else "only high wizards are allowed to use this command.",
    ephemeral=True)

# set deck
@client.tree.command(name="set_deck")
@app_commands.describe(deck = "what deck will you be playing")
async def set_deck(interaction: discord.Interaction, deck: str):
    await interaction.response.send_message(setDeck(interaction.user.name, deck),
    ephemeral=True)

# clear deck

# ban list


client.run(os.getenv("TOKEN"))