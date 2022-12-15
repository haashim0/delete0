import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "25774553"))
API_HASH = environ.get("API_HASH", "331e36e1cb1263f72da71db7d291ed4a")
BOT_TOKEN = environ.get("BOT_TOKEN", "5724620740:AAHogMBJ7tcnmw-tzpz-76GrBql2FP_iObU")
SESSION = environ.get("SESSION", "BQCZyijlx83gjfL5cCZHI_vt3nJu70m6VqBVOoVY-MEVcCokeMADRL-f8ThMfP-m5Xm0GLvXB2TtwHsn4k3VWlYujysbrcwi5DUWnavl5dS4bTl0yCi6q7Ey15DlQ3c8ERaynMHUJ59cRNOnPokyVrJ8niGyH484biyFYRWVigle74yFjyAYMMLrduR5kxC9iwGzIX5j3w12WtR-g7DsnphompC5OB-aPyBUmOUSrd3WL6vEldSKyTE0TynDNt7wEJTGQzALjAfxq3Uyke2V4RR5PIRyuVAuSlag6xq_IaEwXGJFSWabsnWUtdWTWupVO4pP7WOQf1qA-LIb8Kzkt3Q1AAAAAVabUgAA")
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
