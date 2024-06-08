import mysql.connector
import telebot
from telebot import types

# Подключаем токен бота
bot = telebot.TeleBot("6588903102:AAE0IvEgYjAE9VKUTuLsUIiiNjgSytXY-Rs")
message = ''

# РЕГИСТРАЦИЯ#
name = ''
surname = ''
age = 0
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Cколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text); # Проверка на правильный ввод
        except Exception:
            bot.send_message(message.from_user.id, "Не правильно введён возраст")
    keyboard = types.InlineKeyboardMarkup() # Клавиатура
    key_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
    keyboard.add(key_no)
    question = "Тебя зовут " + name + " " + surname + " и тебе " + str(age) + " лет?"
    bot.send_message(message.from_user.id, text=str(question), reply_markup=keyboard)

#Обработчик клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # подключение к бд
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="01evimes",
        database="SugarBt"
    )
    # получаем курсор
    cursor = db.cursor()

    if call.data == "yes": # регистрация успешна
        # Вставка данных в таблицу
        sql = "INSERT INTO user (name, surname, age) VALUES (%s, %s, %s)"
        values = (name, surname, age)
        cursor.execute(sql, values)

        bot.send_message(call.message.chat.id, f"Здравствуй, {name}!")
    elif call.data == "no": # регистрация не успешна
        bot.send_message(call.message.chat.id, "Попробуй ещё раз")
        bot.send_message(call.message.chat.id, "Как тебя зовут?")
        bot.register_next_step_handler(call.message, get_name)
    elif call.data == "sugarInfo":
        bot.send_message(call.message.chat.id, "Содержание сахара в крови должно соответствовать установленному диапазону уровня глюкозы в плазме. После сна натощак это значение должно быть в границах 59–99 мг на 100 мл, что равноценно 3,3–5,5 ммоль/литр. Значение после еды (спустя два часа) не должно превышать 141 мг на 100 мл, что, соответственно, до 7,8")
        bot.send_message(call.message.chat.id, "При анализах крови из пальца натощак допустимы следующие значения: дети до 14 лет — 2,3–3,9 ммоль на литр; подростки от 14 до 19 лет — 2,5–4,0 ммоль на литр; взрослые 20–49 лет — 3,0–5,5 ммоль на литр; пациенты старше 50 лет — 3,5–6,5 ммоль на литр. Если присутствуют небольшие отклонения на несколько десятых, это является допустимым.")
    elif call.data == "bakery":
        cursor.execute("select name, gram from bakery")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            bot.send_message(call.message.chat.id, text)
    elif call.data == "iceCream":
        cursor.execute("select name, gram from iceCream")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            bot.send_message(call.message.chat.id, text)
    elif call.data == "chocolate":
        cursor.execute("select name, gram from chocolate")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            bot.send_message(call.message.chat.id, text)
    elif call.data == "milk":
        cursor.execute("select name, gram from milk")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            bot.send_message(call.message.chat.id, text)
    elif call.data == "fruits":
        cursor.execute("select name, gram from fruits")
        for row in cursor:
            text = str(row[0]) + " - " + str(row[1]) + " г"
            bot.send_message(call.message.chat.id, text)

    # Сохраняем изменения и закрываем соединение
    db.commit()
    db.close()

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "/help - Список функций")
        bot.send_message(message.from_user.id, "/reg - Регистрация")
        bot.send_message(message.from_user.id, "/info - Общая информация")
    elif message.text == "/reg": #Регистрация
            bot.send_message(message.from_user.id, "Как тебя зовут?")
            bot.register_next_step_handler(message, get_name) # Следующий шаг: функция get_name
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
        question = "Выбери категорию"
        bot.send_message(message.from_user.id, text=str(question), reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Неизвестная функция, воспользуйся /help')

bot.polling(none_stop=True, interval=0)
