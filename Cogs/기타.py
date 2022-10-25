# coding: utf-8
import discord
from discord.ext import commands

class 기타(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms') # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.
    
    @commands.command()
    async def 테스트(self, ctx):
        await ctx.send('테스트 결과입니다!\n> 보낸 사람 : {0}\n> 보낸 사람의 닉네임 : {1}\n> 보낸 사람의 ID : {2}\n> 보낸 사람을 멘션할 경우 : <@{2}>'.format(ctx.message.author, ctx.message.author.name, ctx.message.author.id))
    
    @commands.command()
    async def 정보(self, ctx):
        embed = discord.Embed(title='설레봇의 정보입니다!',color=0x04ccff)
        embed.add_field(name='버전',value=self.bot.srver,inline = False)
        embed.add_field(name='기반이 된 버전',value='코드 : 2.5_2021021703 rev 6.3 build 14 (2021년 2월 18일 1시 0분 45초)\nDB1 : PJU:K:C:B:2021103105 (2021년 10월 31일 4시 3분 51초)\nDB2 : b102dff1ef5ddf5e3e9d7a4028656a90aa921252 (2022년 9월 21일 2시 47분)',inline = False)
        embed.add_field(name='개발자',value='하늘토끼(ghwls030306@s-r.ze.am)',inline = False)
        embed.add_field(name='깃허브 링크',value='https://github.com/SkyRabbITs/SeolReBot-3.0',inline = False)
        embed.add_field(name='설레봇이 시작된 시간',value=self.bot.LoadedTime,inline = False)
        embed.set_footer(text='설레봇 버전 {}'.format(self.bot.srver))
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(기타(bot))