# coding: utf-8
import discord
from discord.ext import commands as bot

class _도움말(bot.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @bot.command()
    async def 도움말(self,ctx,*,text='0'):
        num = text.split(' ')[0]
        if(num == '1' or num == '0' or num == ''):
            await ctx.send('설레봇의 명령어 목록입니다!(1/3)\n\n.설레 도움말 [페이지]\n> 명령어 목록을 볼 수 있는 명령어에요! 지금 쓰고 있는 명령어에요.\n.설레 확률 [문장]\n> 어떤 것에 대한 확률을 구할 수 있는 명령어에요. 흔히들 \'확률봇\'이라고 많이 부르는 것 같아요!\n.설레 아침메뉴추천 | .설레 점심메뉴추천 | .설레 저녁메뉴추천 | .설레 야식메뉴추천\n> 설레봇이 랜덤으로 아침/점심/저녁/야식으로 무엇을 먹을 지 추천해주는 명령어에요!')
        elif(num == '2'):
            await ctx.send('설레봇의 명령어 목록입니다!(2/3)\n\n.설레 열번분석 [다이어그램]\n> 가상 철도회사 설빈레피딕스의 다이어그램 번호를 분석할 수 있는 명령어에요.\n> 아메카제, 쿠로카제, S특급 세레나데 닛소라, 슈퍼 라이너 스카이 같이 메구로 철도선에 직결하거나 메구로 철도선에서 직결해 들어오는 열차는 메구로 철도선의 다이어그램(1031R)이 아닌 설빈레피딕스에서 부여한 다이어그램(SMLN21031)을 입력해야 하는 점 유의해주세요!\n.설레 시간\n> 설레봇이 간단한 사담과 함께 시간을 알려주는 명령어에요. 사담은 2021년 2월의 사담 데이터 그대로라 지금과 맞지 않는 내용이 있을 수 있으니까, 양해 부탁드려요!\n> 또한 시간은 하늘토끼의 컴퓨터 시계를 기준으로 표시돼요. KRISS 한국표준과학연구원 표준시계서버와 매일 동기화를 한다고는 하는데도 맨날 2초씩 3초씩 차이가 나니까, 시간이 조금 틀려도 양해 부탁드려요.\n.설레 정보\n> 설레봇의 정보를 볼 수 있어요! 설레봇의 버전, 봇이 시작된 시간 등을 볼 수 있어요.')
        elif(num == '3'):
            await ctx.send('설레봇의 명령어 목록입니다!(3/3)\n이 페이지는 도박 명령어만 다루는 특별 페이지에요. 현재 도박봇의 경우 Python 자체의 의사난수 알고리즘에 문제가 있는 건지 확률이 일정하지 않아요. 3억 6140만 6740번(시드 개수의 10310배)이나 테스트를 돌려봤는데도 이론상 확률과 유의미하게 차이가 나요. 아나콘다 3.10 버전이 나오면 바로 업데이트할 테니까, 그 때까진 양해 부탁드릴게요!\n.설레 도박 회생\n> 돈을 모두 탕진하신 경우, 1주일에 딱 한 번 회생할 수 있어요.\n> 설레봇은 개인회생을 해도 딱히 불이익이 없긴 하지만, 돈이 만원으로 초기화되고 추후 여러가지 불이익을 구현할 예정이니 남용은 하지 말아주세요!')
        else:
            await ctx.send('아직 존재하지 않는 페이지를 입력하셨어요. 설레봇은 2020년 5월에 만들어진 따끈따끈한 봇이라 아직 기능이 그렇게 많지는 않답니다. 앞으로 더 발전할 설레봇을 기대해주세요!')

async def setup(bot):
    await bot.add_cog(_도움말(bot))