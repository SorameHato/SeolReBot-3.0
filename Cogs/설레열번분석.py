# coding: utf-8
import discord
from discord.ext import commands
global guild_ids
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from main import guild_ids

class _열번분석(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.slash_command(name='열번분석',guild_ids=guild_ids,description='가상 철도회사 설빈레피딕스의 열차 번호를 분석해드려요!')
    async def 열번분석(self,ctx,*,arg:discord.Option(str,'\'SM\'으로 시작하는 9자리 열번을 입력해주세요.',name='열번')):
        if arg[0:2]=='SM' and len(arg) == 9: #설빈레피딕스 도시철도 열차
            종류=0 #기본값
            노선명='존재하지 않는 노선입니다.'                        #노선/등급/라이너 정보가 오류로 인해
            등급명='존재하지 않는 등급입니다.'                        #지정되지 않을 경우를 대비해
            라이너명='존재하지 않는 라이너 열차입니다.'               #미리 값을 지정해 놓음
            라이너종류='존재하지 않는 열번이므로 알 수 없습니다.'     #이러면 오류는 안 뜨겠지
            열차번호=1048576                                          #얘는 사실 처리가 귀찮아서 콜록
            
            등급=arg[2:4] #SM'OL'21031
            등급분류=[['OR',1,'일반'],['SW',1,'일반쾌속'],['PW',1,'선별쾌속'],['RP',1,'일반급행'],['CM',1,'통근급행'],['LM',1,'쾌속급행'],['XC',1,'특별급행'],['EX',1,'고속급행'],['LC',1,'각역정차(시온 어반 네트워크)'],['SC',1,'구간급행(시온 어반 네트워크)'],['UR',1,'어반급행(시온 어반 네트워크)'],['DT',1,'도심급행(시온 어반 네트워크)'],['LN',2,'라이너']] #등급 분류 데이터
            for i in range(len(등급분류)):
                if(등급==등급분류[i][0]):
                    종류=등급분류[i][1] #도시철도 열차는 1, 라이너는 2
                    등급명=등급분류[i][2] #등급명
            if(종류==0): #등급 분류에 실패한 경우
                await ctx.respond('등급이 올바르지 않아요! V03.01 개편 이후의 열번을 입력해주세요.')
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
                    elif(노선==30 or 노선==31 or 노선==34):
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
                        switcher = {90:'횡단 종주 계통\n(능곡청안선+남해하랑선)',91:'능곡청안선',92:'남해하랑선',95:'종단 종주 계통\n(강서청양선+유현숲길선)',96:'강서청양선',97:'유현숲길선'}
                        노선명 = '시온 어반 네트워크 ' + switcher.get(노선,'존재하지 않는 노선')
                embed = discord.Embed(title='{} 열번의 분석 결과에요!'.format(arg),color=0x04ccff)
                embed.add_field(name="노선명",value=노선명, inline=True)
                embed.add_field(name="등급명",value=등급명, inline=True)
                embed.set_footer(text='설빈레피딕스 도시철도 열차 열번 분석 결과')
                await ctx.respond(embed=embed)
            elif(종류==2): #라이너
                try:
                    열번 = int(arg[4:9])
                except(ValueError):
                    await ctx.respond('라이너 열차의 경우, SMLN 뒤의 다섯자리는 전부 숫자로 변경되었어요. 다시 확인하시고 입력해주세요.')
                else:
                    if(열번<=9999 or 열번>=40000):
                        await ctx.respond('라이너 열차의 열번이 올바르지 않아요.')
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
                            elif(열번>=14000 and 열번<=14999):
                                라이너명='타사 열차(메구로 철도, DDR동당국영철도 등)\n자세한 정보는 STORM 업무망을 확인해주세요. (역무업무 또는 승무업무 > 0 기타조회 > 2 로지스 > 열번, 날짜 입력, 본청/차량기지/중정비사업단 등에서는 업무창을 닫은 후 6 편의기능 > 3 기타메뉴 > 4 로지스 접속 > 열번, 날짜 입력)'
                                열차번호=format(열번%10000,'04')
                            else:
                                라이너명='열번이 올바르지 않거나 아직 DB에 추가되지 않은 라이너에요.'
                        elif(열번<=29999):
                            라이너종류='관광 라이너'
                            if(열번>=20001 and 열번<=20080):
                                라이너명='쿠로카제'
                                열차번호=format(열번%1000,'04')
                            elif(열번>=20081 and 열번<=20120):
                                라이너명='아오조라'
                                열차번호=format(열번%1000,'04')
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
                                라이너명='열번이 올바르지 않거나 아직 DB에 추가되지 않은 라이너에요.\n아니면 V03.01 개편 때 통근 라이너나 여객 라이너로 바뀐 라이너일 수도 있으니, 다시 한 번 확인해주세요!'
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
                        await ctx.respond(embed=embed)
            else:
                await ctx.respond('데이터 처리 중 오류가 발생했어요. 다시 시도하시거나 열번을 다시 확인해주세요!')
        elif arg[0:2]=='SF': #설빈레피딕스 화물열차
            await ctx.respond('아직 화물열차는 구현되지 않았어요. 빠른 시일 내에 구현할게요!')
        else: #설레 열차가 아닌 경우
            await ctx.respond('열번이 올바르지 않거나, 설빈레피딕스의 열번이 아니에요. 다시 확인하시고 입력해주세요!')
    
    @commands.slash_command(name='약어조회',guild_ids=guild_ids,description='가상 철도회사 설빈레피딕스의 STORM 전산망에서 쓰이는 약어 목록을 조회할 수 있어요!')
    async def 약어조회(self,ctx,text:discord.Option(str,'조회하고 싶으신 약어의 종류를 선택해주세요.',name='종류',choices=['도시철도','라이너'],required=True)):
        embed = discord.Embed(title='전산 상 약어 목록이에요!',description='설빈레피딕스의 STORM 전산망에서 쓰이는 약어 목록이에요.',color=0x04ccff)
        embed.set_footer(text='설빈레피딕스 전산 약어 조회 결과')
        if(text=='도시철도'):
            embed.add_field(name='등급명',value='일반\n일반쾌속\n선별쾌속\n일반급행\n통근급행\n쾌속급행\n특별급행\n고속급행',inline=True)
            embed.add_field(name='약어',value='일반\n일쾌\n선쾌\n일급\n통급\n쾌급\n특급\n고속',inline=True)
            embed.add_field(name='전광판',value='ORdN\nOdSW\nPTSW\nOdRP\nCMRP\nLMRP\nXCRP\nEXRP',inline=True)
        elif(text=='라이너'):
            embed.add_field(name='라이너명',value='Dawn Express\nGlowing Express\nSunset Liner\nSatellite Network\nRiverShore Express\nUrban Liner\n쿠로카제\n아오조라\n유키카제\n아메카제\n호시유메\nCassioPeia\nForest Liner\nStarlight Express\nTwilight Express NightLiner',inline=True)
            embed.add_field(name='약어',value='다운\n글로\n선셋\n새틀\n리버\n어반\n쿠로\n아오\n유키\n아메\n호시\n카페\n포레\n스타\n트익',inline=True)
            embed.add_field(name='전광판',value='dAWN\nGLOW\nSNST\nSTNW\nRIVR\nURBN\nKUR\nAO\nYUKI\nAME\nHOSH\nCASP\nFORE\nSTAR\nTWEX',inline=True)
        else:
            embed.add_field(name='도시철도 약어 조회',value='/약어조회 도시철도',inline=False)
            embed.add_field(name='라이너 열차 약어 조회',value='/약어조회 라이너',inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(_열번분석(bot))
