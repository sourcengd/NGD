import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/94df5f4f55429ace85e01.jpg",
        caption = f"""<b>  𝒘𝒆𝒍𝒄𝒐𝒎𝒆𝒖 𝒕𝒐 <b>\n<a href="https://t.me/ngd_1"> 𝒔𝒐𝒖𝒓𝒄𝒆 𝐚𝐥𝐢𝐜𝐞🥂</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "  𝒅𝒆𝒗 𝒔𝒐𝒖𝒓𝒄𝒆 ", url=f"https://t.me/ngd_2"),
                ],[
                    
                
                    InlineKeyboardButton(
                        " 𝒔𝒐𝒖𝒓𝒄𝒆 𝐚𝐥𝐢𝐜𝐞🥂", url=f"https://t.me/ngd_1"),         
                ],

            ]

        ),

    )
