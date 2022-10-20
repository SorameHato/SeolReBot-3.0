# coding: utf-8
import discord
from discord.ext import commands
import asyncio
from datetime import datetime as dt

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.설레 ', intents=intents)

ver = "3.0_2022102102 rev 0.0 build 20"

async def main():
    async with bot:
        with open('token.txt','r') as token:
            await bot.start(token.readline())
    global LoadedTime
    LoadedTime = "{0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초".format(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second, int(dt.now().microsecond/1000))
    print('┌────────────────────────────────────────────────────────┐\n│   {name}(#{id})으로 로그인되었습니다.    │\n│ 봇이 시작된 시각 : {LoadedTime} │\n└────────────────────────────────────────────────────────┘'.format(name=bot.user.name,id=bot.user.id,LoadedTime=LoadedTime))

asyncio.run(main())