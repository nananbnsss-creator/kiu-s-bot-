import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is online!")

@bot.tree.command(name="embed", description="Send a shop embed")
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(
        title="SHOP INFORMATION",
        description="Welcome to our shop!\n\n"
                    "Please read the rules before ordering.",
        color=0x9B59B6
    )

    embed.add_field(
        name="Status",
        value="🟢 Open",
        inline=True
    )

    embed.add_field(
        name="Orders",
        value="Available",
        inline=True
    )

    embed.set_footer(text="Thank you for supporting our shop!")

    await interaction.response.send_message(embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
