# coding: utf-8
import discord
from discord.ext import commands
import random
import sys
from datetime import datetime as dt

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.설레 ', intents=intents)

'''
봇이 반응을 해야하는 명령어인지 구분하기 위해 메세지 앞에 붙이는 접두사(prefix)를 설정합니다. 현재 !로 
설정되어있습니다. 이곳을 변경시 해당 문자로 명령어를 시작해야합니다. ext에선 discord.Client처럼 
str.startswith 메서드를 사용할 필요가 없습니다.
'''

ver = "3.0_2022101901 rev 0.0 build 17"

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

def 시간사담(hour,minute):
    tcode = hour * 60 + minute
    if(tcode <= 30 or tcode > 1380):
        return('슬슬 잘 준비를 해야 할 시간이네요! 저는 오늘 야간 운행이라 못 자지만요. 하암...')
    elif(tcode > 30 and tcode <= 330):
        return('엣, 이렇게 늦었는데 아직도 안 주무시고 계신가요? 얼른 주무세요!')
    elif(tcode > 330 and tcode <= 540):
        return('좋은 아침이에요! 오늘 하루도 설빈레피딕스 열차를 타고 기분 좋게, 상쾌하게 시작해요!')
    elif(tcode > 540 and tcode <= 660):
        return('하늘이 참 맑죠? 하늘민국은 강수량이 적고 그마저도 겨울에 폭설로 내리는 게 대부분이라 이렇게 맨날 하늘이 파랗고 맑아요. 이 푸른 하늘을 보면서, 힘내서 열심히 일해요!')
    elif(tcode > 660 and tcode <= 780):
        return('슬슬 점심시간이네요. 배고파요...')
    elif(tcode > 780 and tcode <= 960):
        return('점심은 맛있게 드셨나요? 배가 불러서 졸리겠지만 같이 힘내요!')
    elif(tcode > 960 and tcode <= 1080):
        return('조금만 더 일하면 퇴근이에요. 화이팅이에요!')
    elif(tcode > 1080 and tcode <= 1260):
        return('해도 졌겠다, 가벼운 산책 어때요? 전 비번인 날에는 매일 저녁 먹고 나와서 북해 해안가 산책로를 산책해요. 바닷바람도 상쾌하고 기분이 좋거든요.\n아, 그리고 신종 코로나 바이러스 때문에 수도권은 21시 이후로는 아무것도 못 한다면서요? 뭔가 일이 있으면 빨리 나가는 게 좋을 것 같아요.')
    elif(tcode > 1260 and tcode <= 1380):
        return('이제 완전히 밤이네요. 이 시간에는 평소에 하지 못 했던 취미생활을 해 보는 게 어떨까요?')
    else:
        return('오류가 발생해 사담을 처리하지 못했어요. 명령어를 처리하는 도중에 각 시 59분 59초가 지나면 드물게 발생할 수 있는 오류니까, 다시 한 번 시도해주세요!')

def initialDataLoad():
    currencyFile = open("currency.json",'r+')
    currencyData = currencyFile.read()

def dataSave():
    pass

@bot.event
async def on_ready():
    global LoadedTime
    LoadedTime = "{0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초".format(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second, int(dt.now().microsecond/1000))
    print('┌────────────────────────────────────────────────────────┐\n│   {name}(#{id})으로 로그인되었습니다.    │\n│ 봇이 시작된 시각 : {LoadedTime} │\n└────────────────────────────────────────────────────────┘'.format(name=bot.user.name,id=bot.user.id,LoadedTime=LoadedTime))
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
    await ctx.send("설레봇의 정보입니다!\n> 버전 : "+ver+"\n> 기반 : 2.5_2021021703 rev 6.3 build 14 (2021년 2월 18일 1시 0분 45초)\n> DB1 : PJU:K:C:B:2021103105 (2021년 10월 31일 4시 3분 51초)\n> DB2 : b102dff1ef5ddf5e3e9d7a4028656a90aa921252 (2022년 9월 21일 2시 47분 0초)\n> 설레봇을 개발한 사람 : 하늘토끼(ghwls030306@s-r.ze.am)\n> 설레봇이 시작된 시간 : " + LoadedTime)


@bot.command()
async def 시간(ctx):
    await ctx.send('삐, 삐, 삐! 당신의 설레임과 함께, 설빈레피딕스에서 {0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초를 알려드립니다.\n{7}\n이 사담은 2020년 9월 경 설레봇을 \'신 교통동호인 채팅방\'에서 돌릴 때 작성되었어요. 하늘토끼의 가상국가/가상철도 세계관과 관련되어 있거나 지금과는 맞지 않는 내용이 있을 수 있으니 양해 부탁드려요!'.format(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second, int(dt.now().microsecond/1000),시간사담(dt.now().hour,dt.now().minute)))

