from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["اوامر", "الاوامر"])
)
async def mmmezat(client, message):
    await message.reply_text(
        f"""╭── • تحديثات اليس • ──╮

 • اوامر التشغيل بالمجموعة

• تشغيل + اسم الاغنية او بالرد 
-› لتشغيل الاغاني فالمجموعة

• رعد طفيها او  ايقاف
-› لايقاف تشغيل جميع الصوتيات بالمكالمة

• اليس الي بعده او تخطي
-› لتشغيل التالي بالانتظار

 • اليس وقفي او اسكتي
-› لكتم صوت الحساب المساعد بالمكالمة

• اليس اتكلمي
-› لالغاء الكتم واكمال التشغيل

• اليس اسكتي او ايقاف مؤقت
 -› لايقاف التشغيل بشكل مؤقت

• اليس كملي او استئناف
 -› لاكمال التشغيل بعد الايقاف المؤقت

╰── • تحديثات اليس • ──╯ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- المطور .", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- مسح .", callback_data="close"
                    ),
                ],
            ]
        ),
    )

@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/652fd5d4587fd12d49544.jpg",
        caption="~ Team \n~ Dav Source",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور البوت .", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- قناة البوت . ", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
