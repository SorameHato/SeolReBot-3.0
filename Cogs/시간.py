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
def __time__(hour, minute=0, second=0):
    return time(hour=hour,minute=minute,second=second,tzinfo=tz(td(hours=9)))

def __checkBetween__(tcode, beginHour, beginMinute, endHour, endMinute):
    return (tcode >= __time__(beginHour, beginMinute) and tcode < __time__(endHour, endMinute))

def __checkLess__(tcode, endHour, endMinute):
    return (tcode <= __time__(endHour, endMinute))

__대사__ = [ #월요일
    ['주말이 끝났어요... 조금 힘드시겠지만 그래도 조금만 힘을 내 주세요! 저도 힘 내서 열심히 여러분을 가시는 목적지까지 모셔다 드릴 테니까요! 화이팅이에요!', #일 2300 ~ 월 0030
     '좋은 아침이에요! 월요일이라 힘들긴 하지만 그래도 상쾌한 아침이라 기분이 좋은 것 같아요. 오늘 하루도 설빈레피딕스 열차를 타고 기분 좋게, 상쾌하게 시작해요!', #월 0630 ~ 월 0800
     '하늘이 참 맑죠? 하늘민국은 강수량이 적고 그마저도 겨울에 폭설로 내리는 게 대부분이라 이렇게 맨날 하늘이 파랗고 맑아요. 월요일이라 힘드시겠지만, 이 푸른 하늘을 보면서 힘내서 열심히 일해요! 눈 깜짝할 사이에 점심시간이 올 테니까요!' #월 0900 ~ 월 1100
     '슬슬 점심시간이네요... 오늘의 구내식당 점심은 뭐일려나요? 설빈레피딕스에서 직영하는 빛리역 구내식당은 엄청 맛있는데, 외부 업체에서 하는 서지은역 구내식당은 별로인 것 같아요.\n근데 전 이상하게 빛리승무본부보단 서지은승무본부에 배치되는 경우가 많더라고요... 공식 캐릭터 보정은 못 받는 걸까요?', #월 1100~1300
     '다행히 오늘은 빛리승무본부 배속이라 맛있는 점심을 먹었어요! 배가 불러서 졸리겠지만, 힘 내서 퇴근할 때 까지 열심히 일해봐요!', #월 1300 ~ 월 1630
     '월요일이라 월요병 때문에 힘드셨을 것 같은데, 그래도 열심히 일하시느라 수고하셨어요! 빠른 설빈레피딕스 열차를 타고 빛의 속도로 퇴근해요!', #월 1800 ~ 월 1930
     '슬슬 해가 지는 것 같네요. 가벼운 산책은 어떠신가요? 전 해가 지고 난 직후의 풍경을 좋아해서, 비번인 날에는 항상 저녁을 먹고 나와서 북해 해안가 산책로를 산책하고 있어요.', #월 1930 ~ 월 2100
     '이제 완전히 밤이네요. 평소에 못 했던 취미 생활에 도전해보시는 건 어떤가요? 전 요새 그림에 도전하고 있어요! 언젠가 금손 작가님 유설레가 되는 날까지, 열심히 노력하려고요!', #월 2100 ~ 월 2300
    ]
]

__공통대사__ = [#평일
    ['엣, 이렇게 늦었는데 아직까지도 안 주무시는 건가요? 얼른 주무세요!', #월 0030 ~ 월 0200 / 평일 공통대사
     '저기... 밤이 늦었거든요..? 밤을 새실 건가요? 내일 엄청 피곤해하실 거에요. 지금 바로 폰이나 컴퓨터를 끄고 침대나 이부자리로 가서 누우세요!', #월 0200 ~ 월 0630 / 평일 공통대사
     '출근 전쟁 중이신가요? 조금만 더 버티면 분명 금방 회사나 학교에 도착할 테니까, 조금만 더 힘 내 주세요!', #월 0800 ~ 월 0900, 평일 공통대사
     '조금만 더 일하면 퇴근이에요! 마지막까지 힘내주세요!', #월 1630 ~ 월 1800, 평일 공통대사
    ]
]
    

class _시간(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def 시간사담(self, now):
        # now 변수는 슬래시커맨드가 호출될 때 초기화되는 datetime 클래스를 그대로 상속시켜야 함 (이유 : tcode, weekcode 계산 방식 변경)
        tcode = __time__(now.hour, now.minute, now.second) # 시간 형식으로 변경
        weekcode = now.weekday() # 추후 dt 라이브러리를 구워삶아서 추가, 메세지를 월 6:30~금 18:00, 금 18:00~24:00, 토 00:00~24:00, 일 00:00~월 06:30으로 세분화하기
        # weekcode는 월요일이 0, 화요일이 1 ... 일요일이 6인 int형 값
        # tcode는 datetime.time형의 데이터
        if weekcode <= 4 : #평일
            if __checkLess__(tcode, 0, 30): # 평일 0000~0030 요일변 대사
                return(__대사__[weekcode][0])
            elif __checkLess__(tcode, 2, 0): # 평일 0030~0200 공통 대사 : 엣, 이렇게 늦었는데 ~
                return(__공통대사__[0][0])
            elif __checkLess__(tcode, 6, 30): # 평일 0200~0630 공통 대사 : 저기... 밤이 늦었거든요..? ~
                return(__공통대사__[0][1])
            elif __checkLess__(tcode, 8, 0): # 평일 0630~0800 요일별 대사
                return(__대사__[weekcode][1])
            elif __checkLess__(tcode, 9, 0): # 평일 0800~0900 공통 대사 : 출근 전쟁 중이신가요? ~
                return(__공통대사__[0][2])
            elif __checkLess__(tcode, 11, 0): # 평일 0900~1100 요일별 대사
                return(__대사__[weekcode][2])
            elif __checkLess__(tcode, 13, 0): # 평일 1100~1300 요일별 대사
                return(__대사__[weekcode][3])
            elif __checkLess__(tcode, 16, 30): # 평일 1300~1630 요일별 대사
                return(__대사__[weekcode][4])
            elif __checkLess__(tcode, 18, 0): # 평일 1630~1800 공통 대사 : 조금만 더 일하면 퇴근이에요! ~
                return(__공통대사__[0][3])
            elif __checkLess__(tcode, 19, 30): # 평일 1800~1930 요일별 대사
                return(__대사__[weekcode][5])
            elif __checkLess__(tcode, 21, 0): #평일 1930~2100 요일별 대사
                return(__대사__[weekcode][6])
            elif __checkLess__(tcode, 23, 0): #평일 2100~2300 요일별 대사
                return(__대사__[weekcode][7])
            else
                return(__대사__[weekcode+1 if weekcode<4 else 0][0])
            
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
