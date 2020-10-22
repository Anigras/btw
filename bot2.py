#! /usr/bin/python3
# -*- python -*-
# -*- coding: utf-8 -*-



import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


API_TOKEN = '1309274489:AAH1_2ATQJ1B7N6vDTDDzpf_76UuIGp9q30'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["help"])
async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="/dz"))
    poll_keyboard.add(types.KeyboardButton(text="/kr"))
    poll_keyboard.add(types.KeyboardButton(text="/x"))
    poll_keyboard.add(types.KeyboardButton(text="Отмена"))
    poll_keyboard.add(types.KeyboardButton(text="Я узнал все что надо"))
    await message.answer("Выбери нужную команду", reply_markup=poll_keyboard)

@dp.message_handler(lambda message: message.text == "Отмена")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer("Не хочешь разговаривать ну и не надо!!!!      (；⌣̀_⌣́)", reply_markup=remove_keyboard)


@dp.message_handler(lambda message: message.text == "Я узнал все что надо")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer("Молодец))   ヽ(・∀・)ﾉ", reply_markup=remove_keyboard)

@dp.message_handler(commands=['Dz',])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nГеография:(classroom)\nАлгебра(л):\nАлгеба(пр):\nГеометрия(л):\nГеометрия(пр):\nМат.анализ(л):\nМат.анализ(пр): \nФизика: вправа 8\nЗар.лит:ст.53-65;53,57-58;53-55,59\nУкр.лит:\nИстория всес:\nИстория Укр.:\nУкр.мова: \nБиология:\nИнфа:\nХимия:\nМист.:\nАнгл.мова:")


@dp.message_handler(commands=['kr'])
async def cats(message: types.Message):
    
        await message.reply("Пн:\n𝒩𝑜\nВт:\n𝒩𝑜\nСр:Диктант по англ;Олимпиада по физике\n𝒩𝑜\nЧт:\n𝒩𝑜\nПт:\n𝒩𝑜\nСб:\n𝒩𝑜")


@dp.message_handler(commands=['Паша'])
async def cats(message: types.Message):
    
        await message.reply("Бака")

@dp.message_handler(commands=['Даниил'])
async def cats(message: types.Message):
    
        await message.reply("Семпай Пинки")

@dp.message_handler(commands=['Финик'])
async def cats(message: types.Message):
    
        await message.reply("47 хромосомик")

@dp.message_handler(commands=['Александра'])
async def cats(message: types.Message):
    
        await message.reply("ХЗХЗХЗХХЗХЗХЗ")

@dp.message_handler(commands=['Гусь'])
async def cats(message: types.Message):
    
        await message.reply("Гусь")

@dp.message_handler(commands=['КК'])
async def cats(message: types.Message):
    
        await message.reply("Ну типо брат")

@dp.message_handler(commands=['КД'])
async def cats(message: types.Message):
    
        await message.reply("Ну типо брат брата")

@dp.message_handler(commands=['Радиатор'])
async def cats(message: types.Message):
    
        await message.reply("Принцеса")

@dp.message_handler(commands=['Есения'])
async def cats(message: types.Message):
    
        await message.reply("типа тупая")

@dp.message_handler(commands=['Соня'])
async def cats(message: types.Message):
    
        await message.reply("Ходячая википедия")

@dp.message_handler(commands=['Антон'])
async def cats(message: types.Message):
    
        await message.reply("АНТОН САМ ПРИДУМАЙ Я ХЗ ЧТО ПИСАТЬ")

@dp.message_handler(commands=['Ева'])
async def cats(message: types.Message):
    
        await message.reply("Хз что написать,но рисует на тетрадке")

@dp.message_handler(commands=['Вика'])
async def cats(message: types.Message):
    
        await message.reply("Вестник")

@dp.message_handler(commands=['Софа'])
async def cats(message: types.Message):
    
        await message.reply("Хз че писать")

@dp.message_handler(commands=['Певец'])
async def cats(message: types.Message):
    
        await message.reply("Маленький поздюк")

@dp.message_handler(commands=['x'])
async def cats(message: types.Message):
    
        await message.reply("КК\nКД\nФиник\nВика\nПевец\nСофа\nЕва\nАнтон\nСоня\nЕсения\nРадиатор\nГусь\nАлександра\nДаниил\nПаша")

@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
    

        await message.reply_photo(photo, caption='Cats are here 😺')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)