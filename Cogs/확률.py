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
    
    def 주작(self,arg,name_list:list,compare_list1:list,compare_list2:list,exclude_list:list=None): #name_list:list 이거는 name_list가 list형이라고 지정하는 거
        '''주작 처리 함수
        input : arg(유저가 입력한 문장), name_list(이름 부분), compare_list1(100%로 만들어야 하는 것), compare_list2(0%로 만들어야 하는 것), exclude_list(이름 부분에서 제외할 이름) : 아래 주석 참고
        output: 이름이 포함되지 않은 경우 0
                이름은 포함되어 있지만 뒷부분의 문장이 포함되지 않은 경우 -1
                100%로 만들어야 하는 경우 -2
                  0%로 만들어야 하는 경우 -3'''
        ret = 0
        for item in name_list:
            if arg.find(item) != -1:
                ret = -1
        if exclude_list is not None:
            for item in exclude_list:
                if arg.find(item) != -1:
                    ret = 0
        if ret == -1:
            for item in compare_list1:
                if arg.find(item) != -1:
                    ret = -2
            for item in compare_list2:
                if arg.find(item) != -1:
                    ret = -3
        return ret
    
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
        jujak = 0
        if jujak == 0:
            return(f"{arg} 확률은 {random.randint(0,100)}%입니다.")
        else:
            return("오류가 발생했어요! 주작 함수의 처리값이 올바르지 않아요. 주작 함수는 3.2 버전에서 비활성화 되었어요. 해당 오류가 발생한다면 하토를 호출해주세요!")
    
    @commands.slash_command(guild_ids = guild_ids, description="설레봇이 확률을 계산해줘요!")
    async def 확률(self, ctx,text:discord.Option(str,'어떤 것의 확률을 계산할 지 입력해주세요. (예시 : 판치가 여자일, 판치가 여자일 확률, 하토가 내일 오락을 갈 가능성)',name='문장')):
        await ctx.respond(self.확률처리(text))

def setup(bot):
    bot.add_cog(_확률(bot))