# @bot.command()
# async def 시간사담테스트(ctx,*,text):
    # await ctx.send('테스트 결과\n{}'.format(시간사담(int(text.split(' ')[0]),int(text.split(' ')[1]))))

@bot.command()
async def 도박(ctx,*,text):
    if(text.split(' ')[0] == "회생"):
        await ctx.send("아직 데이터 확인 부분의 코드가 완성되지 않았어요. 하지만 벌써부터 회생을 하려는 걸 보니 당신은 도박 중독자이신 것 같네요.\n한국도박문제예방치유원에서 운영하는 도박문제 전화상담 헬프라인은 국번 없이 1336번이에요. 한 번 전화해서 도움을 받아보시는 게 어떤가요?")

@bot.command()
async def 테스트(ctx):
    await ctx.send('테스트 결과입니다!\n> 보낸 사람 : {0}\n> 보낸 사람의 닉네임 : {1}\n> 보낸 사람의 ID : {2}\n> 보낸 사람을 멘션할 경우 : <@{2}>'.format(ctx.message.author, ctx.message.author.name, ctx.message.author.id))

@bot.command()
async def 도움말(ctx,*,text='0'):
    num = text.split(' ')[0]
    if(num == '1' or num == '0' or num == ''):
        await ctx.send('설레봇의 명령어 목록입니다!(1/3)\n\n.설레 도움말 [페이지]\n> 명령어 목록을 볼 수 있는 명령어에요! 지금 쓰고 있는 명령어에요.\n.설레 확률 [문장]\n> 어떤 것에 대한 확률을 구할 수 있는 명령어에요. 흔히들 \'확률봇\'이라고 많이 부르는 것 같아요!\n.설레 아침메뉴추천 | .설레 점심메뉴추천 | .설레 저녁메뉴추천 | .설레 야식메뉴추천\n> 설레봇이 랜덤으로 아침/점심/저녁/야식으로 무엇을 먹을 지 추천해주는 명령어에요!')
    elif(num == '2'):
        await ctx.send('설레봇의 명령어 목록입니다!(2/3)\n\n.설레 열번분석 [다이어그램]\n> 가상 철도회사 설빈레피딕스의 다이어그램 번호를 분석할 수 있는 명령어에요.\n> 아메카제, 쿠로카제, S특급 세레나데 닛소라, 슈퍼 라이너 스카이 같이 메구로 철도선에 직결하거나 메구로 철도선에서 직결해 들어오는 열차는 메구로 철도선의 다이어그램(1031R)이 아닌 설빈레피딕스에서 부여한 다이어그램(SMLN21031)을 입력해야 하는 점 유의해주세요!\n.설레 시간\n> 설레봇이 간단한 사담과 함께 시간을 알려주는 명령어에요. 사담은 2021년 2월의 사담 데이터 그대로라 지금과 맞지 않는 내용이 있을 수 있으니까, 양해 부탁드려요!\n> 또한 시간은 하늘토끼의 컴퓨터 시계를 기준으로 표시돼요. KRISS 한국표준과학연구원 표준시계서버와 매일 동기화를 한다고는 하는데도 맨날 2초씩 3초씩 차이가 나니까, 시간이 조금 틀려도 양해 부탁드려요.\n.설레 정보\n> 설레봇의 정보를 볼 수 있어요! 설레봇의 버전, 봇이 시작된 시간 등을 볼 수 있어요.')
    elif(num == '3'):
        await ctx.send('설레봇의 명령어 목록입니다!(3/3)\n이 페이지는 도박 명령어만 다루는 특별 페이지에요. 아쉽게도 도박 기능은 아직 구현 중이에요. 데이터베이스를 다루는 방법을 배우고 있고, 최대한 재미있게 만드는 방법을 고민하고 있거든요. 많은 기대 부탁드릴게요!\n.설레 도박 회생\n> 돈을 모두 탕진하신 경우, 1주일에 한 번 회생할 수 있어요.\n> 설레봇은 개인회생을 해도 딱히 불이익이 없긴 하지만, 돈이 만원으로 초기화되고 추후 여러가지 불이익을 구현할 예정이니 남용은 하지 말아주세요!')
    else:
        await ctx.send('아직 존재하지 않는 페이지를 입력하셨어요. 설레봇은 2020년 5월에 만들어진 따끈따끈한 봇이라 아직 기능이 그렇게 많지는 않답니다. 앞으로 더 발전할 설레봇을 기대해주세요!')

