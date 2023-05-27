# coding: utf-8
import discord
from discord.ext import commands
import asyncio
from datetime import datetime as dt
import os
import sys
bot = discord.Bot()
ver = "3.2_2023051100 rev 2.33-ReBirth 49 build 246"
guild_ids = [
    1030056186915082262 #테스트용 서버
    #959065568135241728, 단비냐아 서버
    #971037283513946113 노브 파이터
    #현재 전부 더미처리됨
    ]
bot.srver = ver

@bot.event
async def on_ready():
    global LoadedTime
    LoadedTime = str(dt.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f"))[:-3]+"초"
    bot.LoadedTime = LoadedTime
    print('┌────────────────────────────────────────────────────────┐\n│   {name}(#{id})으로 로그인되었습니다.   │\n│ 봇이 시작된 시각 : {LoadedTime} │\n└────────────────────────────────────────────────────────┘'.format(name=bot.user.name,id=bot.user.id,LoadedTime=LoadedTime))
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='/도움말 | 설레봇 v3.2'))

@bot.event
async def on_application_command_error(ctx, error):
    embed = discord.Embed(title='자세한 내용',description=error,color=0xfae5fa)
    embed.add_field(name="보낸 분",value=ctx.author,inline=False)
    embed.add_field(name="보낸 내용",value=ctx.message,inline=False)
    embed.set_footer(text=f'설레봇 버전 {ver}')
    await ctx.respond('오류가 발생했어요!',embed=embed)
    raise error

def load_extensions():
    for filename in os.listdir('Cogs'):
        if filename.endswith('.py'):
            bot.load_extension('Cogs.{}'.format(filename[:-3]))

load_extensions()

with open('token.txt','r') as token:
    bot.run(token.readline())
