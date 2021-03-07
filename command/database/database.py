 # -*- coding: utf-8 -*-
import random
import math
import glob
import json
import discord
import traceback
import asyncio
from PIL import Image
from discord import Embed, NotFound, Forbidden


def sound(ctx,num):
        atk = r"./sampleaudio/SNES-Action01-20(Select).mp3"
        lose = r"./sampleaudio/SNES-Action01-03(Stomp).mp3"
        weapon= r"./sampleaudio/SNES-Action01-11(Damage).mp3"
        geki = r"./sampleaudio/SNES-Action01-17(Message).mp3"
        ryuusei = r"./sampleaudio/SNES-Action01-08(Impact).mp3"
        ban = r"./sampleaudio/SNES-Action01-19(Message).mp3"
        sounds = (atk, lose, weapon, geki, ryuusei, ban)
        ctx.guild.voice_client.play(
           discord.FFmpegPCMAudio(
               executable=r"C:/Users/81808/AppData/Local/Programs/ffmpeg/bin/ffmpeg.exe", #‚±‚±‚Éffmpeg.exe‚Ì‚ ‚éêŠ‚ÌƒpƒX‚ğ“ü‚ê‚Ä‚ËI
               source=sounds[num]), after=lambda e: print(f"{ctx.channel.id}: {ctx.author.id}", e))




