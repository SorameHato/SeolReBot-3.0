# coding: utf-8
import discord
from discord.ext import commands
from datetime import datetime as dt
from datetime import timezone as tz
from datetime import timedelta as td
from datetime import time
global guild_ids
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from main import guild_ids

class _시간(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def __time__(self, hour, minute=0, second=0):
        return time(hour=hour,minute=minute,second=second,tzinfo=tz(td(hours=9)))
    
    def 시간사담(self, now):
        # now 변수는 슬래시커맨드가 호출될 때 초기화되는 datetime 클래스를 그대로 상속시켜야 함 (이유 : tcode, weekcode 계산 방식 변경)
        tcode = __time__(now.hour, now.minute, now.second) # 시간 형식으로 변경
        weekcode = now.isoweekday() # 추후 dt 라이브러리를 구워삶아서 추가, 메세지를 월 6:30~금 18:00, 금 18:00~24:00, 토 00:00~24:00, 일 00:00~월 06:30으로 세분화하기
        # weekcode는 월요일이 1, 화요일이 2 ... 일요일이 7인 int형 값
        # tcode는 datetime.time형의 데이터
        if weekcode == 1:
            pass #추후 대사 작성
        '''
        if(tcode <= __time__(0,30) or tcode > time(23)):
            return('슬슬 잘 준비를 해야 할 시간이네요! 저는 오늘 야간 운행이라 못 자지만요. 하암...')
        elif(tcode > __time__(0,30) and tcode <= __time__(6,30)):
            return('엣, 이렇게 늦었는데 아직도 안 주무시고 계신가요? 얼른 주무세요!')
        elif(tcode > __time__(6,30) and tcode <= __time__(9)):
            return('좋은 아침이에요! 오늘 하루도 설빈레피딕스 열차를 타고 기분 좋게, 상쾌하게 시작해요!')
        elif(tcode > __time__(9) and tcode <= __time__(11)):
            return('하늘이 참 맑죠? 하늘민국은 강수량이 적고 그마저도 겨울에 폭설로 내리는 게 대부분이라 이렇게 맨날 하늘이 파랗고 맑아요. 이 푸른 하늘을 보면서, 힘내서 열심히 일해요!')
        elif(tcode > __time__(11) and tcode <= __time__(13)):
            return('슬슬 점심시간이네요. 배고파요...')
        elif(tcode > __time__(13) and tcode <= __time__(16)):
            return('점심은 맛있게 드셨나요? 배가 불러서 졸리겠지만 같이 힘내요!')
        elif(tcode > __time__(16) and tcode <= __time__(18)):
            return('조금만 더 일하면 퇴근이에요. 화이팅이에요!')
        elif(tcode > __time__(18) and tcode <= __time__(21)):
            return('해도 졌겠다, 가벼운 산책 어때요? 전 비번인 날에는 매일 저녁 먹고 나와서 북해 해안가 산책로를 산책해요. 바닷바람도 상쾌하고 기분이 좋거든요.\n아, 그리고 신종 코로나 바이러스 때문에 수도권은 21시 이후로는 아무것도 못 한다면서요? 뭔가 일이 있으면 빨리 나가는 게 좋을 것 같아요.')
        elif(tcode > __time__(21) and tcode <= __time__(23)):
            return('이제 완전히 밤이네요. 이 시간에는 평소에 하지 못 했던 취미생활을 해 보는 게 어떨까요?')
        else:
            return('오류가 발생해 사담을 처리하지 못했어요. 명령어를 처리하는 도중에 각 시 n9분 59초가 지나면 드물게 발생할 수 있는 오류니까, 다시 한 번 시도해주세요!')
        '''
    
    @commands.slash_command(name='시간',guild_ids=guild_ids,description='현재 시간을 간단한 사담을 덧붙여서 알려줘요!')
    async def 시간(self,ctx):
        now = dt.now(tz(td(hours=9)))
        await ctx.respond('삐, 삐, 삐! 당신의 설레임과 함께, 설빈레피딕스에서 {0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초를 알려드립니다.\n{7}\n이 사담은 2020년 9월 경 설레봇을 \'신 교통동호인 채팅방\'에서 돌릴 때 작성되었어요. 하늘토끼의 가상국가/가상철도 세계관과 관련되어 있거나 지금과는 맞지 않는 내용이 있을 수 있으니 양해 부탁드려요!'.format(now.year, now.month, now.day, now.hour, now.minute, now.second, int(now.microsecond/1000),self.시간사담(now)))

def setup(bot):
    bot.add_cog(_시간(bot))
