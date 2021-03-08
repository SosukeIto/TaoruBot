 # -*- coding: utf-8 -*-
import discord
import math
import random
import json
import traceback
import asyncio
from .database import database
from PIL import Image
from discord.ext import commands
from discord import Embed, NotFound, Forbidden
from all_data.all_data import admin_list, prefix



class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    @commands.bot_has_permissions(read_messages=True, send_messages=True, embed_links=True, add_reactions=True, manage_messages=True, read_message_history=True) 
    async def help_(self, ctx):
      try: 
       contents=[
        f"🤖| **目次**\n\n1.taoruの使い方\n2.音声サンプルの試聴のやり方",
        f"🤖| **目次**\n`みたいページを発言してください。0で処理が終了します`\n1.taoruの使い方\n2.音声サンプルの試聴のやり方",
        f"🤖| **Taoruについて**\n\n`1`.自分がvoiceチャンネルに入る。\n`2`.`t>taoru`もしくは`t>tru`と発言\n`3`.接続完了の文字が表示されればOK！\n`4`.やめたいときは`t>stop`もしくはVCから抜ければ自動で退出します！\n\n`注意`.コマンドを打つ際は必ずTAOをやるチャンネルで発言すること！",
        f"🤖| **音声サンプル**\n\n`1`.ボイスチャンネルに入る\n`2`.`t>sample`もしくは`t>tru`と発言\n`3`.聴きたいサンプルの番号を発言！\n`4`.体に音を覚えさせる",
        ]
       msg = await ctx.send(contents[1])
       while True:
         try:msg_react = await self.bot.wait_for('message', check=lambda m:m.channel == ctx.channel and m.author == ctx.author,timeout = 30)
         except asyncio.TimeoutError:return await msg.edit(content = contents[0])
         if msg_react.content == "0":
             return await msg.edit(content = contents[0])
         elif msg_react.content == "1":
             return await msg.edit(content = contents[2])
         elif msg_react.content == "2":
             return await msg.edit(content = contents[3])
      except: 
            print("エラー情報\n" + traceback.format_exc())
            await self.bot.get_channel(817964124369584128).send("エラー情報```py\n" + traceback.format_exc() + "\n```")
            return 

    @commands.command(pass_context=True)
    @commands.bot_has_permissions(read_messages=True, send_messages=True, embed_links=True, add_reactions=True, manage_messages=True, read_message_history=True) 
    async def invite(self, ctx): 
       await ctx.send(f"**[以下のリンクからどうぞ]**\n(https://discord.com/api/oauth2/authorize?client_id=817952432751509515&permissions=1077226816&scope=bot)")


    @commands.command(aliases=["tru"], pass_context=True)
    @commands.bot_has_permissions(read_messages=True, send_messages=True, embed_links=True, add_reactions=True, manage_messages=True, read_message_history=True) 
    async def taoru(self, ctx): 
        try:
            geki_list = ["【超激レア】","【龍帝】","【最強】","【原初】","【天使】","【ありがとう！】","【大地の覇者】",]
            if ctx.author.voice is None:
             await ctx.send("🤖| **voiceチャンネルに接続してください**")
             return
            if ctx.guild.voice_client:
                await ctx.guild.voice_client.disconnect()
            await ctx.author.voice.channel.connect()
            channel = ctx.channel
            user = str(await self.bot.fetch_user(ctx.author.id))
            await ctx.send(f"🤖| **{channel.name}**に接続完了!\n||使い方がわからない場合は`t>help`でチェック！||")
            while True:

                  try:
                      msg_react = await self.bot.wait_for('message', check=lambda m:m.channel == ctx.channel and m.author.id == 526620171658330112 or m.author == ctx.author, timeout=30)
                  except asyncio.TimeoutError:
                      if not ctx.author.voice:
                        if ctx.guild.voice_client:
                          return await ctx.guild.voice_client.disconnect()
                        else:return
                      else:continue
                  if msg_react.content == "t>stop":
                      await msg_react.guild.voice_client.disconnect()
                      await ctx.send(f"🤖| 終了させたよ！お疲れ様👋")
                  if msg_react.content and f"{user}のHP" in msg_react.content:
                    if msg_react.content and f"{user}はやられてしまった。。。" in msg_react.content:
                      if msg_react.content and not "]はやられてしまった。。。" in msg_react.content:#Userがやられる＆ペットは参加していない
                         database.sound(ctx,1)
                         continue
                      elif msg_react.content and "]の攻撃！" in msg_react.content and "]はやられてしまった。。。" in msg_react.content:#Userがやられる＆ペット参加している
                         database.sound(ctx,1)
                         continue
                      elif msg_react.content and "]の攻撃！" in msg_react.content and not "]はやられてしまった。。。" in msg_react.content:#Userがやられる＆ペットが倒してくれた
                         continue
                    if msg_react.content and not f"{user}はやられてしまった。。。" in msg_react.content:
                      if msg_react.content and not "]はやられてしまった。。。" in msg_react.content:#Userがやられていない＆ペットは参加していない
                         database.sound(ctx,0)
                         continue
                      elif msg_react.content and "]の攻撃！" in msg_react.content and not "]はやられてしまった。。。" in msg_react.content:#Userがやられていない＆ペットは参加して倒した
                         continue

                  elif msg_react.embeds:
                      embed=msg_react.embeds[0]
                      if embed.title and "待ち構えている...！" in embed.title:
                          if embed.title and geki_list[0] in embed.title or geki_list[1] in embed.title or geki_list[2] in embed.title or geki_list[3] in embed.title or geki_list[4] in embed.title or geki_list[5] in embed.title or geki_list[6] in embed.title:
                             database.sound(ctx,3)
                          else:
                             database.sound(ctx,0)
                      elif embed.description and "はもうやられている！" in embed.description:
                          database.sound(ctx,1)
                      elif embed.description and "エリクサーを使ってこのチャンネルに参加している仲間とPETが全回復した！" in embed.description:
                          database.sound(ctx,0)
                      elif embed.description and "の処理がまだ終わって" in embed.description:
                          await asyncio.sleep(3)
                          database.sound(ctx,0)
                      elif embed.description and "問答無用で永久BANです＾＾" in embed.description and "BANされてますよ...?" in embed.description:
                          database.sound(ctx,5)
                      elif embed.description and "おっと装備してる武器は耐久力がもうないようだ..." in embed.description:
                          database.sound(ctx,2)
                      elif embed.description and "この敵には攻撃は不可能のようだ..." in embed.description:
                          database.sound(ctx,4)
        except: 
            print("エラー情報\n" + traceback.format_exc())
            await self.bot.get_channel(817964124369584128).send("エラー情報```py\n" + traceback.format_exc() + "\n```")
            return 



    @commands.command(aliases=["sp"], pass_context=True)
    @commands.bot_has_permissions(read_messages=True, send_messages=True, embed_links=True, add_reactions=True, manage_messages=True, read_message_history=True) 
    async def sample(self, ctx):
        try: 
         contents = [
           f"🤖| **おっと...**\n\n**ボイスチャンネルが見つかりません...**\nボイスチャンネルに入った後、再度コマンドを打ってください.",
           f"**音声一覧**\n\n`数字で発言してください。0で処理が終了します`\n`1`.攻撃可能\n`2`.バトルに負けた\n`3`.武器が壊れた\n`4`.超激レア＆Tohru枠出現\n`5`.この敵には攻撃は不可能のようだ...\n`6`.BANされた",  
           f"**音声一覧**\n\n`処理終了`\n`1`.攻撃可能\n`2`.バトルに負けた\n`3`.武器が壊れた\n`4`.超激レア＆Tohru枠出現\n`5`.この敵には攻撃は不可能のようだ...\n`6`.BANされた",        
           ]
         if ctx.author.voice is None:return await ctx.send(content = contents[0])

         else:
              if ctx.guild.voice_client:
                await ctx.guild.voice_client.disconnect()
              await ctx.author.voice.channel.connect()
              msg_c = await ctx.send(contents[1])
              while True:
                try:msg_react = await self.bot.wait_for('message', check=lambda m:m.channel == ctx.channel and m.author == ctx.author,timeout = 30)
                except asyncio.TimeoutError:
                    await msg_c.edit(content = contents[2])
                    if ctx.guild.voice_client:
                     return await ctx.guild.voice_client.disconnect()
                    else:return
                if msg_react.content == "0":
                   await msg_react.guild.voice_client.disconnect()
                   await msg_c.edit(content = contents[2])
                   return
                elif msg_react.content == "1":
                    database.sound(ctx, 0)
                    msg = await ctx.send(f":robot: | ♪🎶♪♬♪")
                    await asyncio.sleep(2)
                    await msg.delete()
                    await msg_react.delete()
                    continue
                elif msg_react.content == "2":
                    database.sound(ctx, 1)
                    msg = await ctx.send(f":robot: | ♪🎶♪♬♪")
                    await asyncio.sleep(2)
                    await msg.delete()
                    await msg_react.delete()
                    continue
                elif msg_react.content == "3":
                    database.sound(ctx, 2)
                    msg = await ctx.send(f":robot: | ♪🎶♪♬♪")
                    await asyncio.sleep(2)
                    await msg.delete()
                    await msg_react.delete()
                    continue
                elif msg_react.content == "4":
                    database.sound(ctx, 3)
                    msg = await ctx.send(f":robot: | ♪🎶♪♬♪")
                    await asyncio.sleep(2)
                    await msg.delete()
                    await msg_react.delete()
                    continue
                elif msg_react.content == "5":
                    database.sound(ctx, 4)
                    msg = await ctx.send(f":robot: | ♪🎶♪♬♪")
                    await asyncio.sleep(2)
                    await msg.delete()
                    await msg_react.delete()
                    continue
                elif msg_react.content == "6":
                    database.sound(ctx, 5)
                    msg = await ctx.send(f":robot: | ♪🎶♪♬♪")
                    await asyncio.sleep(2)
                    await msg.delete()
                    await msg_react.delete()
                    continue

        except: 
            print("エラー情報\n" + traceback.format_exc())
            await self.bot.get_channel(817964124369584128).send("エラー情報```py\n" + traceback.format_exc() + "\n```")
            return 



    @commands.command(aliases=["ac"], pass_context=True)
    @commands.bot_has_permissions(read_messages=True, send_messages=True, embed_links=True, add_reactions=True, manage_messages=True, read_message_history=True) 
    async def audiochange(self, ctx, *, arg):
        try: 
          if not arg:
            _, conn, cur = [sql for sql in self.bot.sqlite_list if ctx.author.id == sql[0]][0]
            user_id = ctx.author.id
            contents = [
                f"🤖| **おっと...**\n\n**ボイスチャンネルが見つかりません...**\nボイスチャンネルに入った後、再度コマンドを打ってください.",
                f"**音設定**\n\n・変えたい音を番号で発言してください。\n・0で処理が終了します。\n・`t>sample`で音を試聴できます。\n`1`.攻撃可能\n`2`.バトルに負けた\n`3`.武器が壊れた\n`4`.超激レア＆Tohru枠出現\n`5`.この敵には攻撃は不可能のようだ...\n`6`.BANされた",
                f"**音設定**\n\n`処理終了`\n`1`.攻撃可能\n`2`.バトルに負けた\n`3`.武器が壊れた\n`4`.超激レア＆Tohru枠出現\n`5`.この敵には攻撃は不可能のようだ...\n`6`.BANされた",
                ]
            if ctx.author.voice is None:return await ctx.send(content = contents[0])

            else:
              if ctx.guild.voice_client:
                await ctx.guild.voice_client.disconnect()
              await ctx.author.voice.channel.connect()
              msg_c = await ctx.send(contents[1])
              while True:
                try:msg_react = await self.bot.wait_for('message', check=lambda m:m.channel == ctx.channel and m.author == ctx.author,timeout = 30)
                except asyncio.TimeoutError:
                    await msg_c.edit(content = contents[2])
                    if ctx.guild.voice_client:
                     return await ctx.guild.voice_client.disconnect()
                    else:return
                if msg_react.content == "0":
                   await msg_react.guild.voice_client.disconnect()
                   await msg_c.edit(content = contents[2])
                   return
                elif msg_react.content == "1":
                    flag = msg_react.content
                    break
                elif msg_react.content == "2":
                    flag = msg_react.content
                    break
                elif msg_react.content == "3":
                    flag = msg_react.content
                    break
                elif msg_react.content == "4":
                    flag = msg_react.content
                    break
                elif msg_react.content == "5":
                    flag = msg_react.content
                    break
                elif msg_react.content == "6":
                    flag = msg_react.content
                    break
          else:
              flag = arg
         # database.get_player_audio(ctx, user_id, conn, cur)
          msg_c = await ctx.send(f"**音一覧**\n\nどの音に変更しますか？\n0で処理が終了します\n`1`.Jump1\n`2`.Jump2\n`3`.Stomp\n`4`Throw\n`5`.Block\n`6`.Land\n`7`.Brake\n`8`.Impact\m`9`.Door\n`10`.Damage1\n`11`.Damage2\n`12`.Defend\n`13`.Defeat\n`14`.Item1\n`15`.Item2\n`16`.Item3\n`17`.Message1\n`18`.Message2\n`19`.Message3\n`20`.Select\n`21`.Select\n`22`.Select")
          while True:
                try:msg_react = await self.bot.wait_for('message', check=lambda m:m.channel == ctx.channel and m.author == ctx.author and m.content.isdigit() and 0 <= int(m.content) <= 22,timeout = 30)
                except asyncio.TimeoutError:
                    await msg_c.edit(content = contents[2])
                    if ctx.guild.voice_client:
                     return await ctx.guild.voice_client.disconnect()
                    else:return
                if msg_react.content == "0":
                   await msg_react.guild.voice_client.disconnect()
                   await msg_c.edit(content = contents[2])
                   return
                else:
                    order_sound(ctx,msg_react.content)
                    msg = await ctx.send(f":robot: | ♪🎶♪♬♪")
                    await asyncio.sleep(2)
                    await msg_react.delete()
                    await msg.edit(content = f":robot: | 設定が完了しました！")
                    return
        except: 
            print("エラー情報\n" + traceback.format_exc())
            await self.bot.get_channel(817964124369584128).send("エラー情報```py\n" + traceback.format_exc() + "\n```")
            return 

def setup(bot): # 絶対必須
    bot.add_cog(command(bot))