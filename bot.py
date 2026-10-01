import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = 123456789012345678

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)

    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)

    print(f"{bot.user} is online!")
    print("Slash commands synced!")

@bot.tree.command(name="embed", description="Send a shop embed")
async def embed(interaction: discord.Interaction):

    embed = discord.Embed(
        title="SHOP INFORMATION",
        description="Welcome to our shop!\n\nPlease read the rules before ordering.",
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

bot.run(TOKEN)
