# coding: utf-8
import discord
from discord.ext import commands
from datetime import datetime as dt

class _시간(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def 시간사담(self,hour,minute):
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
    
    @commands.command()
    async def 시간(self,ctx):
        await ctx.send('삐, 삐, 삐! 당신의 설레임과 함께, 설빈레피딕스에서 {0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초를 알려드립니다.\n{7}\n이 사담은 2020년 9월 경 설레봇을 \'신 교통동호인 채팅방\'에서 돌릴 때 작성되었어요. 하늘토끼의 가상국가/가상철도 세계관과 관련되어 있거나 지금과는 맞지 않는 내용이 있을 수 있으니 양해 부탁드려요!'.format(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second, int(dt.now().microsecond/1000),self.시간사담(dt.now().hour,dt.now().minute)))

async def setup(bot):
    await bot.add_cog(_시간(bot))