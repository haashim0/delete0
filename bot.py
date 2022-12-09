import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID", "25774553"))
API_HASH = environ.get("API_HASH", "331e36e1cb1263f72da71db7d291ed4a")
BOT_TOKEN = environ.get("BOT_TOKEN", "5724620740:AAHogMBJ7tcnmw-tzpz-76GrBql2FP_iObU")
SESSION = environ.get("SESSION", "BQCDcajqMTofzc-IIPKpPxGKTkgl_Ex5hdyTrKw0rbzyTrYOBh6d8B6eqG9Z7SUvp4smJVJ8JorJVGSuR4IAslwjGR0RxrtTedt02-1vkbdlB1aFw5ZxtGRuV7y6R71F4ZJPDH73gpWAHw-fPZpGaCnWTDwgZvfoJQ4BZdMW2wNvbvUZyA61QqtlNLsyBcbDOXobOSe_A_ZPRIyIlDmnmoiDw9YqahLCqcFMix0j1gx0gRSEoxPM157f7FcDps7rnMxfYfavUD-8bKUXbA3E3OINRbX4Gd6CveqjVoxWWZkP2CR31gnWQtqPsxUn-A21Oi_lUEZD_V7L0BcyQECigAPuAAAAAVabUgAA")
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
