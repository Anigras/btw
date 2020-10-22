import telebot
import config
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Отмена")
    item2 = types.KeyboardButton("Commands")
    item3 = types.KeyboardButton("Я узнал все что надо")
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "ПРив, {0.first_name}!\nЯ - <b>{1.first_name}</b>, созданная Даняй 'Семпаем'.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup,)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Отмена':
            markup = types.InlineKeyboardMarkup(row_width=1)
            item0 = types.InlineKeyboardButton("Да", callback_data='gg')
            item4 = types.InlineKeyboardButton("Нет", callback_data='g')
            markup.add(item0, item4)
 
            bot.send_message(message.chat.id, 'Уверен в своем выборе?  (︶︹︺) ', reply_markup=markup)

        if message.text == 'Я узнал все что надо':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item5 = types.InlineKeyboardButton("Да", callback_data='yes')
            item6 = types.InlineKeyboardButton("Нет", callback_data='no')
            markup.add(item5, item6)
 
            bot.send_message(message.chat.id, 'Я тебе помогла? (◕‿◕✿)', reply_markup=markup)
        
        elif message.text == 'Commands':
 
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("/dz", callback_data='good')
            item2 = types.InlineKeyboardButton("/x", callback_data='bad')
            item3 = types.InlineKeyboardButton("/kr", callback_data='notbade')

            markup.add(item1, item2, item3)
 
            bot.send_message(message.chat.id, 'Выбери команду малец   (づ ◕‿◕ )づ', reply_markup=markup)
 

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, '"Hi!\nГеография:(classroom)\nАлгебра(л):\nАлгеба(пр):\nГеометрия(л):\nГеометрия(пр):\nМат.анализ(л):\nМат.анализ(пр): \nФизика: вправа 8\nЗар.лит:ст.53-65;53,57-58;53-55,59\nУкр.лит:\nИстория всес:\nИстория Укр.:\nУкр.мова: \nБиология:\nИнфа:\nХимия:\nМист.:\nАнгл.мова:")')
            if call.data == 'notbade':
                bot.send_message(call.message.chat.id, 'Пн:\n𝒩𝑜\nВт:\n𝒩𝑜\nСр:Диктант по англ;Олимпиада по физике\n𝒩𝑜\nЧт:\n𝒩𝑜\nПт:\n𝒩𝑜\nСб:\n𝒩𝑜')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'КК\nКД\nФиник\nВика\nПевец\nСофа\nЕва\nАнтон\nСоня\nЕсения\nРадиатор\nГусь\nАлександра\nДаниил\nПаша')
            if call.data == 'g':
                bot.send_message(call.message.chat.id, 'Не хочешь разговаривать ну и не надо!!!!      (；⌣̀_⌣́)')
            if call.data == 'gg':
                bot.send_message(call.message.chat.id, 'Так то лучше    (o^▽^o)')
            if call.data == 'no':
                bot.send_message(call.message.chat.id, '。゜゜(´Ｏ) ゜゜。')
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, '(─‿‿─)♡')


            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Я узнал все что надо",
                reply_markup=None)
            # remove inline buttons
 
            markup1 = types.ReplyKeyboardMarkup(one_time_keyboard = False)
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="'Дин Дон'")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
