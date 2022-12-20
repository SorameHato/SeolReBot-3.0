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
        '''추후 해야 하는 작업 : 주작 부활
        arg문 첫 번째 단어에 '아메' '단비' '<@405716868251385866>' 'アメ' 'ｱﾒ' '메냥' '국왕' '아냥' '아짱' 등이 포함되어 있고 (여기서 예외처리를 해서 '아메짱' '아메쨩'은 걸러야 함) arg문에 '여신' '천사' '아이돌' '텐시' '귀여울' 등이 포함된 경우
        긍정문이면 jujak=-2 (100%)
        부정문이면 jujak=-3 (0%)
        arg문 첫 번째 단어에 '바기' '<@405347248218832906>'가 포함되어 있고 arg문에 '인싸'가 포함된 경우
        긍정문이면 jujak=-2 (100%)
        부정문이면 jujak=-3 (0%)
        '바보'는 긍정문이면 jujak=-3 부정문이면 jujak=-2'''
        # arg문 정제(?)
        if(arg[len(arg)-2:len(arg)] == '확률'):
            arg = arg[0:len(arg)-2]
        if(arg[len(arg)-3:len(arg)] == '가능성'):
            arg = arg[0:len(arg)-3]
        if(arg[len(arg)-2:len(arg)] == '비율'):
            arg = arg[0:len(arg)-2]
        if(arg[len(arg)-1:len(arg)] == ' '):
            arg = arg[0:len(arg)-1]
        jujak_list = [[['아메','단비','405716868251385866','アメ','ｱﾒ','메냥','국왕','아냥','아짱'],['여신','천사','아이돌','텐시','귀여','귀엽','천재'],['아닐','않을','틀릴'],['아메짱','아메쨩']],[['바기','405347248218832906'],['인싸','바보가 아닐','천재','똑똑'],['인싸가 아닐','바보일','천재가 아닐','똑똑하지 않을','멍청할','멍청한','바보같은'],None]]
        jujak = 0
        for jujak_item in jujak_list:
            temp = self.주작(arg,jujak_item[0],jujak_item[1],jujak_item[2],jujak_item[3])
            if temp < jujak:
                jujak=temp
        if jujak == 0:
            return(f"{arg} 확률은 {random.randint(0,100)}%입니다.")
        elif jujak == -1:
            return(f"{arg} 확률은 {random.randint(0,100)}%입니다. (디버그용 : 주작값 -1)")
        elif jujak == -2:
            return(f"{arg} 확률은 100%입니다. (디버그용 : 주작값 -2)")
        elif jujak == -3:
            return(f"{arg} 확률은 0%입니다. (디버그용 : 주작값 -3)")
        else:
            return("오류가 발생했어요! 주작 함수의 처리값이 올바르지 않아요.")
    
    @commands.slash_command(guild_ids = guild_ids, description="설레봇이 확률을 계산해줘요!")
    async def 확률(self, ctx,text:discord.Option(str,'어떤 것의 확률을 계산할 지 입력해주세요. (예시 : 단비냐아가 여신일, 단비냐아가 여신일 확률, 하토가 내일 오락을 갈 가능성)',name='문장')):
        await ctx.respond(self.확률처리(text))

def setup(bot):
    bot.add_cog(_확률(bot))