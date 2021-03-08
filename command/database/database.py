 # -*- coding: utf-8 -*-
import random
import math
import glob
import json
import discord
import traceback
import asyncio
from sqlite3 import connect
from PIL import Image
from discord import Embed, NotFound, Forbidden


async def sound(ctx,num):
   
   atk_, lose_, weapon_, geki_, ryuusei_, ban_ = await get_player_audio(ctx, user_id, conn, cur)
   atk = f"./sampleaudio/{atk_}.mp3"
   lose = f"./sampleaudio/{lose_}.mp3"
   weapon= f"./sampleaudio/{weapon_}.mp3"
   geki = f"./sampleaudio/{geki_}.mp3"
   ryuusei = f"./sampleaudio/{ryuusei_}.mp3"
   ban = f"./sampleaudio/{ban_}.mp3"
   sounds = (atk, lose, weapon, geki, ryuusei, ban)
   ctx.guild.voice_client.play(
           discord.FFmpegPCMAudio(
               executable=r"C:/Users/81808/AppData/Local/Programs/ffmpeg/bin/ffmpeg.exe",
               source=sounds[num]), after=lambda e: print(f"{ctx.channel.name}: {ctx.author.name}", e))

async def get_player_audio(ctx, user_id, conn, cur):
    try: 
        await cur.execute("SELECT * FROM audio WHERE user_id=?", (user_id,))
        sounds = await cur.fetchall() 
        if not sounds: # ユーザーのデータが存在してない場合
            await cur.execute("INSERT INTO audio values(?,?,?,?,?,?)", (user_id, 20, 3, 11, 17, 8, 19))
            await conn.commit() 
            return "20", "3", "11", "17", "8", "19"
        return str(sounds[0]), str(sounds[1]), str(sounds[2]), str(sounds[3]), str(sounds[4]), str(sounds[5])

def order_sound(ctx, num):
   s_path = f"./sampleaudio/{num}.mp3"
   ctx.guild.voice_client.play(
           discord.FFmpegPCMAudio(
               executable=r"C:/Users/81808/AppData/Local/Programs/ffmpeg/bin/ffmpeg.exe",
               source=s_path), after=lambda e: print(f"{ctx.channel.name}: {ctx.author.name}", e))





