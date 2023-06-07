# coding: utf-8
import discord
from discord.ext import commands
global guild_ids
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from main import guild_ids

class _도움말(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.slash_command(name='도움말',guild_ids=guild_ids,description='설레봇의 명령어 목록을 볼 수 있어요!')
    async def 도움말(self,ctx,num:discord.Option(int,'페이지를 입력해주세요! (1~3)',name='페이지',min_value=1,max_value=4)):
        if(num == 1 or num == 0):
            embed = discord.Embed(color=0x04ccff)
            embed.add_field(name='/도움말 [페이지]',value='명령어 목록을 볼 수 있는 명령어에요! 지금 쓰고 있는 명령어에요.',inline = False)
            embed.add_field(name='/정보',value='설레봇의 정보를 볼 수 있어요! 설레봇의 버전, 봇이 시작된 시간 등을 볼 수 있어요.',inline = False)
            embed.add_field(name='/업뎃내역',value='설레봇의 업데이트 내역을 볼 수 있어요!',inline = False)
            embed.add_field(name='/소개',value='설빈레피딕스와 설빈레피딕스 마스코트인 저, 유설레의 간단한 소개를 볼 수 있어요.',inline = False)
            embed.add_field(name='/확률 [문장]',value='어떤 것에 대한 확률을 설레봇이 계산해주는 명령어에요. 흔히들 \'확률봇\'이라고 많이 부르는 것 같아요!',inline = False)
            embed.add_field(name='/핑',value='Summer Pockets의 아오의 반려동물? 이나리가 \'퐁!\' 하면서 현재 설레봇의 레이턴시를 알려줘요!',inline = False)
            embed.set_footer(text='설레봇 버전 {}'.format(self.bot.srver))
            await ctx.respond('설레봇의 명령어 목록입니다!(1/3)',embed=embed)
        elif(num == 2):
            embed = discord.Embed(color=0x04ccff)
            embed.add_field(name='/아침추천 | /점심추천 | /저녁추천 | /야식추천',value='설레봇이 랜덤으로 아침/점심/저녁/야식으로 무엇을 먹을 지 추천해주는 명령어에요!',inline = False)
            embed.add_field(name='/열번분석 [다이어그램]',value='가상 철도회사 설빈레피딕스의 다이어그램 번호를 분석할 수 있는 명령어에요.\n메구로 철도선에 직결하거나 메구로 철도선에서 직결해 들어오는 열차(v02.92 기준 구로테츠 S특급 닛소라, 관광라이너 호시, 아메, 시로, 후유)는 메구로 철도선의 다이어그램(1031U, 45S)이 아닌 설빈레피딕스에서 부여한 9자리 다이어그램(SMLN21031, SMLN14045 / 도쿄텔레포트역, 니지가사키역, 시노노메역, 치도리역에서 확인 가능)을 입력해야 하는 점 유의해주세요! 해당 명령어는 v03.01 개편 중의 버전인 v02.90.00(R04.10.31) 이후의 변경 내역은 들어가 있지 않으니 주의해주세요!',inline = False)
            embed.add_field(name='/약어조회',value='가상 철도회사 설빈레피딕스의 STORM 전산망에서 쓰이는 약어를 조회할 수 있는 명령어에요.',inline = False)
            embed.add_field(name='/시간',value='설레봇이 간단한 사담과 함께 시간을 알려주는 명령어에요. 사담은 2021년 2월의 사담 데이터 그대로라 지금과 맞지 않는 내용이 있을 수 있으니까, 양해 부탁드려요!\n또한 시간은 하토의 컴퓨터 시계를 기준으로 표시돼요. KRISS 한국표준과학연구원 표준시계서버와 매일 동기화를 한다고는 하는데도 맨날 2초씩 3초씩 차이가 나니까, 시간이 조금 틀려도 양해 부탁드려요.',inline = False)
            embed.add_field(name='/타이머',value='지정한 시간 이후에 지정한 메세지를 전송하는 명령어에요!',inline = False)
            embed.set_footer(text='설레봇 버전 {}'.format(self.bot.srver))
            await ctx.respond('설레봇의 명령어 목록입니다!(2/3)',embed=embed)
        elif(num == 3):
            embed = discord.Embed(color=0x04ccff)
            embed.add_field(name='/도박 조회',value='소지금을 조회할 수 있는 명령어에요.',inline = False)
            embed.add_field(name='/도박 룰렛 [금액]',value='룰렛을 돌릴 수 있는 명령어에요.',inline = False)
            embed.add_field(name='/도박 회생',value='1주일에 한 번 개인회생을 할 수 있는 명령어에요. 회생을 하면 금액이 초기금액으로 초기화돼요.',inline = False)
            embed.add_field(name='/도박 이체 [보낼 분 멘션] [금액]',value='소지금을 다른 분께 이체할 수 있는 명령어에요.',inline = False)
            embed.set_footer(text='설레봇 버전 {}'.format(self.bot.srver))
            await ctx.respond('설레봇의 명령어 목록입니다!(3/3)\n이 페이지는 도박 명령어만 다루는 특별 페이지에요. 현재 도박봇의 경우 Python 자체의 의사난수 알고리즘에 문제가 있는 건지 확률이 일정하지 않아요. 3억 6140만 6740번(시드 개수의 10310배)이나 테스트를 돌려봤는데도 이론상 확률과 유의미하게 차이가 나요. (약 0.02% 정도) 아나콘다 3.10 버전이 나오면 바로 업데이트할 테니까, 그 때까진 양해 부탁드릴게요!\n만약 데이터가 없다고 뜨면, 먼저 조회를 해보세요!',embed=embed)
        else:
            await ctx.respond('아직 존재하지 않는 페이지를 입력하셨어요. 설레봇은 2020년 5월에 만들어진 따끈따끈한 봇이라 아직 기능이 그렇게 많지는 않답니다. 앞으로 더 발전할 설레봇을 기대해주세요!')

def setup(bot):
    bot.add_cog(_도움말(bot))