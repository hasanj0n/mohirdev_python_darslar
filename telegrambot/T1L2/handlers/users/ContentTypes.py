from aiogram.dispatcher.filters.builtin import ContentTypeFilter
from aiogram import  types
from loader import  dp
# Text
# @dp.message_handler(content_types='text')
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def text(message:types.Message):
    await message.answer('Text yubordiz')


#Rasm
# @dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo(message:types.Message):
    await message.answer('Rasm yubordiz')

#Audio
# @dp.message_handler(content_types='audio')
@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def audio(message:types.Message):
    await message.answer('Audio yubordiz')

#Video
# @dp.message_handler(content_types='video')
@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def video(message:types.Message):
    await message.answer('Video yubordiz')

#Document
# @dp.message_handler(content_types='document')
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document(message:types.Message):
    await message.answer('Document yubordiz')

#Sticker
# @dp.message_handler(content_types='sticker')
@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def document(message:types.Message):
    await message.answer('Sticker yubordiz')