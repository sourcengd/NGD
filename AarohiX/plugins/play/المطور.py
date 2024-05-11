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

╰── • تحديثات اليس • ──╯ """,),
    )

@app.on_message(command(["مطور", "المطور"]))
async def devid(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    uid = OWNER_ID
    await app.download_media(usr.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
       
    await message.reply_photo(
        photo="downloads/developer.jpg",
        caption=f"""<b>𝑛𝑎𝑚𝑒 :</b> <a href='tg://user?id={uid}'>{name}</a>\n\n<b>𝑢𝑠𝑒𝑟 :</b> @{usrnam}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(name, url=f"tg://user?id={uid}"),
                ],[
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
                ],
            ]
        ),
    )
