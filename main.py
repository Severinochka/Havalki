import telebot
from telebot import types
import sqlite3

connect = sqlite3.connect('test1.db')
cursor = connect.cursor()

connect.execute('CREATE TABLE if NOT EXISTS {}(language TEXT,places TEXT,types TEXT,price TEXT, addresses TEXT UNIQUE)'.format('test'))
def test_db():

    
    test_list = ['русский', 'Ломоносова 9', 'Азия', 'до 300(чисто перекусить)', 'Kimchi to go (Загородный пр. 21-23)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Азия', 'до 300(чисто перекусить)', 'Bomu (Ломономова 26)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Азия', 'до 700 (хочу нормально покушать)', 'Joly Woo (Загородный пр. 9)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Азия', '1000 и больше (сегодня шикуем)', 'Spar (Владимирский пр. 19)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Азия', 'до 700(хочу нормально покушать)', 'Chou Do (Загородный пр. 2)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Европа', 'до 700 (хочу нормально покушать)', 'Mama Roma (Загородный пр. 21-23)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Европа', 'до 300(чисто перекусить)', "Angel's coffee (Ломоносова 9а)"]
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Европа', 'до 300(чисто перекусить)', 'Spar (Владимирский пр. 19)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Европа', 'до 700(хочу нормально покушать)', 'Хачо и Пури (Загородный пр. 13)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Европа', 'до 700(хочу нормально покушать)', 'ЦЕХ 85 ()']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Америка', '1000 и больше (сегодня шикуем)', 'Burger&Crabs (Рубенштейна 29/28)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Америка', '1000 и больше (сегодня шикуем)', 'Frank (Ломоносова 28)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Америка', 'до 300(чисто перекусить)', 'KFC (Загородный пр. 2)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Россия', 'до 300(чисто перекусить)', 'Теремок (Загородный пр. 18)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Россия', 'до 300(чисто перекусить)', 'Вольчек (Разъезжая 1)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Россия', 'до 300(чисто перекусить)', 'Falafel King (Загородный пр. 20)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Ломоносова 9', 'Россия', 'до 300(чисто перекусить)', 'Пироговый дворик (Разъезжая 6)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()

    test_list = ['русский', 'Кронверкский пр. 49', 'Россия', 'до 300(чисто перекусить)', 'Вольчек (Сытнинская 10)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Кронверкский пр. 49', 'Россия', 'до 300(чисто перекусить)', 'Теремок (Кронверкский пр. 47)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Кронверкский пр. 49', 'Россия', 'до 700(хочу нормально покушать)', 'Отменная Пельменная (Маркина 4)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Кронверкский пр. 49', 'Россия', 'до 300(чисто перекусить)', 'Cous-Cous (Кропоткина 19/8)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Кронверкский пр. 49', 'Россия', 'до 300(чисто перекусить)', 'PeliBox (Александровский парк 4к3)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Кронверкский пр. 49', 'Европа', 'до 700(хочу нормально)', 'ЦЕХ 85 (Воскова 27/18)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Кронверкский пр. 49', 'Европа', '1000 и больше(сегодня шикуем)', 'Тбилисо (Сытнинская 10)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Кронверкский пр. 49', 'Европа', 'до 700(хочу нормально покушать)', "Pita's (Кронверкский пр. 23)"]
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Кронверкский пр. 49', 'Америка', 'до 300(чисто перекусить)', 'Burger King (Александровский парк 4к3)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()

    test_list = ['русский', 'Биржевая 16', 'Россия', 'до 300(чисто перекусить)', 'Express Столовая (Биржевой пер. 2)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Россия', 'до 300(чисто перекусить)', 'Вольчек (1-ая линия ВО 46)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Россия', 'до 700(хочу нормально покушать])', 'Пильмения (Средний пр. ВО 11)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Россия', 'до 700(хочу нормально покушать)', 'Бутерbrodsky (наб. Макарова 16)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Азия', 'до 700(хочу нормально покушать)', 'Koreana light (Средний пр. ВО 11)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Азия', 'до 700(хочу нормально покушать)', '7 специй (Средний пр. ВО 13)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Азия', 'до 700(хочу нормально покушать)', 'Spar (2-я линия ВО 39/16)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Азия', 'до 700(хочу нормально покушать)', 'Tokyo City (Средний пр. ВО 34)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Европа', 'до 700(хочу нормально покушать)', 'ДоДо (6-я линия ВО 25)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Европа', 'до 700(хочу нормально покушать)', 'Spar (2-я линия ВО 39/16)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Европа', '1000 и больше(сегодня шикуем)', 'Brasserie Kriek (6-я линия ВО 25)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Европа', 'до 700(хочу нормально покушать)', 'Mama Roma (Средний пр. ВО 6)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Европа', 'до 700(хочу нормально покушать)', 'Хачапури & Вино (Кадетская линия ВО 29)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()
    test_list = ['русский', 'Биржевая 16', 'Америка', 'до 300(чисто перекусить)', 'KFC (Средний пр. ВО 36/40)']
    cursor.execute("INSERT INTO test VALUES(?,?,?,?,?);", test_list)
    connect.commit()

#test_db EVER NEVER WOULD BE USED

bot = telebot.TeleBot('5387905202:AAG4T-JsodA7N4XVUymI6HeUMuNNeNS-eBQ')
@bot.message_handler(commands=['start'])
def start(m, res=False):

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ломо")
        item2=types.KeyboardButton("Кронва")
        item3=types.KeyboardButton("Биржа")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, text='Выбери адрес, где ты сейчас находишься',  reply_markup = markup)

bot.polling()
