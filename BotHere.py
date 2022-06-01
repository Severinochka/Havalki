import aiogram
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import sqlite3

connect = sqlite3.connect('test1.db')
cursor = connect.cursor()

connect.execute('CREATE TABLE if NOT EXISTS {}(language TEXT,places TEXT,types TEXT,price TEXT, addresses TEXT UNIQUE)'.format('test'))

Bot = aiogram.Bot
bot = Bot('5387905202:AAG4T-JsodA7N4XVUymI6HeUMuNNeNS-eBQ')
dp = aiogram.Dispatcher(bot)


# KEYBOARD
main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button = types.KeyboardButton("I wanna eat!!")
buttom = types.KeyboardButton("Я хочу есть!!")
main_keyboard.add(button, buttom)

second_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  #, one_time_keyboard=True
lomo = types.KeyboardButton("Ломоносова 9")
kronva = types.KeyboardButton("Кронверкский пр. 49")
birja = types.KeyboardButton("Биржевая линия 16")
second_keyboard.add(lomo, kronva, birja)

third_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  #, one_time_keyboard=True
asia = types.KeyboardButton("Азия")
europa = types.KeyboardButton("Европа")
usa = types.KeyboardButton("Америка")
russia = types.KeyboardButton("Россия")
third_keyboard.add(asia, europa, usa, russia)

fourth_main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
rub300 = types.KeyboardButton('до 300(чисто перекусить)')
rub700 = types.KeyboardButton('до 700(хочу нормально покушать)')
rub1000 = types.KeyboardButton('1000 и больше(сегодня шикуем)')
fourth_main_keyboard.add(rub300, rub700, rub1000)

fifth_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  #, one_time_keyboard=True
mainMenu = types.KeyboardButton("Вернуться в главное меню")
# temp = types.KeyboardButton("Добавить новое заведение")
fifth_keyboard .add(mainMenu) #, temp

###

second_keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  #, one_time_keyboard=True
lomo1 = types.KeyboardButton("Lomonosova street 9")
kronva1 = types.KeyboardButton("Kronverksky ave. 49")
birja1 = types.KeyboardButton("Birzhevaya line 16")
second_keyboard1.add(lomo1, kronva1, birja1)

third_keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  #, one_time_keyboard=True
asia1 = types.KeyboardButton("Asia")
europa1 = types.KeyboardButton("Europe")
usa1 = types.KeyboardButton("America")
russia1 = types.KeyboardButton("Russia")
third_keyboard1.add(asia1, europa1, usa1, russia1)

fourth_main_keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
rub3001 = types.KeyboardButton('up to 300 rub(just a snack)')
rub7001 = types.KeyboardButton('up to 700 rub(wanna eat well)')
rub10001 = types.KeyboardButton('1000 rub and more(today we are chic)')
fourth_main_keyboard1.add(rub3001, rub7001, rub10001)

fifth_keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)  #, one_time_keyboard=True
mainMenu1 = types.KeyboardButton("Return to main menu")
# temp1 = types.KeyboardButton("Add a new establishment")
fifth_keyboard1.add(mainMenu1) #, temp1


#


@dp.message_handler(commands=["start"])
async def start(message: aiogram.types.message):
    await message.answer("Приветики-пистолетики всем голодным и не очень:)\nКак ты?\n\nHey, there  to all the hungry and not so:)\nHow are you?", reply_markup=main_keyboard)

@dp.message_handler(text=["Вернуться в главное меню"])
async def start(message: aiogram.types.message):
    await message.answer("Приветики-пистолетики всем голодным и не очень:)\nКак ты?\n\nHey, there  to all the hungry and not so:)\nHow are you?", reply_markup=main_keyboard)

@dp.message_handler(text=["Return to main menu"])
async def start(message: aiogram.types.message):
    await message.answer("Приветики-пистолетики всем голодным и не очень:)\nКак ты?\n\nHey, there  to all the hungry and not so:)\nHow are you?", reply_markup=main_keyboard)

