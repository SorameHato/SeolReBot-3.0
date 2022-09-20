# coding: utf-8
import discord
from discord.ext import commands
import random
import sys

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

'''
봇이 반응을 해야하는 명령어인지 구분하기 위해 메세지 앞에 붙이는 접두사(prefix)를 설정합니다. 현재 !로 
설정되어있습니다. 이곳을 변경시 해당 문자로 명령어를 시작해야합니다. ext에선 discord.Client처럼 
str.startswith 메서드를 사용할 필요가 없습니다.
'''

def 확률처리(arg,jujakApply):
    jujak = False
    # arg문 정제(?)
    if(arg[len(arg)-2:len(arg)] == '확률'):
        arg = arg[0:len(arg)-2]
    if(arg[len(arg)-3:len(arg)] == '가능성'):
        arg = arg[0:len(arg)-3]
    if(arg[len(arg)-1:len(arg)] == ' '):
        arg = arg[0:len(arg)-1]
    if(jujakApply == True):
        #for문을 이용해 arg가 예외처리할 문장과 일치하는지 하나하나 확인, 일치하면 jujak=True
        jujak_list = ["단비냐아가 천사일", "단비냐아가 여신일", "단비가 천사일", "단비가 여신일", "아메가 천사일", "아메가 여신일", "아메냐아가 천사일", "아메냐아가 여신일", "아메냥이 천사일", "아메냥이 여신일", "단비냥이 천사일", "단비냥이 여신일", "메냥이가 천사일", "메냥이가 여신일", "국왕님이 천사일", "국왕님이 여신일", "바기가 인싸일", "바기냥이 인싸일", "바기챤이 인싸일", "바기짱이 인싸일", "아메님이 천사일", "아메님이 여신일", "아메냥님이 천사일", "아메냥님이 여신일", "<@405716868251385866> 가 천사일", "<@405716868251385866> 가 여신일", "<@405716868251385866>가 천사일", "<@405716868251385866>가 여신일", "<@405716868251385866> 이 천사일", "<@405716868251385866> 이 여신일", "<@405716868251385866>이 천사일", "<@405716868251385866>이 여신일", "<@405716868251385866> 님이 천사일", "<@405716868251385866> 님이 여신일", "<@405716868251385866>님이 천사일", "<@405716868251385866>님이 여신일", "단비냐아가 천재일", "단비가 천재일", "아메가 천재일", "아메냐아가 천재일", "아메냥이 천재일", "단비냥이 천재일", "메냥이가 천재일", "국왕님이 천재일", "아메님이 천재일", "아메냥님이 천재일", "<@405716868251385866> 가 천재일", "<@405716868251385866>가 천재일", "<@405716868251385866> 이 천재일", "<@405716868251385866>이 천재일", "<@405716868251385866> 님이 천재일", "<@405716868251385866>님이 천재일","단비냐아가 아이돌일", "단비가 아이돌일", "아메가 아이돌일", "아메냐아가 아이돌일", "아메냥이 아이돌일", "단비냥이 아이돌일", "메냥이가 아이돌일", "국왕님이 아이돌일", "아메님이 아이돌일", "아메냥님이 아이돌일", "<@405716868251385866> 가 아이돌일", "<@405716868251385866>가 아이돌일", "<@405716868251385866> 이 아이돌일", "<@405716868251385866>이 아이돌일", "<@405716868251385866> 님이 아이돌일", "<@405716868251385866>님이 아이돌일", "단비냐아가 넷아이돌일", "단비가 넷아이돌일", "아메가 넷아이돌일", "아메냐아가 넷아이돌일", "아메냥이 넷아이돌일", "단비냥이 넷아이돌일", "메냥이가 넷아이돌일", "국왕님이 넷아이돌일", "아메님이 넷아이돌일", "아메냥님이 넷아이돌일", "<@405716868251385866> 가 넷아이돌일", "<@405716868251385866>가 넷아이돌일", "<@405716868251385866> 이 넷아이돌일", "<@405716868251385866>이 넷아이돌일", "<@405716868251385866> 님이 넷아이돌일", "<@405716868251385866>님이 넷아이돌일", "단비냐아가 귀여울", "단비가 귀여울", "아메가 귀여울", "아메냐아가 귀여울", "아메냥이 귀여울", "단비냥이 귀여울", "메냥이가 귀여울", "국왕님이 귀여울", "아메님이 귀여울", "아메냥님이 귀여울", "<@405716868251385866> 가 귀여울", "<@405716868251385866>가 귀여울", "<@405716868251385866> 이 귀여울", "<@405716868251385866>이 귀여울", "<@405716868251385866> 님이 귀여울", "<@405716868251385866>님이 귀여울", "단비냐아가 무적급으로 귀여울", "단비가 무적급으로 귀여울", "아메가 무적급으로 귀여울", "아메냐아가 무적급으로 귀여울", "아메냥이 무적급으로 귀여울", "단비냥이 무적급으로 귀여울", "메냥이가 무적급으로 귀여울", "국왕님이 무적급으로 귀여울", "아메님이 무적급으로 귀여울", "아메냥님이 무적급으로 귀여울", "<@405716868251385866> 가 무적급으로 귀여울", "<@405716868251385866>가 무적급으로 귀여울", "<@405716868251385866> 이 무적급으로 귀여울", "<@405716868251385866>이 무적급으로 귀여울", "<@405716868251385866> 님이 무적급으로 귀여울", "<@405716868251385866>님이 무적급으로 귀여울", "단비냐아가 세상에서 제일 귀여울", "단비가 세상에서 제일 귀여울", "아메가 세상에서 제일 귀여울", "아메냐아가 세상에서 제일 귀여울", "아메냥이 세상에서 제일 귀여울", "단비냥이 세상에서 제일 귀여울", "메냥이가 세상에서 제일 귀여울", "국왕님이 세상에서 제일 귀여울", "아메님이 세상에서 제일 귀여울", "아메냥님이 세상에서 제일 귀여울", "<@405716868251385866> 가 세상에서 제일 귀여울", "<@405716868251385866>가 세상에서 제일 귀여울", "<@405716868251385866> 이 세상에서 제일 귀여울", "<@405716868251385866>이 세상에서 제일 귀여울", "<@405716868251385866> 님이 세상에서 제일 귀여울", "<@405716868251385866>님이 세상에서 제일 귀여울", "단비냐아가 텐시일", "단비가 텐시일", "아메가 텐시일", "아메냐아가 텐시일", "아메냥이 텐시일", "단비냥이 텐시일", "메냥이가 텐시일", "국왕님이 텐시일", "아메님이 텐시일", "아메냥님이 텐시일", "<@405716868251385866> 가 텐시일", "<@405716868251385866>가 텐시일", "<@405716868251385866> 이 텐시일", "<@405716868251385866>이 텐시일", "<@405716868251385866> 님이 텐시일", "<@405716868251385866>님이 텐시일", "메냥님이 천사일", "메냥님이 여신일", "메냥님이 텐시일", "메냥님이 세상에서 제일 귀여울", "메냥님이 귀여울", "메냥님이 무적급으로 귀여울", "메냥님이 넷아이돌일", "메냥님이 아이돌일", "메냥님이 천재일"]
        for i in range(len(jujak_list)):
            if(arg==jujak_list[i]):
                jujak=True
    return("{arg} 확률은 {rnd}%입니다.".format(arg=arg,rnd=random.randint(0,100) if jujak==False else 100))

