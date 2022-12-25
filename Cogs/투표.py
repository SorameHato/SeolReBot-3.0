# coding: utf-8
import discord
from discord.ext import commands
global guild_ids
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from main import guild_ids
from datetime import datetime

class VoteModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="투표의 제목을 입력해주세요!"))
        self.add_item(discord.ui.InputText(label="투표의 항목을 한 줄에 하나씩 입력해주세요!", style=discord.InputTextStyle.long))
        self.add_item(discord.ui.InputText(label="투표를 끝낼 날짜와 시간을 입력해주세요! (예시 : 20221031 103145)"))

    async def callback(self, interaction: discord.Interaction):
        try:
            endDate = datetime(int(self.children[2].value[0:4]),int(self.children[2].value[4:6]),int(self.children[2].value[6:8]),int(self.children[2].value[9:11]),int(self.children[2].value[11:13]),int(self.children[2].value[13:15]))
        except Exception as error:
            raise error
        else:
            voteData = [self.children[0].value,[],endDate]
            itemList = ''
            j = 1
            for line in self.children[1].value.split('\n'):
                voteData[1].append(line)
                itemList += f'{j}. {line}\n'
                j += 1
            
            embed = discord.Embed(title="아래와 같은 투표를 성공적으로 시작했어요!")
            embed.add_field(name="투표명", value=voteData[0],inline=False)
            embed.add_field(name="항목", value=itemList[:-1],inline=False)
            embed.add_field(name="종료일", value=voteData[2].strftime("%Y년 %m월 %d일 %H시 %M분 %S초"),inline=True)
            await interaction.response.send_message(embed=embed)

class _투표(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    투표g = discord.SlashCommandGroup(name="투표",description="투표 기능과 관련된 명령어에요!",guild_ids=guild_ids)
    
    @투표g.command(name='시작',description='새로운 투표를 시작할 수 있어요! 한 번 생성한 투표는 수정할 수 없으니까 오타가 나지 않도록 주의해주세요!')
    async def voteStart(self,ctx):
        modal = VoteModal(title='새로운 투표의 정보를 입력해주세요!')
        await ctx.send_modal(modal)
    
    @투표g.command(name='목록',description='현재 진행중인 투표의 목록을 볼 수 있어요!')
    async def voteList(self,ctx):
        await ctx.respond('투표 목록 테스트에요!')
    
    @투표g.command(name='정보',description='현재 진행중인 투표의 자세한 정보를 볼 수 있어요!')
    async def voteDetail(self,ctx,i:discord.Option(int,'\'/투표 목록\' 명령어로 조회한 투표의 번호를 입력해주세요!',name='번호')):
        await ctx.respond(f'투표 상세정보 테스트에요! 디버그용 : i = {i}')

def setup(bot):
    bot.add_cog(_투표(bot))