@bot.command()
async def 열번분석(ctx,*,text):
    arg=text
    if arg[0:2]=='SM' and len(arg) == 9: #설빈레피딕스 도시철도 열차
        종류=0 #기본값
        노선명='존재하지 않는 노선입니다.'                        #노선/등급/라이너 정보가 오류로 인해
        등급명='존재하지 않는 등급입니다.'                        #지정되지 않을 경우를 대비해
        라이너명='존재하지 않는 라이너 열차입니다.'               #미리 값을 지정해 놓음
        라이너종류='존재하지 않는 열번이므로 알 수 없습니다.'     #이러면 오류는 안 뜨겠지
        열차번호=1048576                                          #얘는 사실 처리가 귀찮아서 콜록
        
        등급=arg[2:4] #SM'OL'21031
        등급분류=[['OR',1,'일반'],['SW',1,'일반쾌속'],['PW',1,'선별쾌속'],['RP',1,'일반급행'],['CM',1,'통근급행'],['LM',1,'쾌속급행'],['XC',1,'특별급행'],['EX',1,'고속급행'],['LN',2,'라이너']] #등급 분류 데이터
        for i in range(len(등급분류)):
            if(등급==등급분류[i][0]):
                종류=등급분류[i][1] #도시철도 열차는 1, 라이너는 2
                등급명=등급분류[i][2] #등급명
        if(종류==0): #등급 분류에 실패한 경우
            await ctx.send('등급이 올바르지 않아요! V03.01 개편 이후의 열번을 입력해주세요.')
        elif(종류==1): #도시철도
            try:
                노선 = int(arg[4:6])
            except(ValueError): #광역/로컬선
                노선 = arg[4:6]
                switcher={'ES':'동해시사이드선','WF':'서해환상선','SL':'남해선','NE':'북해쾌속선','NL':'북해로컬선','NS':'북해연안선','EY':'엔유선','E1':'Ex1호선','EC':'동청산선','YR':'용림선','YS':'예산세현선','DS':'대산설원선'}
                try:
                    노선명=switcher.get(노선,'존재하지 않는 노선입니다.')
                except(UnboundLocalError):
                    노선명='존재하지 않는 노선입니다.'
            else:#도시철도선
                if(노선>0 and 노선<=20):
                    노선명 = '용해{}호선'.format(노선)
                elif(노선==93 or 노선==94 or 노선==98 or 노선==99 or 노선==0 or 노선>=100):
                    노선명 = '존재하지 않는 노선입니다.'
                elif(노선==30 or 노선==31):
                    노선명 = 'CQ{}호선'.format(노선-20)
                elif(노선<=40):
                    노선명 = '유하{}호선'.format(노선-20)
                elif(노선<=60):
                    노선명 = '양서{}호선'.format(노선-40)
                elif(노선<=80):
                    노선명 = '가람{}호선'.format(노선-60)
                elif(노선<=89):
                    노선명 = '동명{}호선'.format(노선-80)
                else:
                    switcher = {90:'시온종주선',91:'능곡청안선',92:'남해하랑선',95:'종단 급행 노선',96:'강서청양선',97:'유현숲길선'}
                    노선명 = '시온 어반 네트워크 ' + switcher.get(노선,'존재하지 않는 노선')
            embed = discord.Embed(title='{} 열번의 분석 결과에요!'.format(arg),color=0x04ccff)
            embed.add_field(name="노선명",value=노선명, inline=True)
            embed.add_field(name="등급명",value=등급명, inline=True)
            embed.set_footer(text='설빈레피딕스 도시철도 열차 열번 분석 결과')
            await ctx.send(embed=embed)
        elif(종류==2): #라이너
            try:
                열번 = int(arg[4:9])
            except(ValueError):
                await ctx.send('라이너 열차의 경우, SMLN 뒤의 다섯자리는 전부 숫자로 변경되었어요. 다시 확인하시고 입력해주세요.')
            else:
                if(열번<=9999 or 열번>=40000):
                    await ctx.send('라이너 열차의 열번이 올바르지 않아요.')
                else:
                    if(열번<=20000):
                        라이너종류='통근 라이너'
                        if(열번>=10000 and 열번<=10999):
                            라이너명='구형 라이너 (남아있는 정보가 없어 정확히 어떤 라이너인지는 알 수 없어요.)'
                            열차번호=format(열번%10000,'04')
                        elif(열번>=11000 and 열번<=11999):
                            라이너명='Dawn Express'
                            열차번호=format(열번%10000,'04')
                        elif(열번>=12001 and 열번<=12060):
                            라이너명='Glowing Express'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=13001 and 열번<=13080):
                            라이너명='Sunset Liner'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=13081 and 열번<=13160):
                            라이너명='Satellite Network'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=13161 and 열번<=13240):
                            라이너명='RiverShore Express'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=13501 and 열번<=13620):
                            라이너명='Urban Liner(능곡청안선 · 남해하랑선 계통)'
                            열차번호=format(열번%1000-500,'03')
                        elif(열번>=13621 and 열번<=13740):
                            라이너명='Urban Liner(강서청양선 · 유현숲길선 계통)'
                            열차번호=format(열번%1000-620,'03')
                        elif(열번>=13741 and 열번<=13770):
                            라이너명='Urban Liner(능곡청안선 · 남해하랑선 계통 - 우회)\n학익대-유화 : 6호선'
                            열차번호=format(열번%1000-540,'03')
                        elif(열번>=13771 and 열번<=13790):
                            라이너명='Urban Liner(능곡청안선 · 남해하랑선 계통 - 우회)\n학익대-단비구청 : 6호선, 단비구청-에리 : 12호선'
                            열차번호=format(열번%1000-520,'03')
                        elif(열번>=13791 and 열번<=13810):
                            라이너명='Urban Liner(능곡청안선 · 남해하랑선 계통 - 우회)\n여진구청-유현 : 2호선, 유현-벼리시청 : CQ10호선, 벼리시청-단비구청 : 12호선, 단비구청-유화 : 6호선'
                            열차번호=format(열번%1000-490,'03')
                        else:
                            라이너명='열번이 올바르지 않거나 아직 DB에 추가되지 않은 라이너에요.'
                    elif(열번<=29999):
                        라이너종류='관광 라이너'
                        if(열번>=20001 and 열번<=20080):
                            라이너명='쿠로카제'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=20081 and 열번<=20120):
                            라이너명='아오조라'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=21001 and 열번<=21030):
                            라이너명='유키카제'
                            열차번호=열번%10000
                        elif(열번>=21031 and 열번<=21070):
                            라이너명='아메카제'
                            열차번호=열번%10000
                        elif(열번>=21071 and 열번<=21130):
                            라이너명='호시유메'
                            열차번호=열번%10000
                        else:
                            라이너명='열번이 올바르지 않거나 아직 DB에 추가되지 않은 라이너에요.\n> 아니면 V03.01 개편 때 통근 라이너나 여객 라이너로 바뀐 라이너일 수도 있으니, 다시 한 번 확인해주세요!'
                    else:
                        라이너종류='여객 라이너'
                        if(열번>=31000 and 열번<=31299):
                            라이너명='하늘특별시발 시온특별시행 CassioPeia Traveler'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=31300 and 열번<=31499):
                            라이너명='하늘특별시발 송월광역시행 CassioPeia Traveler'
                            열차번호=열번%1000
                        elif(열번>=31500 and 열번<=31749):
                            라이너명='하늘특별시발 시온특별시행 CassioPeia Commuter'
                            열차번호=열번%1000
                        elif(열번>=31750 and 열번<=31900):
                            라이너명='하늘특별시발 송월광역시행 CassioPeia Commuter'
                            열차번호=열번%1000
                        elif(열번>=31901 and 열번<=31999):
                            라이너명='CassioPeia 임시열차'
                            열차번호=열번%1000
                        elif(열번>=32001 and 열번<=32060):
                            라이너명='Forest Liner'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=32061 and 열번<=32110):
                            라이너명='StarLight Express'
                            열차번호=format(열번%1000,'03')
                        elif(열번>=34000 and 열번<=34999):
                            라이너명='Twilight Express NightLiner'
                            열차번호='N{}'.format(열번%10000)
                        else:
                            라이너명='열번이 올바르지 않거나 아직 DB에 추가되지 않은 라이너에요.'
                    embed = discord.Embed(title='{} 열번의 분석 결과에요!'.format(arg),color=0x04ccff)
                    embed.add_field(name="라이너 종류",value=라이너종류, inline=False)
                    if(열차번호 != 1048576):
                        embed.add_field(name="라이너 이름",value=라이너명, inline=True)
                        embed.add_field(name="열차번호",value='제 {}열차'.format(열차번호), inline=True)
                    else:
                        embed.add_field(name="라이너 이름",value=라이너명, inline=False)
                    embed.set_footer(text='설빈레피딕스 라이너 열차 열번 분석 결과')
                    await ctx.send(embed=embed)
        else:
            await ctx.send('데이터 처리 중 오류가 발생했어요. 다시 시도하시거나 열번을 다시 확인해주세요!')
    elif arg[0:2]=='SF': #설빈레피딕스 화물열차
        await ctx.send('아직 화물열차는 구현되지 않았어요. 빠른 시일 내에 구현할게요!')
    else: #설레 열차가 아닌 경우
        await ctx.send('열번이 올바르지 않거나, 설빈레피딕스의 열번이 아니에요. 다시 확인하시고 입력해주세요!')

@bot.command()
async def 셧다운(ctx):
    # dataSave()
    await ctx.send("설레봇을 종료합니다. 반드시 설레봇이 종료된 후 anaconda를 종료하고 Windows Terminal 창을 닫아주세요.")
    sys.exit()

bot.run(open("token.txt","r").readline())