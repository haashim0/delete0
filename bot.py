import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "25774553"))
API_HASH = environ.get("API_HASH", "331e36e1cb1263f72da71db7d291ed4a")
BOT_TOKEN = environ.get("BOT_TOKEN", "5724620740:AAHogMBJ7tcnmw-tzpz-76GrBql2FP_iObU")
SESSION = environ.get("SESSION", "BQCWSID5_7Mnh80G_DTmTbbwfFB2GCLC_SWFYCshH0cwXYsI2QcQq9xi05TE9pwORrQu3wqERA0noUlxlzKHW7Wv-zu6S3Uj7OQcWX4AZmi3fpGsKUXvGAH_U2NZhkqb-U8FcAeneZz3Ws0MG8rdsnWRvHlZdfn391Jh9vJME4wIiUnL2_arwkg5N-GOf66lPRrsbTa9rEhvhp1G8S_P-4ltggdokQCR8q1durZAwNav_0mYQKHPmiJiaT7xtN05AIkd7TDB4yoRsWZHKEM79OaGAg9waPEVJYi4LzZ03DllXV-FbISvxYVSsZlEbdbW5Md_VbiJ80T1WHxijNKoHjUZAAAAAVabUgAA")
TIME = int(environ.get("TIME", "7200"))
GROUPS = []
for grp in environ.get("GROUPS", "-1001754707385").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS", "5291606032").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hᴇʟʟᴏ {}\n\nI ᴏɴʟʏ sᴜᴘᴘᴏʀᴛ ᴛʜᴇ</b> <a href='http://telegram.me/TamilDub_Linkzz'><b>TᴀᴍɪʟDᴜʙ_Lɪɴᴋᴢᴢ</b></a> <b>ɢʀᴏᴜᴘ\n\nI ᴅᴏ ɢʀᴏᴜᴘ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴄʟᴇᴀɴɪɴɢ ᴇᴠᴇʀʏ 𝟸 ʜᴏᴜʀs</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
