# coding: utf-8
import discord
from discord.ext import commands as bot
import random

class 확률(bot.Cog):
    def __init(self,bot):
        self.bot = bot
    
    def 확률처리(self, arg):
        # arg문 정제(?)
        if(arg[len(arg)-2:len(arg)] == '확률'):
            arg = arg[0:len(arg)-2]
        if(arg[len(arg)-3:len(arg)] == '가능성'):
            arg = arg[0:len(arg)-3]
        if(arg[len(arg)-2:len(arg)] == '비율'):
            arg = arg[0:len(arg)-2]
        if(arg[len(arg)-1:len(arg)] == ' '):
            arg = arg[0:len(arg)-1]
        return("{arg} 확률은 {rnd}%입니다.".format(arg=arg,rnd=random.randint(0,100)))
    
    @bot.command()
    async def 확률(self, ctx,*,text):
        await ctx.send(확률처리(text))

async def setup(bot):
    await bot.add_cog(Ping(bot))