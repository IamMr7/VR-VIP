from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config
from pyrogram.types import CallbackQuery
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup , ReplyKeyboardRemove
from pyrogram.errors import MessageNotModified

@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/08cec0a2a844713e1624a.jpg",
        caption="Source HMS",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور البوت .", url=config.OWNER_ID),
                ],
                [
                    InlineKeyboardButton(
                        "- قناة البوت . ", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )

@app.on_message(filters.command(["الاوامر"], ""))
async def khalid(client: Client, message: Message):
       await message.reply_text(
                "اليك اوامر البوت عزيزي العضو",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["اوامر 1","اوامر 2"],
                        ["اوامر 3","اوامر 4"],
                        ["اوامر 5","اوامر 6"],
                        ["❎ ¦ حذف الاوامر"]
                    ],
                    resize_keyboard=True
                )
            )  
               
@app.on_message(filters.text, group=39)
async def almortagel(client, message):
   if message.text == "اوامر 1":
       await message.reply_text(f"✅**اوامر الادمن**\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n🎧 | - إليك اوامر التحكم بالمقاطع المشغله ( دآخل المجموعات )  •\n🔻 | - الاوامر تعمل بدون استخدام اي علامات  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ -『 **وقف** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •\n◍ -『 **كمل** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •\n◍ -『 **اسكت** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •\n◍ -『 **اتكلم** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •\n◍ -『 **تخطي** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •\n◍ -『 **ايقاف** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n🎙️ | - إليك اوامر التحكم بالمقاطع المشغله ( دآخل القنوات )  •\n🔻 | - الاوامر تعمل بدون استخدام اي علامات  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ -『 **وقف** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •\n◍ -『 **كمل** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •\n◍ -『 **اسكت** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •\n◍ -『 **اتكلم** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •\n◍ -『 **تخطي** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •\n◍ -『 **ايقاف** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬")
   elif message.text == "اوامر 2":
       await message.reply_text(f"✅<u>**اوامرالتشغيل :**</u>\n🎺 | - اوامر تشغيل البوت في الجروبات والقنوات  •\n🎺 | - الاوامر تعمل بدون استخدام اي علامات  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ - اوامر تشغيل البوت في المجموعات - √\n◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به  •\n◍ -『 **فيديو** 』\n ثم اسم مقطع الفيديو او الرابط الخاص به  •\n◍ -『 **تنزيل** 』\n ثم اسم المقطع المراد تنزيله من موقع اليوتيوب مباشر او الرابط الخاص به  •\n◍ -『 **ريلود** 』\n قم بأرسالها ( دآخل المجموعات ) لتحديث قائمه المشرفين بمجموعتك  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ - **جزء القنوات** - √\n◍ - اوامر تشغيل البوت في القنوات 👇 - √\n◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به لتشغيله بقناتك  •\n◍ -『 **فيديو** 』\nثم اسم الفيديو او الرابط الخاص به لتشغيله بقناتك  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬.")
   elif message.text ==  "اوامر 3":
       await message.reply_text(f"✅**اوامر البوت:**\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n✅ | - إليك قسم ( الاوامر الاضافيه ) للبوت  •\n✅ | - جميع الاوامر تعمل بدون علامات  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ -『 **حدد** 』\n ثم رقم المجموعات الذي تستخدم بوتك فيديو بنفس الوقت •\n◍ -『 **وضع شغل** 』\n لضبط وضع تحكم التشغيل للأدمن او للاعضاء داخل مجموعتك  •\n◍ -『 **القائمه** 』\n لعرض قائمه التشغيل الخاصه بك  •\n◍ -『 **حذف القائمه** 』\n لحذف قائمه التشغيل الخاصه بك  •\n◍ -『 **لغه** 』\n لتغيير لغة البوت إلي اي لغه اخري  •\n◍ -『 **احصائيات** 』\n لعرض قسم الاحصائيات العامه للبوت ولترند التشغيل العالمي •\n◍ -『 **ريلود** 』\n لتحديث قائمة المشرفين داخل مجموعتك •\n◍ -『 **بينج** 』\n لقياس سرعه التشغيل علي السيرفر وعرض تفاصيل معلومات التشغيل •\n◍ -『 **كلمات** 』\n ثم اسم الاغنيه لجلب كلمات الاغنيه كامله بصيغه النصوص •\n◍ -『 **تنزيل** 』\n ثم اسم المقطع او الرابط الخاص به لتحميله مباشر من اليوتيوب •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬")
   elif message.text == "اوامر 4":
       await message.reply_text(f"😜 **ᴀᴜᴛʜ ᴜsᴇʀs**\nᴀᴜᴛʜ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ. [ᴀᴅᴍɪɴs ᴏɴʟʏ]\n/auth [ᴜsᴇʀɴᴀᴍᴇ] : ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜ ʟɪsᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.\n/unauth [ᴜsᴇʀɴᴀᴍᴇ] : ʀᴇᴍᴏᴠᴇ ᴀ ᴀᴜᴛʜ ᴜsᴇʀs ғʀᴏᴍ ᴛʜᴇ ᴀᴜᴛʜ ᴜsᴇʀs ʟɪsᴛ.\n/authusers : sʜᴏᴡs ᴛʜᴇ ᴀᴜᴛʜ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.")
   elif message.text == "اوامر 5":
       await message.reply_text(f"🍒 **<u>ʙʀᴏᴀᴅᴄᴀsᴛ ғᴇᴀᴛᴜʀᴇ</u>** [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :\n/broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.\n<u>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴍᴏᴅᴇs:</u>\n**-pin** : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.\n**-pinloud** : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ sᴇɴᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴇᴍʙᴇʀs\n**-user** : ʙʀᴏᴀᴅᴄᴀsᴛs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.\n**-assistant** : ʙʀᴏᴀᴅᴄᴀsᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀssɪᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.\n**-nobot** : ғᴏʀᴄᴇs ᴛʜᴇ ʙᴏᴛ ᴛᴏ ɴᴏᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ..\n**ᴇxᴀᴍᴩʟᴇ:** `/broadcast -user -assistant -pin ᴛᴇsᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ`")
   elif message.text == "اوامر 6":
       await message.reply_text(f"""
⩹━★⊷⌯⌞ ѕᴏụʀᴄᴇ VR ⌝⌯⊶★━⩺

★قايمه مميزات سورس المرتجل

★ميزه ⦂ المطور بيجيب المطور البوت 
★ميزه ⦂ تبيه بفتح+قفل الكول
★ميزه ⦂ ترحيب دخول و خروج الاعضاء 
★ميزه ⦂ جروب بيجيب الجروب+الرابط+ايدي
★ميزه ⦂ قول البوت بيقول بالكلمه اللي بتقولها 
★ميزه ⦂ الالعاب +كت+تويت+العاب متطوره
★ميزه ⦂ تلغراف ميديا بردعالصوره
★ميزه ⦂ ايدي بالرد بالصوره
★ميزه ⦂ جمالي برد بالصوره ونسبه
★ميزه ⦂ اذاعه خاص+بالتثبيت+بالمساعد+عام
★ميزه ⦂ الصوتيه..ف كول
★ميزه ⦂ نزول تلقائي للمساعد لعدم وجود حد فالكول
★ميزه ⦂ بث مباشر للقنوات 
★ميزه ⦂ اسمي بيجب الاسم
★ميزه ⦂ سورس بيجب السورس
★ميزه ⦂ حظر+كتم ميوزك
★ميزه ⦂ كشف
★ميزه ⦂ تاك لكل الاعضاء
★ميزه ⦂ انا مين
★ميزه ⦂ رتبتي
★ميزه ⦂ مبرمج
★ميزه ⦂ المنشئ+المالك
★ميزه ⦂ الاحصائيات
★ميزه ⦂ كيب المطور من خلاله تتحكم في الحساب المساعد
★ميزه ⦂ الاذكار
★ميزه ⦂ تبيه بوقت صلاه
★ميزه ⦂ دعوه في كول
★ميزه ⦂  دعوه فالخاص بتاع البوت
★ميزه ⦂ تنبيه..بانضمام بوت في الجروبات
★ميزه ⦂ غنيلي 
★ميزه ⦂ بايو
★ميزه ⦂ خروج المساعد من جروبات لعدم تقطيع صوت..البوت
★ميزه ⦂ اسال/اصراحه
★ميزه ⦂ نكت
★ميزه ⦂ ذكاء اصتناعي 
★ميزه ⦂ مميزات. بيجبلك مميزات موجوده فسورس 
★ميزه ⦂ رفع و تنزيل مطور 
★ميزه ⦂ افلام
★ميزه ⦂ مكالمات النشطه+مجموعات البوت شغال فيها
★ميزه ⦂ اساله دينيه
★ميزه ⦂ مين فالكول+بتعرف مين فكول و عددهم
★ميزه ⦂ انا فين+بتجلك جروب
★ميزه ⦂ الرابط+رابط مجموعه
★ميزه ⦂ فنان+اكتب اسم فنان و هتجبلك اغانيه
★ميزه ⦂ اصدار+حول

⩹━★⊷⌯⌞ ѕᴏụʀᴄᴇ VR ⌝⌯⊶★━⩺""")

@app.on_message(filters.command(["❎ ¦ حذف الاوامر"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الاوامر بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )
