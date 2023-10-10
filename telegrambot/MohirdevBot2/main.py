"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from OxfordLookUp import getDefinitions
from  googletrans import  Translator
translator =Translator()

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5553111122:AAGp7asLuP48i0th_nCnlaU2HnQIZkl26tA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alekum, botga xush kelibsiz!")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Bu o'zbekcha va inglizcha so'zlarni inglizcha tavsifi va tallafuzini qaytaruvchi yoki matnlarni tarjima qiluvchi bot!")



@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) >2:
        dest = "uz" if lang == "en" else "en"
        await message.reply(translator.translate(message.text, dest).text)

    else :
        if lang == "en":
            word_id = message.text
        else:
            word_id = translator.translate(message.text,dest="en").text

        lookup =getDefinitions(word_id)
        if lookup:
            await  message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get("audio"):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z mavjud emas!")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)