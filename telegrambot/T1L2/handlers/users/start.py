from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.builtin import Command

from loader import dp



@dp.message_handler(CommandStart(deep_link='kunuz'))
async def start_link(message: types.Message):
    await message.answer(f"Salom,kunuz royxatdan otdiz!")

# https://t.me/fullteachbot?start=kunuz
#https://t.me/fullteachbot?start=daryouz
@dp.message_handler(CommandStart(deep_link='daryouz'))
async def start_link2(message: types.Message):
    await message.answer(f"Salom,daryouz royxatdan otdiz!")

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

# @dp.message_handler(commands='fullteach')
@dp.message_handler(Command('fullteach'))
async def fullteach(message:types.Message):
    await message.answer('Full Teach Academy')