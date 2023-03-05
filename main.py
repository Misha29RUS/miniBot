import telebot
from telebot import types
from time import sleep
import sqlite3

bot = telebot.TeleBot('5818550349:AAF4vY8XTiogETFKsVoMZgvsjnv6Unxdj4g')

command = {
        'toxic': "Обзови меня",
        'id': "Дай id",
        'photo': "Дай фото",
        'home': "👈 На главную",
        'base': "Запиши меня в базу",
    }

toxic_list = {
        'lox': "лох",
        'chert': "чмо",
        'chmo': "чёрт",
    }


@bot.message_handler(commands=['startbase'])
@bot.message_handler(func=lambda message: message.text == command['base'])
def start(message):
    name = bot.send_message(message.chat.id, "Как тебя записать?")
    bot.register_next_step_handler(name, nickname)


def nickname(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_name(
        name INTEGER    
    )""")
    connect.commit()
    user_name = [message.text]
    cursor.execute("INSERT INTO login_name VALUES(?);", user_name)
    connect.commit()
    bot.send_message(message.chat.id, 'Отлично, записал!')


@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: message.text == command['home'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🌚 Создай иллюзию')
    btn2 = types.KeyboardButton('🤙 Зачитай реп')
    btn3 = types.KeyboardButton('😂 Расскажи анекдот')
    btn4 = types.KeyboardButton('💊 Открой меню помощи')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник! Что мне сделать?", reply_markup=markup)


@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == '💊 Открой меню помощи')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(f'{command["toxic"]}')
    btn2 = types.KeyboardButton(f'{command["id"]}')
    btn3 = types.KeyboardButton(f'{command["photo"]}')
    btn4 = types.KeyboardButton(f'{command["home"]}')
    btn5 = types.KeyboardButton(f'{command["base"]}')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    command_list = '\n'.join(list(command.values()))
    n = '\n'
    bot.send_message(message.from_user.id, f"Что выбирите: {n}{command_list}", reply_markup=markup)


@bot.message_handler(commands=['toxic'])
@bot.message_handler(func=lambda message: message.text == command['toxic'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(f'{toxic_list["lox"]}')
    btn2 = types.KeyboardButton(f'{toxic_list["chert"]}')
    btn3 = types.KeyboardButton(f'{toxic_list["chmo"]}')
    btn4 = types.KeyboardButton(f'{command["home"]}')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, f"Как тебя обозвать?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def botText(message):
    if message.text == "🌚 Создай иллюзию":
        for i in range(10):
            bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}.Это я, твой единственный зритель."
                                              "На протяжении многих лет я создавал "
                                              "иллюзию того, что твои стримы смотрят много людей. Но это был я. "
                                              "Сейчас напишу это сообщение со всех аккаунтов.")
            sleep(0.5)

    elif message.text == '🤙 Зачитай реп':
        bot.send_message(message.from_user.id, "Коля, коля, тр*хни меня\n"
                                               "Коля, коля, тр*хни меня, Коля\n"
                                               "Ты моя вселенная, я не могу без тебя\n"
                                               "Коля, коля, тр*хни меня, Коля\n"
                                               "Ты моя вселенная, я не могу без тебя\n"
                                               "Я хочу, хочу тебя, Кооля\n")

    elif message.text == '😂 Расскажи анекдот':
        bot.send_message(message.from_user.id, "Сидит мужик в кафе. Выпивает. Мимо проходит монашка. Ловит взгляд мужика и говорит укоризненно:\n"
                                               "— Как ты можешь прожигать свою жизнь в этом пристанище блуда и разврата!\n"
                                               "— Да нет тут никакого разврата, сестра…\n"
                                               "… Лиза, — гневно отвечает монашка.\n"
                                               "— Да, Лиза. Все нормально. Я просто пью.\n"
                                               "— И это противно Господу, — говорит монашка.\n"
                                               "— А ты сама-то, сестра Лиза, пробовала хоть раз? — спрашивает мужик.\n"
                                               "— Нет! — возмущенно восклицает монашка.\n"
                                               "— Как же ты можешь утверждать? — спрашивает мужик. — Вот, я сейчас куплю тебе выпивку, и ты попробуешь…\n"
                                               "— Никогда! Чтобы люди увидели, как монашка пьет спиртное?\n"
                                               "— Я попрошу, чтобы тебе налили в кофейную чашку, — говорит мужик.\n"
                                               "Монашка неохотно соглашается. Мужик подходит к стойке и говорит:\n"
                                               "— Слышь, дай мне два стакана водки, но один налей в кофейную чашку.\n"
                                               "Бармен оборачивается:\n"
                                               "— Там случайно не сестра Лиза?..", parse_mode='html')

    elif message.text in toxic_list.values():
        bot.send_message(message.chat.id, f"{message.from_user.first_name} {message.text}", parse_mode='html')

    elif message.text == command['id']:
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')

    elif message.text == command['photo']:
        photo = open('photo/test.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True)