@dp.message_handler(text="Я хочу есть!!") #, one_time_keyboard=True
async def eat1(message: aiogram.types.message):
    await message.reply("Не смею более задерживать.\nВыбери адрес, где ты находишься:", reply_markup=second_keyboard)

    @dp.message_handler(text="Ломоносова 9")
    async def lmn(mes: aiogram.types.message):
        await mes.reply("Какую кухню предпочтешь?", reply_markup=third_keyboard)
        @dp.message_handler(text="Азия")
        async def ai(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)
            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:", reply_markup=fifth_keyboard)
                res = cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Азия" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res = cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Азия" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Азия" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Европа")
        async def eu(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Европа" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Европа" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Европа" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Америка")
        async def am(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Америка" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Америка" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Америка" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Россия")
        async def ru(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Россия" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Россия" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Ломоносова 9" AND types="Россия" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

    @dp.message_handler(text=["Кронверкский пр. 49"])
    async def krn(message: aiogram.types.message):
        await message.reply("Какую кухню предпочтешь?", reply_markup=third_keyboard)
        @dp.message_handler(text="Европа")
        async def eu(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Европа" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Европа" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Европа" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Азия")
        async def ai(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)
            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Азия" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Азия" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Азия" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Америка")
        async def am(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Америка" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Америка" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Америка" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Россия")
        async def ru(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Россия" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Россия" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Кронверкский пр. 49" AND types="Россия" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

    @dp.message_handler(text=["Биржевая линия 16"])
    async def brj(message: aiogram.types.message):
        await message.reply("Какую кухню предпочтешь?", reply_markup=third_keyboard)
        @dp.message_handler(text="Европа")
        async def eu(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Европа" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Европа" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Европа" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Азия")
        async def ai(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)
            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Азия" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Азия" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Азия" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Америка")
        async def am(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Америка" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Америка" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Америка" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

        @dp.message_handler(text="Россия")
        async def ru(mess: aiogram.types.message):
            await mess.reply("Насколько ты готов раскошелиться??", reply_markup=fourth_main_keyboard)

            @dp.message_handler(text="до 300(чисто перекусить)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("Лааадно, нищеброд)) Вот тебе списочек:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Россия" AND price="до 300(чисто перекусить)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="до 700(хочу нормально покушать)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Воу! Да мы серьезно настроены))0)")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Россия" AND price="до 700(хочу нормально покушать)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)

            @dp.message_handler(text="1000 и больше(сегодня шикуем)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("Не знали, что у студентов есть столько денег...\nПредлагаем Вам следующие заведения:")
                res=cursor.execute(f'SELECT addresses FROM test WHERE places="Биржевая линия 16" AND types="Россия" AND price="1000 и больше(сегодня шикуем)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("Прости, но мы не знаем о таком месте:(")
                @dp.message_handler(text="Вернуться в главное меню")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard)


@dp.message_handler(text=["Return to main menu"])
async def start(message: aiogram.types.message):
    await message.answer("Приветики-пистолетики всем голодным и не очень:)\nКак ты?\n\nHey, there  to all the hungry and not so:)\nHow are you?", reply_markup=main_keyboard)

@dp.message_handler(text="I wanna eat!!")  # , one_time_keyboard=True
async def eat2(message: aiogram.types.message):
    await message.reply("I dare not delay any longer.\n Pick an address where you are located:", reply_markup=second_keyboard1)

    @dp.message_handler(text="Lomonosova street 9")
    async def lmn(mes: aiogram.types.message):
        await mes.reply("What kind of cuisine do you prefer?", reply_markup=third_keyboard1)

        @dp.message_handler(text="Asia")
        async def ai(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=fourth_main_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(f'SELECT addresses FROM eeng WHERE places="Lomonosova street 9" AND types="Asia" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)

            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="Asia" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything :(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic)")
            async def vip(messa: aiogram.types.message):
                await messa.reply("We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="Asia" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)

        @dp.message_handler(text="Europe")
        async def eu(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=fourth_main_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="Europe" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="Europe" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic)")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="Europe" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


        @dp.message_handler(text="America")
        async def am(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=fourth_main_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="America" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="America" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic)")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="America" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


        @dp.message_handler(text="Russia")
        async def ru(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=fourth_main_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="Russia" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="Russia" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic)")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Lomonosova street 9" AND types="Russia" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


    @dp.message_handler(text=["Kronverksky ave. 49"])
    async def krn(message: aiogram.types.message):
        await message.reply("What kind of cuisine do you prefer?")

        @dp.message_handler(text="Asia")
        async def ai(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=third_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places=""Kronverksky ave. 49"" AND types="Asia" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="Asia" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic)")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="Asia" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


        @dp.message_handler(text="Europe")
        async def eu(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=third_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="Europe" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="Europe" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic))")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="Europe" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


        @dp.message_handler(text="America")
        async def am(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=third_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="America" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="America" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic))")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="America" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


        @dp.message_handler(text="Russia")
        async def ru(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=third_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="Russia" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="Russia" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic))")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Kronverksky ave. 49" AND types="Russia" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


    @dp.message_handler(text=["Birzhevaya line 16"])
    async def krn(message: aiogram.types.message):
        await message.reply("What kind of cuisine do you prefer?")

        @dp.message_handler(text="Asia")
        async def ai(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=fourth_main_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Asia" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Asia" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic))")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Asia" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


        @dp.message_handler(text="Europe")
        async def eu(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=fourth_main_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Europe" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Europe" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic))")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Europe" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


        @dp.message_handler(text="America")
        async def am(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=fourth_main_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="America" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="America" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic))")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="America" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


        @dp.message_handler(text="Russia")
        async def ru(mess: aiogram.types.message):
            await mess.reply("How much are you willing to shell out?", reply_markup=fourth_main_keyboard1)

            @dp.message_handler(text="up to 300 rub(just a snack)")
            async def trista(messa: aiogram.types.message):
                await messa.reply("All right, pauper)) Here's a list for you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Russia" AND price="up to 300 rub(just a snack)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="up to 700 rub(wanna eat well)")
            async def sem(messa: aiogram.types.message):
                await messa.reply("Whoa! We're serious about this))0)")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Russia" AND price="up to 700 rub(wanna eat well)"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)


            @dp.message_handler(text="1000 rub and more(today we are chic))")
            async def vip(messa: aiogram.types.message):
                await messa.reply(
                    "We didn't know students had so much money...\nThe following establishments are available to you:")
                res = cursor.execute(
                    f'SELECT addresses FROM test WHERE places="Birzhevaya line 16" AND types="Russia" AND price="1000 rub and more(today we are chic))"').fetchall()
                for i in res:
                    for j in i:
                        await messa.answer(j)
                if not res:
                    await messa.answer("I'm sorry, sweetie, but we didn't find anything:(")
                @dp.message_handler(text="Return to main menu")
                async def back(messag: aiogram.types.message):
                    await messag.answer(" ", reply_markup=fifth_keyboard1)





#///////////////////
#     @dp.message_handler(text=["я не пистолетик"])
#     async def start(message: aiogram.types.message):
#         await message.reply("secret")
#
#     @dp.message_handler(text=["secret"])
#     async def start(message: aiogram.types.message):
#         await message.reply("secret")
#
# @dp.message_handler (text=["start", "вернуться в главное меню"])
# async def start(message: aiogram.types.message):
#     await message.reply("Приветики-пистолетики, всем голодныи и не оч123456ень")
#
#
# @dp.message_handler(not())
# async def none(message: aiogram.types.message):
#     await message.reply("Прости, но мы ничего не нашли")



if __name__ == "__main__":
    aiogram.executor.start_polling(dp, skip_updates=True)
