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
    
    @commands.command()
    async def 소개(self,ctx):
        embed = discord.Embed(color=0x04ccff)
        embed.add_field(name='설빈레피딕스는?',value="설빈레피딕스는 망망대해에 떠 있는 이 세계관의 유일한 대륙, '하늘민국'의 유일한 철도 회사에요. 2011년 4월 30일 하늘민국 오픈과 동시에 설립되었고, 2022년 10월 31일 11.5주년을 맞이했어요.\n사실 '설빈레피딕스'라는 회사는 2017년 8월 5일 우리나라로 따지면 충북선, 경강선 원주~강릉 구간 같은 광역철도를 담당하기 위한 회사로 출범했어요. 도시철도는 '하늘메트로'라는 회사가 맡고 있었고요. (물론 둘 다 대표는 하늘토끼였어요) 그런데 어쩌다 보니까 2018년 초, 하늘메트로가 설빈레피딕스에 합병되게 되었어요. 단지 '이름이 멋지다'는 이유였죠. 따라서 지금은 하늘민국의 모든 철도노선을 운행하고 있답니다.\n도움을 주신 분 : 신내기지, 푸른나래(구문 등을 알려주심) CoolMetro(일부 텍스쳐) Nexon Korea, 4시(4hour4444)(안내방송 BGM) CeVIO CS7 사토 사사라, Clova AI(안내방송) 電車の音のページ(구동음) ~~예정 : 나고코모(Nagoya_Common) (텍스쳐) CeVIO AI 스즈키 츠즈미, 가능하다면 아메냐아(안내방송)~~\n더 자세한 정보는 이 쪽을 참고해주세요! http://utwiki.pe.kr/r/%EC%84%A4%EB%B9%88%EB%A0%88%ED%94%BC%EB%94%95%EC%8A%A4",inline=False)
        embed.add_field(name='유설레는?',value="자기소개에요! 이름은 유설레, 생년월일은 1998년 04월 30일이에요. 2021년 2월 기준 하늘민국 양서도 유신시 엔유구 강냥동(그 이하는 비밀!)에 살고 있고, 직업은 설빈레피딕스 기관사 겸 마스코트에요. 배속 승무사업소는 한설승무사업소인데 이상하게 출근은 맨날 세안조차장이나 엔유승무사업소로 하는 중이에요. 유신시 한설구가 아니라 유신시 엔유구에서 살고 있기도 하고요.\n취미는 아케이드판 전차로Go에서 '4㎝ 오버런'하기에요. 원래는 그루브코스터 할 때 쓰던 NESiCA를 쓰고 있었는데, 그루브코스터가 2022년 11월 말에 하드 용량 부족으로 업데이트를 중단한다고 해서 @의 캐릭터가 그려진 반다이남코 패스포트로 갈아탔어요. 설정상 히나비타의 메우 메우, 10번의 KAC에서 11번을 우승한 타츠 못지 않은 리듬게임 랭커에요. 주력 기종은 BeatStream... 이었는데 BeatStream이 죽었네요..? 그래서 이젠 평범한 고수가 되었어요.",inline=False)
        embed.set_footer(text='설레봇 버전 {} | 2020년 7월에 작성한 내용을 약간씩만 고쳐서 재활용했습니다. 지금과는 다른 내용이 일부 들어가있을 수 있습니다.'.format(self.bot.srver))
        await ctx.send('저와 설빈레피딕스의 간단한 설명이에요!',embed=embed)

async def setup(bot):
    await bot.add_cog(기타(bot))