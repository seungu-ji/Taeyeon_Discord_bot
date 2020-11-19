import asyncio
import discord
from discord.ext import commands
import os


token_path = os.path.dirname(os.path.abspath(__file__))+"/token.txt"
t = open(token_path,"r",encoding="utf-8")
token = t.read().split()[0]

game = discord.Game("탱구")
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game, help_command=None)
# commands.Bot(command_prefix는 해당 구문이 맨 앞에 있을때 명령어로 인식, status는 봇의 상태값, activity는 봇의 상태말)

@bot.event
async def on_ready():
    print("봇 시작")

@bot.command()
async def help(ctx):
    await ctx.send("무엇을 도와드릴까요?")

@bot.command()
async def about_taeyeon(ctx):
    embed = discord.Embed(title=f"안녕하세요,",description=f"태연입니다!", color=0xf33b76)
    embed.add_field(name=f"태연님의 출생월일은요?",value=f"1989년 3월 9일",inline=False)
    embed.add_field(name=f"태연님의 신체 스펙은요?",value=f"160cm, 45kg, 245mm, A형",inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx):
    await ctx.send("https://www.youtube.com/channel/UC5z2fxN6rs69cSyXur6X6Mg")

@bot.command()
async def img(ctx):
    file = discord.File("./img/태연50.jpg",spoiler=False)
    await ctx.channel.send(file=file)
    
@bot.event
async def on_member_join(member):
    await member.send("{}님 어서오세요.".format(member))


@bot.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("ㅅㅂ")
    print(bad)
    if bad >= 0:
        await message.channel.send("말 이쁘게 하랬지!")
        await message.delete() # 욕설 문장 삭제
    await bot.process_commands(message) # 메시지 중 명령어가 있을 경우 처리해주는 코드 ex)!ㅅㅂ


bot.run(token)