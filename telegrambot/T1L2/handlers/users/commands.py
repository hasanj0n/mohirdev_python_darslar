from aiogram.dispatcher.filters.builtin import Command,CommandPrivacy,CommandSettings
from aiogram import  types
from  loader import  dp

@dp.message_handler(CommandSettings())   # /settings Komandasi
async def settings(message:types.Message):
    await message.answer('Sozlamalar bolimi')
@dp.message_handler(commands='welcome')
async def welcome(message:types.Message):
    await message.answer("Welcome")
# https://t.me/fullteachbot?start=kunuz
#https://t.me/fullteachbot?start=daryouz
