# coding: utf-8
import discord
from discord.ext import commands
import random
global guild_ids
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from main import guild_ids

class _식사추천(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def 식사추천(self):
        음식list = ["치킨","피자","짜장","짬뽕","볶음밥","돌솥비빔밥","떡볶이","순대","족발","보쌈","삼겹살","파스타","돈카츠","라멘","라면","스테이크","김밥","샌드위치","햄버거","한정식","불고기","초밥","우동","닭갈비","빵","마라탕","샤브샤브","탕수육","토스트","부대찌개","수제비","곰탕","설렁탕","순대국","칼국수","회","제육볶음","감자탕","청국장","물회","깐풍기","사케동","연어스테이크","쌀국수","송어회","리조또","타코야끼","카레","잔치국수","밥버거","곱창","육회","스키야키","김치찌개","된장찌개"]
        return(random.choice(음식list))
    
    def 야식추천(self):
        야식list = ["치킨","피자","떡볶이","순대","족발","보쌈","라면","우동","빵","탕수육","부대찌개","회","제육볶음","타코야끼","카레","잔치국수","곱창","육회","계란말이","어묵탕","김치찌개","라멘","해장국","모둠튀김","매운새우깡","쌀새우깡","새우깡블랙","콩나물해장라면"]
        return(random.choice(야식list))
    
    @commands.slash_command(name='아침추천',guild_ids=guild_ids,description='설레봇이 아침 메뉴를 추천해드려요!')
    async def 아침메뉴추천(self, ctx):
        await ctx.respond("유설레가 추천하는 오늘의 아침 메뉴는? "+self.식사추천()+"(이)에요!\n점심, 저녁식사 메뉴를 추천하는 함수를 돌려 쓰고 있어서 아침으로 먹기에는 부담스러운 음식이 나올지도 몰라요. 양해해주세요!")

    @commands.slash_command(name='점심추천',guild_ids=guild_ids,description='설레봇이 점심 메뉴를 추천해드려요!')
    async def 점심메뉴추천(self, ctx):
        await ctx.respond("유설레가 추천하는 오늘의 점심 메뉴는? "+self.식사추천()+"(이)에요!\n저녁식사 메뉴를 추천하는 함수를 돌려 쓰고 있어서 점심으로 먹기에는 부담스러운 음식이 나올지도 몰라요. 양해해주세요!")

    @commands.slash_command(name='저녁추천',guild_ids=guild_ids,description='설레봇이 저녁 메뉴를 추천해드려요!')
    async def 저녁메뉴추천(self, ctx):
        await ctx.respond("유설레가 추천하는 오늘의 저녁 메뉴는? "+self.식사추천()+"(이)에요!")

    @commands.slash_command(name='야식추천',guild_ids=guild_ids,description='설레봇이 야식 메뉴를 추천해드려요!')
    async def 야식메뉴추천(self, ctx):
        await ctx.respond("유설레가 추천하는 오늘의 야식 메뉴는? "+self.야식추천()+"(이)에요!")

def setup(bot):
    bot.add_cog(_식사추천(bot))
# 클래스명을 식사추천으로 쓰면 함수명하고 겹쳐서 TypeError: __init__() missing 1 required positional argument: 'bot' 오류가 난다!
