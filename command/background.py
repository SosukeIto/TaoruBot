# -*- coding: utf-8 -*-
import os
import discord
from discord.ext import commands
from discord import Embed, Forbidden, Game,AllowedMentions
from threading import Thread
from aiosqlite import connect
from asyncio import new_event_loop
import asyncio
from traceback import format_exc

class Background(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener() 
    async def on_message(self, message): 
        try:
            pass
        except:
            return print("�G���[���\n" + traceback.format_exc())
def setup(bot): # ��ΕK�{
    bot.add_cog(Background(bot))