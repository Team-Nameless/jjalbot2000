#!/usr/bin/env python
import os
import random
import discord
import reddit #reddit.py
from discord.ext import commands
from pathlib import Path


#load posts from reddit
redditsc = reddit.scrapper()

subque = ['programmerhumor']

for i in subque:
    redditsc.update(i)

client = discord.Client()

game = discord.Game('`r')

bot = commands.Bot(command_prefix='`', status = discord.Status.online, activity = game, help_command = None)


def redditsend(arg,ctx):
    if arg == '':
        sub, url, details = redditsc.random()

    else:
        sub, url, details = redditsc.fromsub(arg)
        print(url)

    print(arg)
        
    embed = discord.Embed(
            title = 'r/' +sub +' 에서 온 짤:',
            description = details[0]
    )

    embed.set_image(url= url)
    embed.url = 'https://reddit.com' + details[1]
    embed.set_footer(
        text  = ctx.message.author.name,
        icon_url = ctx.message.author.avatar_url
    )
    return embed



@bot.event
async def on_ready():
    print('We have logged in!')


@bot.command()
async def 도움(ctx):

    embed = discord.Embed(
        title= '짤봇2000를 사용하주셔서 감사합니다.',
        colour=discord.Colour(0xE5E242),

        description = '현재는 레딧에서 이미지를 가져오는것만 가능합니다.',
    ) 
    
    # or '\U0001f44d' or '👍'
    
    await ctx.send(embed=embed)


@bot.command(pass_context = True)
async def rd(ctx, arg = ''):
    embed = redditsend(arg,ctx)
    await ctx.send(embed=embed)


@bot.command(pass_context = True)
async def j(ctx, arg = ''):
    result = os.fspath(random.choice(list(Path("./jjall").rglob("*"))))
    print(result)
    
    file = discord.File(result)
 
    await ctx.send(file=file)
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        up = '\N{THUMBS UP SIGN}'
        down = '\N{THUMBS DOWN SIGN}'

        await message.add_reaction(up)
        await message.add_reaction(down)
        
    await bot.process_commands(message)




bot.run(open('token').read())