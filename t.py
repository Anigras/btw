import config
import telebot

from telebot import types


bot = telebot.TeleBot('config.TOKEN')


@bot.message_handler(commands=['start'])
def gg(message):
	sti = open('static/gg.webp', 'rb')
	bot.send_message(message.chat.id, "GG, {0.first_name}!\nЯ - <b>{1.first_name}</b>, WP".format(messahe.from_user, bot.get_me()) 
		parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):


	markup = types.InlineKeyboardMarkup(row_width=2)
	item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
	item2 = types.InlineKeyboardButton("НЕ очень", callback_data='bad')

	markup.add(item1, item2)

@bot.callback_query_handler(func=lamba call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'ЮХу')
			elif call.data =='bad':
				bot.send_message(call.message.chat.id, '((((')
	bot.send_message(message.chat.id, 'Отлично', peply_markup=markup)

bot.polling(none_stop=True)