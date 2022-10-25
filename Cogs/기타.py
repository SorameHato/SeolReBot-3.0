# coding: utf-8
import discord
from discord.ext import commands as bot

class 기타(bot.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @bot.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms') # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.
    
    @bot.command()
    async def 테스트(self, ctx):
        await ctx.send('테스트 결과입니다!\n> 보낸 사람 : {0}\n> 보낸 사람의 닉네임 : {1}\n> 보낸 사람의 ID : {2}\n> 보낸 사람을 멘션할 경우 : <@{2}>'.format(ctx.message.author, ctx.message.author.name, ctx.message.author.id))
    
    @bot.command()
    async def 정보(self, ctx):
        await ctx.send(f"설레봇의 정보입니다!\n> 버전 : {self.bot.srver}\n> 기반 : 2.5_2021021703 rev 6.3 build 14 (2021년 2월 18일 1시 0분 45초)\n> DB1 : PJU:K:C:B:2021103105 (2021년 10월 31일 4시 3분 51초)\n> DB2 : b102dff1ef5ddf5e3e9d7a4028656a90aa921252 (2022년 9월 21일 2시 47분 0초)\n> 설레봇을 개발한 사람 : 하늘토끼(ghwls030306@s-r.ze.am)\n> 설레봇이 시작된 시간 : {self.bot.LoadedTime}")

async def setup(bot):
    await bot.add_cog(기타(bot))