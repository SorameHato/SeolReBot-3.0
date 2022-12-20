# coding: utf-8
import discord
import asyncio
from datetime import datetime as dt
import os
import sys
bot = discord.Bot()
ver = "3.0_2022120500 rev 30.3 build 58"
bot.srver = ver

@bot.event
async def on_ready():
    global LoadedTime
    LoadedTime = "{0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초".format(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second, int(dt.now().microsecond/1000))
    bot.LoadedTime = LoadedTime
    print('┌────────────────────────────────────────────────────────┐\n│   {name}(#{id})으로 로그인되었습니다.   │\n│ 봇이 시작된 시각 : {LoadedTime} │\n└────────────────────────────────────────────────────────┘'.format(name=bot.user.name,id=bot.user.id,LoadedTime=LoadedTime))

@bot.slash_command(guild_ids = [959065568135241728], description="Check bot's response latency")
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f"Delay: {bot.latency} seconds", color=0xFFFFFF)
    embed.set_footer(text="Embed Footer")
    await ctx.respond(embed=embed)

with open('token_new.txt','r') as token:
    bot.run(token.readline())