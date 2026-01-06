import os
import telebot
from telebot import types
from datetime import datetime

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(
        "📞 Telefon raqamni yuborish",
        request_contact=True
    )
    kb.add(btn)

    bot.send_message(
        message.chat.id,
        "Assalomu alaykum!\n\n"
        "Buyurtma berish uchun telefon raqamingizni yuboring 👇",
        reply_markup=kb
    )

@bot.message_handler(content_types=['contact'])
def get_contact(message):
    phone = message.contact.phone_number
    name = message.contact.first_name
    time = datetime.now().strftime("%d.%m.%Y %H:%M")

    bot.send_message(
        ADMIN_ID,
        f"📦 YANGI BUYURTMA\n\n"
        f"👤 Ism: {name}\n"
        f"📞 Telefon: {phone}\n"
        f"🕒 Vaqt: {time}"
    )

    bot.send_message(
        message.chat.id,
        "✅ Rahmat! Buyurtmangiz qabul qilindi.\n"
        "Tez orada siz bilan bog‘lanamiz."
    )

bot.polling(none_stop=True)

# redeploy

