# coding: utf-8
import discord
from discord.ext import commands
import random
global guild_ids
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위폴더의 파일을 import할 수 있게 해주는 거
from main import guild_ids

class _확률(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def 확률처리(self,arg):
        # arg문 정제(?)
        if(arg[len(arg)-2:len(arg)] == '확률'):
            arg = arg[0:len(arg)-2]
        if(arg[len(arg)-3:len(arg)] == '가능성'):
            arg = arg[0:len(arg)-3]
        if(arg[len(arg)-2:len(arg)] == '비율'):
            arg = arg[0:len(arg)-2]
        if(arg[len(arg)-1:len(arg)] == ' '):
            arg = arg[0:len(arg)-1]
        return(f"{arg} 확률은 {random.randint(0,100)}%이에요!")
    
    @commands.slash_command(guild_ids = guild_ids, description="설레봇이 확률을 계산해줘요!")
    async def 확률(self, ctx,text:discord.Option(str,'어떤 것의 확률을 계산할 지 입력해주세요. (예시 : 판치가 여자일, 판치가 여자일 확률, 하토가 내일 오락을 갈 가능성)',name='문장')):
        await ctx.respond(self.확률처리(text))

def setup(bot):
    bot.add_cog(_확률(bot))
