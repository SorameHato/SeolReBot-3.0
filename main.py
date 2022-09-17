import discord
from discord.ext import commands
import random

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
        jujak_list = ["단비냐아가 천사일", "단비냐아가 여신일", "단비가 천사일", "단비가 여신일", "아메가 천사일", "아메가 여신일", "아메냐아가 천사일", "아메냐아가 여신일", "아메냥이 천사일", "아메냥이 여신일", "단비냥이 천사일", "단비냥이 여신일", "메냥이가 천사일", "메냥이가 여신일", "국왕님이 천사일", "국왕님이 여신일", "바기가 인싸일", "바기냥이 인싸일", "바기챤이 인싸일", "바기짱이 인싸일"]
        for i in range(len(jujak_list)):
            if(arg==jujak_list[i]):
                jujak=True
    return("{arg} 확률은 {rnd}%입니다.".format(arg=arg,rnd=random.randint(0,100) if jujak==False else 100))

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

bot.run(open("token.txt","r").readline())