def 식사추천():
    음식list = ["치킨","피자","짜장","짬뽕","볶음밥","돌솥비빔밥","떡볶이","순대","족발","보쌈","삼겹살","파스타","돈카츠","라멘","라면","스테이크","김밥","샌드위치","햄버거","한정식","불고기","초밥","우동","닭갈비","빵","마라탕","샤브샤브","탕수육","토스트","부대찌개","수제비","곰탕","설렁탕","순대국","칼국수","회","제육볶음","감자탕","청국장","물회","깐풍기","사케동","연어스테이크","쌀국수","송어회","리조또","타코야끼","카레","잔치국수","밥버거","곱창","육회","스키야키","김치찌개","된장찌개"]
    return(random.choice(음식list))

def 야식추천():
    야식list = ["치킨","피자","떡볶이","순대","족발","보쌈","라면","우동","빵","탕수육","부대찌개","회","제육볶음","타코야끼","카레","잔치국수","곱창","육회","계란말이","어묵탕","김치찌개","라멘","해장국","모둠튀김","매운새우깡","쌀새우깡","새우깡블랙","콩나물해장라면"]
    return(random.choice(야식list))

def initial_data_load():
    currencyFile = open("currency.json",'r+')
    currencyData = currencyFile.read()

def data_save():
    pass

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name) # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
    print(bot.user.id) # 위와 같은 클래스에서 id 프로퍼티 출력
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms') # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.

