# coding: utf-8
import discord
from discord.ext import commands
import asyncio
from datetime import datetime as dt
import os
import sys
bot = discord.Bot()
ver = "3.1_2022122208 rev 2.8 build 171"
guild_ids = [
    959065568135241728, #단비냐아 서버
    971037283513946113 #노브 파이터
    ]
bot.srver = ver

@bot.event
async def on_ready():
    global LoadedTime
    LoadedTime = "{0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초".format(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second, int(dt.now().microsecond/1000))
    bot.LoadedTime = LoadedTime
    print('┌────────────────────────────────────────────────────────┐\n│   {name}(#{id})으로 로그인되었습니다.   │\n│ 봇이 시작된 시각 : {LoadedTime} │\n└────────────────────────────────────────────────────────┘'.format(name=bot.user.name,id=bot.user.id,LoadedTime=LoadedTime))
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='/도움말 | 설레봇 v3.1'))

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