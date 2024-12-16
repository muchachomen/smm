import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton




BOT_TOKEN = "7648526822:AAENqSJ0uulVldU6JDkehbmSBc7rXRxA_mw"

bot = telebot.TeleBot(BOT_TOKEN)


ADMINS = [1970397502]



def client_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Создать новый заказ", "Мои заказы")
    markup.add("Мой баланс", "Заработать")
    markup.add("Помощь", "FAQ", "Чеки")
    return markup



def admin_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Создать новый заказ", "Мои заказы", "Мой баланс")
    markup.add("Управление категориями", "Управление товарами", "Рассылка")
    markup.add("Заработать", "Помощь", "FAQ", "Чеки")
    return markup



@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.from_user.id
    if user_id in ADMINS:
        bot.send_message(
            message.chat.id,
            "Добро пожаловать, администратор! Выберите нужный пункт меню:",
            reply_markup=admin_main_menu()
        )
    else:
        bot.send_message(
            message.chat.id,
            "Добро пожаловать! Выберите нужный пункт меню:",
            reply_markup=client_main_menu()
        )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id


    if user_id not in ADMINS:
        if message.text == "Создать новый заказ":
            bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=create_order_menu())
        elif message.text == "Мои заказы":
            bot.send_message(message.chat.id, "Ваши заказы (здесь будет пагинация):")
        elif message.text == "Мой баланс":
            bot.send_message(message.chat.id, "Ваш текущий баланс: 0 рублей.")
        elif message.text == "Заработать":
            bot.send_message(message.chat.id, "Реферальная программа: поделитесь ссылкой и зарабатывайте!")
        elif message.text == "Помощь":
            bot.send_message(message.chat.id, "Как пользоваться ботом: [инструкция]")
        elif message.text == "FAQ":
            bot.send_message(message.chat.id, "Часто задаваемые вопросы: [список вопросов]")
        elif message.text == "Чеки":
            bot.send_message(message.chat.id, "Ваши чеки: (здесь будет информация)")
        else:
            bot.send_message(message.chat.id, "Я не понимаю эту команду. Попробуйте снова.")


    else:
        if message.text == "Управление категориями":
            bot.send_message(message.chat.id, "Управление категориями: добавить/удалить/редактировать.")
        elif message.text == "Управление товарами":
            bot.send_message(message.chat.id, "Управление товарами: добавить/удалить/редактировать.")
        elif message.text == "Рассылка":
            bot.send_message(message.chat.id, "Введите сообщение для рассылки:")
        elif message.text in ["Создать новый заказ", "Мои заказы", "Мой баланс"]:
            handle_text(message)  # Администратор также может пользоваться клиентскими функциями
        else:
            bot.send_message(message.chat.id, "Я не понимаю эту команду. Попробуйте снова.")



def create_order_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Категория 1", callback_data="category_1"))
    markup.add(InlineKeyboardButton("Категория 2", callback_data="category_2"))
    markup.add(InlineKeyboardButton("Назад", callback_data="back_to_main"))
    return markup



bot.polling(none_stop=True)
