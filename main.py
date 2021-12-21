import os

import discord
from discord.ext import commands

from near.database import get_main
from near.web.keep_alive import keep_alive

bot_prefix = get_main.BotMainDB.MESSAGE_PREFIX
bot_creator_name = get_main.BotMainDB.BOT_CREATOR_NAME
bot_current_version = get_main.BotMainDB.BOT_VERSION
bot_owner_id_or_dev_id = get_main.BotMainDB.DEV_ID

token = get_main.BotMainDB.BOT_TOKEN
client = commands.Bot(command_prefix=bot_prefix)


@client.command()
async def loadex(ctx, extension):
    if ctx.author.id == bot_owner_id_or_dev_id:
        client.load_extension(f'cogs.{extension}')
        embed = discord.Embed(
            title="SUCCESS", description=f"`ADDED cogs.{extension} from NearBot`", color=0xff0000)
        embed.set_author(
            name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(
            title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
        embed.set_author(
            name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        await ctx.send(embed=embed)
        return


@client.command()
async def unloadex(ctx, extension):
    if ctx.author.id == bot_owner_id_or_dev_id:
        try:
            client.unload_extension(f'cogs.{extension}')
            embed = discord.Embed(
                title="SUCCESS", description=f"`REMOVED cogs.{extension} from NearBot`", color=0xff0000)
            embed.set_author(
                name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await ctx.send(embed=embed)
            return
        except:
            embed = discord.Embed(
                title="ERROR", description="`You don't have the permissions required to use this command!`", color=0xff0000)
            embed.set_author(
                name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            await ctx.send(embed=embed)
            return


# This is for user input sanitization
# Add more stuff here to make it better
blacklisted_letters_n_words = ("nc",
                               "netcat",
                               "ncat",
                               "apt",
                               "snap",
                               "remove",
                               "uninstall",
                               "{",
                               "}",
                               "<",
                               ">",
                               "/silent",
                               "/verysilent",
                               "grabify"
                               )


@client.event
async def on_message(message):
    if client.user == message.author:
        return

    msg = message.content

    if msg.startswith(f'{bot_prefix}'):

        msgaftercmnd = msg.split(" ")[1:-1]

        messagesubcont = ""
        for messagesubcontlp in msgaftercmnd:
            messagesubcont += messagesubcontlp

        if messagesubcont in blacklisted_letters_n_words:
            embed = discord.Embed(
                title="Something is wrong!", description="Please enter the command with valid characters", color=0xff0000)
            embed.set_author(
                name=f"{client.user.name}", icon_url=f"{client.user.avatar_url}")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.add_field(
                name="Possible Fix", value=f"Dont have {blacklisted_letters_n_words} in your command!", inline=True)
            await message.send(embed=embed)
            return

    await client.process_commands(message)

keep_alive()
client.run(token)
