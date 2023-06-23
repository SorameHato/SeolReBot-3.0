# coding: utf-8
import discord, os, sys
from discord.ext import commands
global guild_ids
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from main import guild_ids
from SkyLib.josa import josa에요
import random

class _meal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mealList = ["치킨","피자","짜장","짬뽕","볶음밥","돌솥비빔밥","떡볶이","순대","족발","보쌈","삼겹살","파스타","돈카츠","라멘","라면","스테이크","김밥","샌드위치","햄버거","한정식","불고기","초밥","우동","닭갈비","빵","마라탕","샤브샤브","탕수육","토스트","부대찌개","수제비","곰탕","설렁탕","순대국","칼국수","회","제육볶음","감자탕","청국장","물회","깐풍기","사케동","연어스테이크","쌀국수","송어회","리조또","타코야끼","카레","잔치국수","밥버거","곱창","육회","스키야키","김치찌개","된장찌개",'카라아게동']
        self.nightMealList = ["치킨","피자","떡볶이","순대","족발","보쌈","라면","우동","빵","탕수육","부대찌개","회","제육볶음","타코야끼","카레","잔치국수","곱창","육회","계란말이","어묵탕","김치찌개","라멘","해장국","모둠튀김","매운새우깡","쌀새우깡","새우깡블랙","콩나물해장라면"]
    
    @commands.slash_command(name='식사추천',guild_ids=guild_ids,description='설레봇이 어떤 걸 먹을 지 추천해드려요!')
    async def mealSelect(self, ctx, arg:discord.Option(str,'아침인지 점심인지 저녁인지 선택해주세요!',name='종류',choices=['아침','점심','저녁'],required=True)):
        embed = discord.Embed(title=f'유설레가 추천하는 오늘의 {arg} 메뉴는? {self.__josa__(random.choice(self.mealList))}',description='저녁식사 메뉴를 추천하는 함수를 돌려 쓰고 있어서 아침, 점심으로 먹기에는 부담스러운 음식이 나올지도 몰라요. 양해해주세요!' if (arg != '저녁') else None,color=0x04ccff)
        await ctx.respond(embed=embed)
    
    @commands.slash_command(name='야식추천',guild_ids=guild_ids,description='설레봇이 야식을 추천해드려요!')
    async def nightMealSelect(self, ctx):
        embed = discord.Embed(title=f'유설레가 추천하는 오늘의 야식 메뉴는? {self.__josa__(random.choice(self.nightMealList))}',color=0x04ccff)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(_meal(bot))