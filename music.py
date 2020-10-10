import os
import asyncio
import functools
import itertools
import math
import random

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands


@bot.event
async def on_member_join(member):
        embed = discord.Embed(
            title = "WELCOME",
            description = "**Chào mừng **" + member.mention + " **đã đến với Đài Truyền Hình Tiếng Nói Việt Nam** \n <#763256682372399114> **để đọc luật và react role nha!**",
            colour = discord.Colour(0xff33ff)
        )

        embed.set_footer(text="ĐTH - TV")
        embed.set_image(url="https://media.discordapp.net/attachments/619548575709396996/764537398464872479/image0_2.png?width=1043&height=587")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/619548575709396996/764075472354803752/imDTHage0.png")
        embed.set_author(name="ĐÀI TRUYỀN HÌNH TIẾNG NÓI VIỆT NAM", icon_url="https://media.discordapp.net/attachments/619548575709396996/764075472354803752/imDTHage0.png")

        channel = client.get_channel(763256876741427241)
        await channel.send("**Welcome** " + member.mention)

        await channel.send( embed=embed)
        
@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

bot.run(os.environ['token'])