@bot.command(name="1234")
async def _1234(ctx):
    await ctx.send("5678")
#파이썬 문법에 따라 함수를 만들 때에는 첫글자에는 숫자를 넣을 수 없는데, 숫자를 사용하고싶다면 함수 이름 자리는 다른 아무것으로 대체하고 괄호 안에 name=""을 사용하여 명령어를 제작할 수 있다.

@bot.command()
async def 확률(ctx,*,text):
    if(text[0:3] == "주작X"):
        await ctx.send(확률처리(text[3:len(text)], False))
    else:
        await ctx.send(확률처리(text,True))

@bot.command()
async def 테스트(ctx):
    await ctx.send("입국 심사 : <#1019793951642898522>, 신원 확인 : <#1019801276004974643>")
    
@bot.command()
async def 물기(ctx, *, text):
    await ctx.send("'" + text + "'을(를) 물... 거라고 생각하셨으면 오산입니다. 저는 매우 착하기 때문이죠.\n - 개발자 하늘토끼")

@bot.command()
async def 물어뜯기(ctx, *, text):
    await ctx.send("'" + text + "'을(를) 물어뜯을... 게 아니라 님부터 물어뜯어야겠어요. 콱!\n - 개발자 하늘토끼")

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

# @bot.command()
# async def 사볼곡추천(ctx):
    # await ctx.send("고릴라가 있다 INF (15렙) 어떠신가요?")

@bot.command()
async def 하늘토끼괴롭히기(ctx):
    await ctx.send("공론화해드릴까요..? 일단 스카이웨어 포털 http://swa.re.kr (구축 예정) 으로 좀 오시죠\n- 개발자 하늘토끼")
    
@bot.command()
async def 괴롭히기(ctx):
    await ctx.send("공론화해드릴까요..? 일단 스카이웨어 포털 http://swa.re.kr (구축 예정) 으로 좀 오시죠\n- 개발자 하늘토끼")
    
@bot.command()
async def 이지매하기(ctx):
    await ctx.send("공론화해드릴까요..? 일단 스카이웨어 포털 http://swa.re.kr (구축 예정) 으로 좀 오시죠\n- 개발자 하늘토끼")

@bot.command()
async def 도박(ctx,*,text):
    if(text.split(' ')[0] == "회생"):
        await ctx.send("아직 데이터 확인 부분의 코드가 완성되지 않았어요. 하지만 벌써부터 회생을 하려는 걸 보니 당신은 도박 중독자이신 것 같네요.\n한국도박문제예방치유원에서 운영하는 도박문제 전화상담 헬프라인은 국번 없이 1336번이에요. 한 번 전화해서 도움을 받아보시는 게 어떤가요?")

@bot.command()
async def 셧다운(ctx):
    await ctx.send("설레봇을 종료합니다. 반드시 설레봇이 종료된 후 anaconda를 종료하고 Windows Terminal 창을 닫아주세요.")
    sys.exit()

bot.run(open("token.txt","r").readline())