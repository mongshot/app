import telegram
import asyncio

TELEGRAM_BOT_TOKEN = '6384605708:AAEzqbyJnXu0yAdNFZvUBaK8fcpTEvseuNo'
TELEGRAM_CHAT_ID = '71046013'

async def send_telegram_message(message):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# 메시지 보내기
asyncio.run(send_telegram_message("Hello"))