# coding: utf-8
import discord, os, sys
from discord.ext import commands
global guild_ids
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위폴더의 파일을 import할 수 있게 해주는 거
from main import guild_ids
import random

class _prob(commands.Cog): #prob은 probability의 약자
    def __init__(self,bot):
        self.bot = bot
    
    def probCalc(self,arg):
        #arg문 정제(?)
        if(arg[-2:] == '은?'):
            arg = arg[:-2]
        if(arg[-1:] == '?'):
            arg = arg[:-1]
        if(arg[-2:] == '확률'):
            arg = arg[:-2]
        if(arg[-3:] == '가능성'):
            arg = arg[:-3]
        if(arg[-2:] == '비율'):
            arg = arg[:-2]
        if(arg[-1:] == ' '):
            arg = arg[:-1]
        return(f"{arg} 확률은 {random.randint(0,100)}%이에요!")
    
    @commands.slash_command(guild_ids = guild_ids, description="무언가가 일어날 확률이 궁금하시다고요? 유설레가 계산해드릴게요!")
    async def 확률(self, ctx,text:discord.Option(str,'어떤 것의 확률을 계산할 지 입력해주세요. (예시 : 하토가 귀엽지 않을, 하토가 귀엽지 않을 확률, 하토가 내일 오락을 갈 가능성)',name='문장')):
        await ctx.respond(self.probCalc(text))

def setup(bot):
    bot.add_cog(_prob(bot))