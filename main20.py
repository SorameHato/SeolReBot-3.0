# coding: utf-8
import discord
from discord.ext import commands
import asyncio
from datetime import datetime as dt
import os
import sys

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.설레 ', intents=intents)

ver = "3.0_2022111915 rev 0.29.1 build 54"
bot.srver = ver

# @bot.command(name="관리 언로드")
# async def unload_extension(ctx, extension=None):
    # if extension is not None:
        # await unload_function(extension)
        # await ctx.send(f":white_check_mark: {extension}기능을 종료했습니다!")
    # else:
        # await unload_function(None)
        # await ctx.send(":white_check_mark: 모든 확장기능을 종료했습니다!")
 
 
# async def unload_function(extension=None):
    # if extension is not None:
        # try:
            # await bot.unload_extension(f"Cogs.{extension}")
        # except (commands.ExtensionNotLoaded, commands.ExtensionNotFound):
            # pass
    # else:
        # for filename in os.listdir("Cogs"):
            # if filename.endswith(".py"):
                # try:
                    # await bot.unload_extension(f"Cogs.{filename[:-3]}")
                # except (commands.ExtensionNotLoaded, commands.ExtensionNotFound):
                    # pass


# 출처: https://aochfl.tistory.com/337?category=1039703 [매초리의 생활공간:티스토리]

@bot.command()
async def 셧다운(ctx):
    if ctx.message.author.id == 971036318035501066:
        await ctx.send('설레봇을 종료합니다. 반드시 설레봇이 종료된 후 anaconda를 종료하고 Windows Terminal 창을 닫아주세요.')
        await bot.close()
    else:
        await ctx.send('소유주 인증에 실패했습니다.')

@bot.event
async def on_ready():
    global LoadedTime
    LoadedTime = "{0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초".format(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second, int(dt.now().microsecond/1000))
    bot.LoadedTime = LoadedTime
    print('┌────────────────────────────────────────────────────────┐\n│   {name}(#{id})으로 로그인되었습니다.    │\n│ 봇이 시작된 시각 : {LoadedTime} │\n└────────────────────────────────────────────────────────┘'.format(name=bot.user.name,id=bot.user.id,LoadedTime=LoadedTime))

@bot.event
async def on_command_error(ctx, error):
    print('오류 발생 | 보낸 사람 : {}, 내용 : {}, 오류 : {}'.format(ctx.message.author,ctx.message.content,error))
    embed = discord.Embed(title='자세한 내용',description=error,color=0xfae5fa)
    embed.add_field(name="보낸 분",value=ctx.message.author,inline=False)
    embed.add_field(name="보낸 내용",value=ctx.message.content,inline=False)
    embed.set_footer(text='설레봇 버전 {}'.format(ver))
    await ctx.send('오류가 발생했어요!',embed=embed)

async def load_extensions():
    for filename in os.listdir('Cogs'):
        if filename.endswith('.py'):
            await bot.load_extension('Cogs.{}'.format(filename[:-3]))

asyncio.run(load_extensions())
with open('token.txt','r') as token:
    bot.run(token.readline())