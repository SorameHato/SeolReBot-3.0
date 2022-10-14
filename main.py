# coding: utf-8
import discord
from discord.ext import commands
import random
import sys
from datetime import datetime as dt
import Module.SeolReLib as SRLib

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

'''
봇이 반응을 해야하는 명령어인지 구분하기 위해 메세지 앞에 붙이는 접두사(prefix)를 설정합니다. 현재 !로 
설정되어있습니다. 이곳을 변경시 해당 문자로 명령어를 시작해야합니다. ext에선 discord.Client처럼 
str.startswith 메서드를 사용할 필요가 없습니다.
'''

ver = "3.0_2022101400 rev 0.0 build 10"

def 확률처리(arg):
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

def 식사추천():
    음식list = ["치킨","피자","짜장","짬뽕","볶음밥","돌솥비빔밥","떡볶이","순대","족발","보쌈","삼겹살","파스타","돈카츠","라멘","라면","스테이크","김밥","샌드위치","햄버거","한정식","불고기","초밥","우동","닭갈비","빵","마라탕","샤브샤브","탕수육","토스트","부대찌개","수제비","곰탕","설렁탕","순대국","칼국수","회","제육볶음","감자탕","청국장","물회","깐풍기","사케동","연어스테이크","쌀국수","송어회","리조또","타코야끼","카레","잔치국수","밥버거","곱창","육회","스키야키","김치찌개","된장찌개"]
    return(random.choice(음식list))

def 야식추천():
    야식list = ["치킨","피자","떡볶이","순대","족발","보쌈","라면","우동","빵","탕수육","부대찌개","회","제육볶음","타코야끼","카레","잔치국수","곱창","육회","계란말이","어묵탕","김치찌개","라멘","해장국","모둠튀김","매운새우깡","쌀새우깡","새우깡블랙","콩나물해장라면"]
    return(random.choice(야식list))

def initialDataLoad():
    currencyFile = open("currency.json",'r+')
    currencyData = currencyFile.read()

def dataSave():
    pass

@bot.event
async def on_ready():
    global LoadedTime
    LoadedTime = "{0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6}초".format(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second, int(dt.now().microsecond/1000))
    print('┌────────────────────────────────────────────────────────────┐\n│ {name}(#{id})으로 로그인되었습니다. │\n│ 봇이 시작된 시각 : {LoadedTime}     │\n└────────────────────────────────────────────────────────────┘'.format(name=bot.user.name,id=bot.user.id,LoadedTime=LoadedTime))
    # print(bot.user.name + '(#' + str(bot.user.id) + ')으로 로그인되었습니다.\n봇이 시작된 시각 : '+LoadedTime)
    # print('──────────────────────────────────────────────────────────')
'''
print(bot.user.name) # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
print(bot.user.id) # 위와 같은 클래스에서 id 프로퍼티 출력

LoadedTime은 아래의 코드를 대체하는 코드
In [8]: import datetime
In [10]: dt = datetime.datetime.now()
In [48]: LoadedTime = "{0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6}초".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, int(dt.microsecond/1000))
'''

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms') # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.

@bot.command()
async def 확률(ctx,*,text):
    await ctx.send(확률처리(text))

@bot.command()
async def 아침메뉴추천(ctx):
    await ctx.send("유설레가 추천하는 오늘의 아침 메뉴는? "+식사추천()+"입니다!\n점심, 저녁식사 메뉴를 추천하는 함수를 돌려 쓰고 있어서 아침으로 먹기에는 부담스러운 음식이 나올지도 몰라요. 양해해주세요!")

@bot.command()
async def 점심메뉴추천(ctx):
    await ctx.send("유설레가 추천하는 오늘의 점심 메뉴는? "+식사추천()+"입니다!\n저녁식사 메뉴를 추천하는 함수를 돌려 쓰고 있어서 점심으로 먹기에는 부담스러운 음식이 나올지도 몰라요. 양해해주세요!")

@bot.command()
async def 저녁메뉴추천(ctx):
    await ctx.send("유설레가 추천하는 오늘의 저녁 메뉴는? "+식사추천()+"입니다!")

@bot.command()
async def 야식메뉴추천(ctx):
    await ctx.send("유설레가 추천하는 오늘의 야식 메뉴는? "+야식추천()+"입니다!")

@bot.command()
async def 정보(ctx):
    await ctx.send("설레봇의 정보입니다!\n> 버전 : "+ver+"\n> 기반 : 2.5_2021021703 rev 6.3 build 14 (2021년 2월 18일 1시 0분 45초)\n> DB1 : PJU:K:C:B:2021103105 (2021년 10월 31일 4시 3분 51초)\n> DB2 : b102dff1ef5ddf5e3e9d7a4028656a90aa921252 (2022년 9월 21일 2시 47분 0초)\n> 봇이 시작된 시간 : " + LoadedTime)

@bot.command()
async def 열번분석(ctx,*,text):
    await ctx.send(SRLib.열번분류(text))

@bot.command()
async def 도박(ctx,*,text):
    if(text.split(' ')[0] == "회생"):
        await ctx.send("아직 데이터 확인 부분의 코드가 완성되지 않았어요. 하지만 벌써부터 회생을 하려는 걸 보니 당신은 도박 중독자이신 것 같네요.\n한국도박문제예방치유원에서 운영하는 도박문제 전화상담 헬프라인은 국번 없이 1336번이에요. 한 번 전화해서 도움을 받아보시는 게 어떤가요?")

@bot.command()
async def 셧다운(ctx):
    # dataSave()
    await ctx.send("설레봇을 종료합니다. 반드시 설레봇이 종료된 후 anaconda를 종료하고 Windows Terminal 창을 닫아주세요.")
    sys.exit()

bot.run(open("token.txt","r").readline())