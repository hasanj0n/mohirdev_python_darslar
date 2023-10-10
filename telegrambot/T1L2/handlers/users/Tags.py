from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import  types
from loader import  dp

@dp.message_handler(hashtags='ok')
async def hashtag(message:types.Message):
    await message.answer("Omonov Hashtag")

@dp.message_handler(cashtags=['ok'])
async def cashtag(message:types.Message):
    await message.answer("Omonov Cashtag")