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
     
    '''해당 유저의 잔고를 조회하는 명령어
    input : uid (ctx.message.author.id 로 얻은 해당 유저의 id)
    output : 해당 유저의 잔액(단, 해당 유저의 데이터가 없는 경우 -1)'''
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
        if exist == False:
            return -1
     
    '''해당 유저의 잔고를 변경하는 명령어
    input : uid (ctx.message.author.id 로 얻은 해당 유저의 id)
    amount (얼마나 변경할 것인지, 주의해야 할 점은 잔액을 인출하는 경우 음수로 입력해야 함, 그리고 절댓값을 입력하는 게 아님. 26만원에서 25만 5천원으로 변경하고 싶으면 255000이 아닌 -5000으로 입력해야 함)
    output : 인출/입금 후 잔액 (단, 해당 유저의 데이터가 없는 경우 -1, 잔고가 부족한 경우 -2)'''
    def 변경(self,uid,amount):
        db = list()
        status = -1
        with open('data.csv','r',newline='',encoding='utf-8') as a:
            reader = csv.reader(a)
            for line in reader:
                if line[0] == uid:
                    if line[1] + amount >= 0:
                        line[1] += amount
                        ret = line[1]
                        status = 1
                    else:
                        status = -2
                db.append(line)
        if status == 0:
            with open('data.csv','w',newline='',encoding='utf-8') as a:
                writer = csv.writer(a)
                writer.writerows(db)
            return ret
        else:
            return status
     
    def 잭팟뽑기:
        with open('seed_basic.pickle','rb') as a:
            seed = pickle.load(a)
            return random.choice(list3)
     
    def 잭팟:
        결과 = self.잭팟뽑기()
        
     
    @bot.command()
    async def 도박(ctx,*,text):
        메뉴 = text.split(' ')[0]
        if 메뉴 == '잭팟' :
            pass
        if(메뉴 == "회생"):
            await ctx.send("아직 데이터 확인 부분의 코드가 완성되지 않았어요. 하지만 벌써부터 회생을 하려는 걸 보니 당신은 도박 중독자이신 것 같네요.\n한국도박문제예방치유원에서 운영하는 도박문제 전화상담 헬프라인은 국번 없이 1336번이에요. 한 번 전화해서 도움을 받아보시는 게 어떤가요?")

async def setup(bot):
    await bot.add_cog(_도박(bot))