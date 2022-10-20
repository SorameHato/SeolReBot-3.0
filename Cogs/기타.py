# coding: utf-8
import discord
from discord.ext import commands as bot

class 클래스명(bot.Cog):
    def __init__(self,bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Ping(bot))