import mysql.connector
import telebot
from telebot import types

# Подключаем токен бота
bot = telebot.TeleBot("6588903102:AAE0IvEgYjAE9VKUTuLsUIiiNjgSytXY-Rs")
message = ''
prv_messages = []
keyboard_id = None

#Обработчик клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global prv_messages
    global keyboard_id
    if prv_messages:
        for msg_id in prv_messages:
            bot.delete_message(call.message.chat.id, msg_id)
        prv_messages = []
    # подключение к бд
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="01evimes",
        database="SugarBt"
    )
    # получаем курсор
    cursor = db.cursor()

    if call.data == "sugarInfo":
        sent = bot.send_message(call.message.chat.id, "Содержание сахара в крови должно соответствовать установленному диапазону уровня глюкозы в плазме. После сна натощак это значение должно быть в границах 59–99 мг на 100 мл, что равноценно 3,3–5,5 ммоль/литр. Значение после еды (спустя два часа) не должно превышать 141 мг на 100 мл, что, соответственно, до 7,8")
        prv_messages.append(sent.message_id)
        sent = bot.send_message(call.message.chat.id, "При анализах крови из пальца натощак допустимы следующие значения: дети до 14 лет — 2,3–3,9 ммоль на литр; подростки от 14 до 19 лет — 2,5–4,0 ммоль на литр; взрослые 20–49 лет — 3,0–5,5 ммоль на литр; пациенты старше 50 лет — 3,5–6,5 ммоль на литр. Если присутствуют небольшие отклонения на несколько десятых, это является допустимым.")
        prv_messages.append(sent.message_id)
    elif call.data == "bakery":
        cursor.execute("select name, gram from bakery")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            sent = bot.send_message(call.message.chat.id, text)
            prv_messages.append(sent.message_id)
    elif call.data == "iceCream":
        cursor.execute("select name, gram from iceCream")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            sent = bot.send_message(call.message.chat.id, text)
            prv_messages.append(sent.message_id)
    elif call.data == "chocolate":
        cursor.execute("select name, gram from chocolate")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            sent = bot.send_message(call.message.chat.id, text)
            prv_messages.append(sent.message_id)
    elif call.data == "milk":
        cursor.execute("select name, gram from milk")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            sent = bot.send_message(call.message.chat.id, text)
            prv_messages.append(sent.message_id)
    elif call.data == "fruits":
        cursor.execute("select name, gram from fruits")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            sent = bot.send_message(call.message.chat.id, text)
            prv_messages.append(sent.message_id)
    elif call.data == "exit":
        if keyboard_id:
            bot.delete_message(call.message.chat.id, keyboard_id)


    # Сохраняем изменения и закрываем соединение
    db.commit()
    db.close()

@bot.message_handler(content_types=['text'])
def start(message):
    global keyboard_id
    if message.text == "/help":
        bot.send_message(message.from_user.id, "/help - Список функций")
        bot.send_message(message.from_user.id, "/info - Общая информация")
    elif message.text == "/info":
        keyboard = types.InlineKeyboardMarkup()  # Клавиатура
        sugarInfo = types.InlineKeyboardButton(text="Норма сахара", callback_data="sugarInfo")
        keyboard.add(sugarInfo)
        bakery = types.InlineKeyboardButton(text="Хлебобулочные изделия", callback_data="bakery")
        keyboard.add(bakery)
        iceCream = types.InlineKeyboardButton(text="Мороженое", callback_data="iceCream")
        keyboard.add(iceCream)
        chocolate = types.InlineKeyboardButton(text="Шоколад", callback_data="chocolate")
        keyboard.add(chocolate)
        milk = types.InlineKeyboardButton(text="Молочные и кисломолочные продукты", callback_data="milk")
        keyboard.add(milk)
        fruits = types.InlineKeyboardButton(text="Фрукты и ягоды", callback_data="fruits")
        keyboard.add(fruits)
        exit = types.InlineKeyboardButton(text="Назад", callback_data="exit")
        keyboard.add(exit)
        question = "Выбери категорию"
        key = bot.send_message(message.from_user.id, text=str(question), reply_markup=keyboard)
        keyboard_id = key.message_id
    else:
        bot.send_message(message.from_user.id, 'Неизвестная функция, воспользуйся /help')

bot.polling(none_stop=True, interval=0)
