import telebot
from telebot import types
from time import sleep

bot = telebot.TeleBot('5818550349:AAF4vY8XTiogETFKsVoMZgvsjnv6Unxdj4g')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🌚 Создай иллюзию')
    btn2 = types.KeyboardButton('🤙 Зачитай реп')
    btn3 = types.KeyboardButton('😂 Расскажи анекдот')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник! Что мне сделать?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def botText(message):

    if message.text == "🌚 Создай иллюзию":
        for i in range(10):
            bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}. Это я, твой единственный зритель. "
                                              "На протяжении многих лет я создавал "
                                              "иллюзию того, что твои стримы смотрят много людей. Но это был я. "
                                              "Сейчас напишу это сообщение со всех аккаунтов.")
            sleep(0.5)

    elif message.text == '🤙 Зачитай реп':
        bot.send_message(message.from_user.id, "Коля, коля, тр*хни меня")
        bot.send_message(message.from_user.id, "Коля, коля, тр*хни меня, Коля")
        bot.send_message(message.from_user.id, "Ты моя вселенная, я не могу без тебя")
        bot.send_message(message.from_user.id, "Коля, коля, тр*хни меня, Коля")
        bot.send_message(message.from_user.id, "Ты моя вселенная, я не могу без тебя")
        bot.send_message(message.from_user.id, "Я хочу, хочу тебя, Кооля")

    elif message.text == '😂 Расскажи анекдот':
        bot.send_message(message.from_user.id, "Сидит мужик в кафе. Выпивает. Мимо проходит монашка. Ловит взгляд мужика и говорит укоризненно:")
        bot.send_message(message.from_user.id, "— Как ты можешь прожигать свою жизнь в этом пристанище блуда и разврата!")
        bot.send_message(message.from_user.id, "— Да нет тут никакого разврата, сестра…")
        bot.send_message(message.from_user.id, "… Лиза, — гневно отвечает монашка.")
        bot.send_message(message.from_user.id, "— Да, Лиза. Все нормально. Я просто пью.")
        bot.send_message(message.from_user.id, "— И это противно Господу, — говорит монашка.")
        bot.send_message(message.from_user.id, "— А ты сама-то, сестра Лиза, пробовала хоть раз? — спрашивает мужик.")
        bot.send_message(message.from_user.id, "— Нет! — возмущенно восклицает монашка.")
        bot.send_message(message.from_user.id, "— Как же ты можешь утверждать? — спрашивает мужик. — Вот, я сейчас куплю тебе выпивку, и ты попробуешь…")
        bot.send_message(message.from_user.id, "— Никогда! Чтобы люди увидели, как монашка пьет спиртное?")
        bot.send_message(message.from_user.id, "— Я попрошу, чтобы тебе налили в кофейную чашку, — говорит мужик.")
        bot.send_message(message.from_user.id, "Монашка неохотно соглашается. Мужик подходит к стойке и говорит:")
        bot.send_message(message.from_user.id, "— Слышь, дай мне два стакана водки, но один налей в кофейную чашку.")
        bot.send_message(message.from_user.id, "Бармен оборачивается:")
        bot.send_message(message.from_user.id, "— Там случайно не сестра Лиза?..")


bot.polling(none_stop=True)