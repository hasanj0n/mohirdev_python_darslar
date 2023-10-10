from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = "5575489890:AAGcfNmsSQ7qILqJdrRPsyaUk_zltANouFk"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalom alekum, Xush Kelibsiz"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)    

bot.infinity_polling()


