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

async def setup(bot):
    await bot.add_cog(기타(bot))