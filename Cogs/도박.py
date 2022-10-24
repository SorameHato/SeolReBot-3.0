# coding: utf-8
import discord
from discord.ext import commands as bot
import pickle
import random
import csv
from datetime import datetime as dt

# 시드값 : seed.pickle
# 데이터베이스 : data.pickle (2차원 배열)
# 0 : 유저ID, 1 : 소지금, 2 : 마지막으로 회생한 날짜
# 확인용 각 시드가 나온 횟수 : seedtimes.pickle

class c도박(bot.Cog):
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
                if line[0] == str(uid):
                    exist = True
                    with open('log.txt','a',encoding='utf-8') as b:
                        b.write('{}\t{}\t조회\t소지금 : {}\n'.format(dt.now(),uid,line[1]))
                    try:
                        return int(line[1])
                    except(ValueError):
                        return -3
        # .설레 도박 조회 명령어에서는 -1값이 반환되면 자동으로 db추가를 진행하는 기능을 추가해야 함
        # 이 외의 경우에는 그냥 데이터가 없다고만 출력
        if exist == False:
            with open('log.txt','a',encoding='utf-8') as b:
                b.write('{}\t{}\t조회\t잔액 : 데이터 없음\n'.format(dt.now(),uid))
            return -1
     
    '''해당 유저의 잔고를 변경하는 명령어
    input : uid (ctx.message.author.id 로 얻은 해당 유저의 id)
    amount (얼마나 변경할 것인지, 주의해야 할 점은 잔액을 인출하는 경우 음수로 입력해야 함, 그리고 절댓값을 입력하는 게 아님. 26만원에서 25만 5천원으로 변경하고 싶으면 255000이 아닌 -5000으로 입력해야 함)
    output : 인출/입금 후 잔액 (단, 해당 유저의 데이터가 없는 경우 -1, 잔고가 부족한 경우 -2)'''
    def 변경(self,uid,amount):
        db = list()
        amount = int(amount)
        status = -1
        with open('data.csv','r',newline='',encoding='utf-8') as a:
            reader = csv.reader(a)
            for line in reader:
                if line[0] == str(uid):
                    if int(line[1]) + amount >= 0:
                        line[1] = int(line[1]) + amount
                        ret = line[1]
                        with open('log.txt','a',encoding='utf-8') as b:
                            b.write('{}\t{}\t변경\t소지금 : {} → {} (amount : {})\n'.format(dt.now(),uid,ret-amount,ret,amount))
                        status = 1
                    else:
                        with open('log.txt','a',encoding='utf-8') as b:
                            b.write('{}\t{}\t변경\t소지금 : {} → (잔고 부족으로 인한 변경 실패, amount : {})\n'.format(dt.now(),uid,line[1],amount))
                        status = -2
                db.append(line)
        if status == 1:
            with open('data.csv','w',newline='',encoding='utf-8') as a:
                writer = csv.writer(a)
                writer.writerows(db)
            with open('log.txt','a',encoding='utf-8') as b:
                b.write('{}\t{}\t변경\t데이터 기록 완료\n'.format(dt.now(),uid))
            return ret
        else:
            return status
     
    def 잭팟뽑기(self):
        with open('seed_basic.pickle','rb') as a:
            seed = pickle.load(a)
            return random.choice(seed)
     
    def 잭팟(self, uid, amount):
        a = self.조회(uid)
        if a < 0:
            return -1
        else:
            if a < amount:
                return -2
            else:
                결과 = self.잭팟뽑기()
                with open('log.txt','a',encoding='utf-8') as b:
                    b.write('{}\t{}\t룰렛\t결과 : {}, amount : {}\n'.format(dt.now(),uid,결과,amount))
                #todo : 결과별로 코드 표 참고해서 embed로 결과 만들기, 배율 해서 잔액에 결과값 더하기 (배율은 표에 나와있는 배율 - 1.0으로 해야 함)
                if 결과 == 46:
                    embed = discord.Embed(title='아쉽게도 본전이에요.', color=0xccffff)
                    embed.add_field(name='배율',value='x1',inline=True)
                    embed.add_field(name='확률',value='35.5537%',inline=True)
                    embed.add_field(name='소지금',value=a,inline=False)
                    embed.set_footer(text='설레봇 룰렛 | code = {}'.format(결과))
                elif 결과 == 55:
                    b = self.변경(uid,0-amount)
                    embed = discord.Embed(title='꽝이에요... 정말 운이 없었네요...', color=0xccffff)
                    embed.add_field(name='배율',value='x0',inline=True)
                    embed.add_field(name='확률',value='9.9989%',inline=True)
                    embed.add_field(name='소지금',value=b,inline=False)
                    embed.set_footer(text='설레봇 룰렛 | code = {}'.format(결과))
                elif 결과>=20 and 결과<=45:
                    배율목록=[5.73,5.2,4.86,4.28,3.71,3.29,2.52,2.06,1.95,1.87,1.79,1.71,1.64,1.52,1.46,1.4,1.34,1.28,1.23,1.18,1.14,1.1,1.07,1.05,1.03,1.02]
                    배율 = 배율목록[결과-20]
                    b = self.변경(uid,amount*(배율-1))
                    embed = discord.Embed(title='Lucky! 축하드려요! 이득이에요!', color=0xccffff)
                    embed.add_field(name='배율',value='x{}'.format(배율),inline=True)
                    embed.add_field(name='확률',value='2.2508%' if 배율<1.2 else '1.3636%' if 배율<2 else '0.3138%',inline=True)
                    embed.add_field(name='소지금',value=b,inline=False)
                    embed.set_footer(text='설레봇 룰렛 | code = {}'.format(결과))
                elif 결과>=47 and 결과<=54:
                    배율목록=[0.98,0.92,0.84,0.72,0.6,0.4,0.15,0.1]
                    배율 = 배율목록[결과-47]
                    b = self.변경(uid,amount*(배율-1))
                    embed = discord.Embed(title='운이 없었네요...', color=0xccffff)
                    embed.add_field(name='배율',value='x{}'.format(배율),inline=True)
                    embed.add_field(name='확률',value='2.3079%' if 배율<0.7 else '2.8385%',inline=True)
                    embed.add_field(name='소지금',value=b,inline=False)
                    embed.set_footer(text='설레봇 룰렛 | code = {}'.format(결과))
                else:
                    embed = discord.Embed(title='처리 중 오류가 발생했어요!',description='하늘토끼의 귀챠니즘으로 6배율 이상(확률 약 0.6%)은 수동으로 처리하도록 코드를 짰어요. 죄송하지만 하늘토끼를 불러주시겠어요?',color=0xfae5fa)
                    embed.add_field(name='결과',value=결과,inline=True)
                    embed.set_footer(text='설레봇 룰렛 | code = {}'.format(결과))
                    print('{} 현재 룰렛 6배 이상 발생!'.format(dt.now()))
                return embed
     
    @bot.command()
    async def 도박(self,ctx,*,text='조회'):
        메뉴 = text.split(' ')[0]
        if 메뉴 == '룰렛' :
            try:
                amount = int(text.split(' ')[1])
            except(ValueError):
                print('오류 발생 | 보낸 사람 : {}, 내용 : {}, 오류 : {}'.format(ctx.message.author,ctx.message.content,error))
                embed = discord.Embed(title='자세한 내용',description='{}: 룰렛에 베팅할 금액이 정상적으로 입력되지 않았어요. 금액은 숫자로만 입력해주세요!'.format(error),color=0xfae5fa)
                embed.add_field(name="보낸 분",value=ctx.message.author,inline=False)
                embed.add_field(name="보낸 내용",value=ctx.message.content,inline=False)
                embed.set_footer(text='설레봇 버전 {}'.format(ver))
                await ctx.send('오류가 발생했어요!',embed=embed)
            else:
                if amount % 100 == 0:
                    embed1 = self.잭팟(ctx.message.author.id,amount)
                    if embed1 == -1:
                        embed2 = discord.Embed(title='처리 중 오류가 발생했어요!',description='{}님의 데이터가 존재하지 않아요.'.format(ctx.message.author),color=0xfae5fa)
                        embed2.set_footer(text='설레봇 룰렛 | code = {}'.format(embed1))
                    elif embed1 == -2:
                        embed2 = discord.Embed(title='처리 중 오류가 발생했어요!',description='소지금이 부족해요.',color=0xfae5fa)
                        embed2.add_field(name='요청한 금액',value=text.split(' ')[1],inline=True)
                        embed2.add_field(name='소지금',value=조회(ctx.message.author.id),inline=True)
                        embed2.set_footer(text='설레봇 룰렛 | code = {}'.format(embed1))
                        await ctx.send('돈이 부족해요!',embed=embed2)
                    else:
                        await ctx.send('룰렛의 결과에요!\n> 소지금이 음수로 표시되는 경우 진짜로 잔액이 마이너스가 된 게 아니라 오류로 룰렛의 결과가 반영이 되지 않은 경우에요. 이 경우, 하늘토끼를 호출해주시면 반영해드릴게요.',embed=embed1)
                else:
                    await ctx.send('float형의 데이터가 불안정한 문제가 있어 모든 데이터를 int형으로 처리하기 위해 도박 기능을 100원 단위로만 쓸 수 있게 제한중이에요. 금액을 100원 단위로 입력해주세요!')
        elif 메뉴 == '조회':
            잔액 = self.조회(ctx.message.author.id)
            if 잔액 >= 0:
                embed = discord.Embed(title='조회 결과에요!', color=0xccffff)
                embed.add_field(name='닉네임',value=ctx.message.author,inline=True)
                embed.add_field(name='소지금',value=잔액,inline=True)
                #마지막 회생일 추가
                embed.set_footer(text='설레봇 룰렛')
                await ctx.send(embed=embed)
            elif 잔액 == -1:
                embed2 = discord.Embed(title='처리 중 오류가 발생했어요!',description='{}님의 데이터가 존재하지 않아요.'.format(ctx.message.author),color=0xfae5fa)
                embed2.set_footer(text='설레봇 룰렛 | code = -1')
                await ctx.send('자동 등록 기능은 구현이 어려울 것 같아요. 도박 기능을 이용하시려면 하늘토끼를 불러주세요!',embed=embed2) #데이터 초기화(추가)
            else:
                embed = discord.Embed(title='처리 중 오류가 발생했어요!',description='데이터가 올바르게 읽히지 않았어요. csv 파일을 직접 수정해야 해요. 하늘토끼를 불러주세요.',color=0xfae5fa)
                embed.add_field(name='소지금',value=잔액,inline=False)
                embed.set_footer(text='설레봇 룰렛 | code = {}'.format(잔액))
                await ctx.send(embed=embed)
        elif(메뉴 == "회생"):
            await ctx.send("아쉽게도 자동 회생 기능은 지금의 하늘토끼의 기술로는 구현하기 힘들다는 결론이 났어요. 2학년 때 고급파이썬을 배우면 구현해볼게요. 일단은 하늘토끼를 불러주세요.\n추가로, 한 가지 유용한 정보를 드릴게요. 한국도박문제예방치유원에서 운영하는 도박문제 전화상담 헬프라인은 국번 없이 1336번이에요. 한 번 전화해서 도움을 받아보시는 게 어떤가요?")
        elif 메뉴 == '임베드':
            try:
                amount = int(text.split(' ')[1])
            except(ValueError):
                print('오류 발생 | 보낸 사람 : {}, 내용 : {}, 오류 : {}'.format(ctx.message.author,ctx.message.content,error))
                embed = discord.Embed(title='자세한 내용',description='{}: 임베드 종류가 제대로 입력되지 않았어요. 하토님, 데이터 변경은 수동으로 해야 하는 거 아시죠? 현타가 오면 이 노래를 듣고 온 뒤에 작업하세요.\nhttps://youtu.be/eIX_wA-ZZH4'.format(error),color=0xfae5fa)
                embed.add_field(name="보낸 분",value=ctx.message.author,inline=False)
                embed.add_field(name="보낸 내용",value=ctx.message.content,inline=False)
                embed.set_footer(text='설레봇 버전 {}'.format(ver))
                await ctx.send('오류가 발생했어요!',embed=embed)
            else:
                if amount == 0:
                    embed = discord.Embed(title='777 A Lot Huge Lucky! 잭팟이 터졌어요! 무려 5572배에요!',description='운이 엄청 좋은 당신을 코코나츠가 같이 축하드려요. (코코나츠 페이스북 사용자명 coconatsu__5572__)',color=0xffd07b)
                    embed.add_field(name='배율',value='x5572',inline=True)
                    embed.add_field(name='확률',value='0.0029%',inline=True)
                    embed.set_image(url='https://pbs.twimg.com/media/EQAknWIUEAIsnZS?format=png&name=900x900')
                elif amount == 1:
                    embed = discord.Embed(title='777 Huge Lucky! 잭팟이 터졌어요! 1000배에요!',description='운이 엄청 좋은 당신을 미즈하라 치즈루가 같이 축하드려요. (이치노세 치즈루의 이름의 어원 __센__바즈루)',color=0xffd07b)
                    embed.add_field(name='배율',value='x1000',inline=True)
                    embed.add_field(name='확률',value='0.0057%',inline=True)
                    embed.set_image(url='https://pbs.twimg.com/media/FfxUJ5xUoAAtFrz?format=jpg&name=large')
                elif amount == 2:
                    embed = discord.Embed(title='777 Lucky! 잭팟이 터졌어요! 505배에요!',description='운이 엄청 좋은 당신을 나카노 이츠키가 같이 축하드려요. (이츠키의 생일 5월 5일)',color=0xffd07b)
                    embed.add_field(name='배율',value='x505',inline=True)
                    embed.add_field(name='확률',value='0.0057%',inline=True)
                    embed.set_image(url='https://pbs.twimg.com/media/Ff2li4AVsAAgX0r?format=jpg&name=large')
                elif amount == 3:
                    embed = discord.Embed(title='777 Lucky! 잭팟이 터졌어요! 428배에요!',description='운이 엄청 좋은 당신을 나카노 요츠바가 같이 축하드려요. (요츠바의 고로아와세 428)',color=0xffd07b)
                    embed.add_field(name='배율',value='x428',inline=True)
                    embed.add_field(name='확률',value='0.0057%',inline=True)
                    embed.set_image(url='https://pbs.twimg.com/media/Ff2lk-YUoAA5syI?format=jpg&name=large')
                elif amount == 4:
                    embed = discord.Embed(title='777 Lucky! 잭팟이 터졌어요! 390배에요!',description='운이 엄청 좋은 당신을 나카노 미쿠가 같이 축하드려요. (미쿠의 고로아와세 39 × 10)',color=0xffd07b)
                    embed.add_field(name='배율',value='x390',inline=True)
                    embed.add_field(name='확률',value='0.0057%',inline=True)
                    embed.set_image(url='https://pbs.twimg.com/media/FfxgC7vUcAASYYo?format=jpg&name=large')
                elif amount == 7:
                    embed = discord.Embed(title='777 Lucky! 잭팟이 터졌어요! 200배에요!',description='운이 엄청 좋은 당신을 나카노 니노가 같이 축하드려요. (다섯 쌍둥이 중 둘째라 200)',color=0xffd07b)
                    embed.add_field(name='배율',value='x200',inline=True)
                    embed.add_field(name='확률',value='0.0057%',inline=True)
                    embed.set_image(url='https://pbs.twimg.com/media/Ff2m7pLVUAAkwWb?format=jpg&name=large')
                elif amount == 8:
                    embed = discord.Embed(title='777 Lucky! 잭팟이 터졌어요! 187배에요!',description='운이 엄청 좋은 당신을 나카노 이치카가 같이 축하드려요. (이치카 > 一花 > 이치하나로도 읽을 수 있음 > 고로아와세로 187)',color=0xffd07b)
                    embed.add_field(name='배율',value='x187',inline=True)
                    embed.add_field(name='확률',value='0.0057%',inline=True)
                    embed.set_image(url='https://pbs.twimg.com/media/Ff2lhEnUYAAK0Bx?format=jpg&name=large')
                embed.add_field(name='소지금',value='하늘토끼가 수동으로 계산할 예정입니다.',inline=False)
                embed.set_footer(text='설레봇 룰렛 | code = {}'.format(amount))
                await ctx.send('하토님, 소지금 수동으로 처리하는 거 잊지 마세요!',embed=embed)

async def setup(bot):
    await bot.add_cog(c도박(bot))