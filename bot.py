from pyrogram import Client, filters
from config import APP_ID, API_HASH, BOT_TOKEN, KANAL, KANALIM

Bot = Client("kanalkopy", api_id=APP_ID, api_hash=API_HASH, session_string=BOT_TOKEN)
owner = "mmagneto"

@Bot.on_message(filters.incoming & filters.chat(KANAL))
async def kopy(bot, message):
    try:
        await bot.send_message(owner, "`Yeni Mesaj Gönderildi`")
        await bot.copy_message(
            chat_id = KANALIM,
            from_chat_id = KANAL,
            message_id = message.id)
    except Exception as e:
        print(e)

Bot.run()
