# -*- coding: utf-8 -*-
import os
import discord
from discord.ext import commands
from discord import Embed, Forbidden, Game,AllowedMentions
from threading import Thread
from sqlite3 import connect
from asyncio import new_event_loop
import asyncio
from traceback import format_exc
from all_data.all_data import token, prefix, admin_list
loop = new_event_loop()


async def run():
    sqlite_list = []
    bot = MyBot(sqlite_list=sqlite_list)
    try:
        if not os.path.exists("./all_data/taoru.db"):
            open(f"./all_data/taoru.db", "w").close() 
            async with connect('./all_data/taoru.db') as conn: # データベースに接続
                async with conn.cursor() as cur:
                    await conn.commit() 

                    await cur.execute("CREATE TABLE IF NOT EXISTS audio(user_id BIGINT(20), atk_audio INT, lose_audio INT, waeapon_audio INT, geki_audio INT, ryuusei_audio INT, ban_audio INT)")
                    await conn.commit()

        await bot.start(token) 
    except:
       print("エラー情報\n" + format_exc())
       return

class MyBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=commands.when_mentioned_or(prefix), allowed_mentions=AllowedMentions(everyone=False, users=False, roles=False), fetch_offline_members=False, pm_help=None, help_attrs=dict(hidden=True), loop=loop)
        self.ready = None
        self.sqlite_list = kwargs.pop("sqlite_list")
        self.remove_command('help') 
        [self.load_extension(f'command.{c}') for c in ["command"]] 

    async def on_ready(self): 
        try: 
            print(self.user.name, self.user.id) 
            await self.change_presence(activity=Game(name=f"{prefix}help", type=1)) # BOTのステータス変更
        except:
           print("エラー情報\n" + format_exc())
           await bot.get_channel(817964124369584128).send("エラー情報```py\n" + traceback.format_exc() + "\n```")
           return
        self.ready = True


    async def on_command_error(self, ctx, error):
        if not self.ready:
            return
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.NoPrivateMessage):
            return

if __name__ == '__main__':
    main_task = loop.create_task(run())
    loop.run_until_complete(main_task)
    loop.close()