# coding: utf-8
import discord
from discord.ext import commands as bot
import pickle
import random
import csv

# 시드값 : seed.pickle
# 데이터베이스 : data.pickle (2차원 배열)
# 0 : 유저ID, 1 : 소지금, 2 : 마지막으로 회생한 날짜
# 확인용 각 시드가 나온 횟수 : seedtimes.pickle

class _도박(bot.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def 조회(self,uid):
        exist = False
        with open('data.csv','r',newline='',encoding='utf-8') as a:
            reader = csv.reader(a)
            for line in reader:
                if line[0] == uid:
                    exist = True
                    return line[1]
        # .설레 도박 조회 명령어에서는 -1값이 반환되면 자동으로 db추가를 진행하는 기능을 추가해야 함
        # 이 외의 경우에는 그냥 데이터가 없다고만 출력
        if exist = False:
            return -1
    
    def 변경(self,uid,amount):
        with open('data.csv','r',newline='',encoding='utf-8') as a:
            db = pickle.load(a)

async def setup(bot):
    await bot.add_cog(_도박(bot))