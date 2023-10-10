
api_token = "5009367013:AAHBUvhop5-IzPB2i_EMOaRiDqe9cjVYdTA"

salomlashish = ["salom" ,"assalomu alekum"]
hayrlashish = ["hayr" ,"sog' bo'ling"]

from  aiogram import  Bot , Dispatcher ,executor ,types

bot = Bot(token=api_token)
dp =Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await  message.answer(f"Salom foydalanuvchi!")


@dp.message_handler(content_types="text")
async def test(message: types.Message):
    text = message.text
    text = text.lower()
    if text in salomlashish:
        await message.answer("Assalomu alekum")
    if text in hayrlashish:
        await  message.answer("Salomat bo'ling!")
    if text not in salomlashish and text not in hayrlashish:
        await  message.answer("Boshqa buyruq kiriting!")


if __name__ == "__main__":
    executor.start_polling(dp)
