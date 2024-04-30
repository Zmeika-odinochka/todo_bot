import telebot
import random

HELP = """
/help - напечатать справку о программе.
/add - добавить задачу в список (название задачи уточняем у пользователя).
/show - напечатать все добавленные задачи.
/exit - Выход из программы.
/random - добавить случайную задачу на сегодня.
"""


RANDOM_TASK = "Учиться программированию."
RANDOM_TASKS = [
    "Начать писать код", "Изучать теорию", "Проходить практикум",
    "Смотреть видосики", "Отдыхать", "Дзен питона"
]


TOKEN = "6948048739:AAH9GENG2Jl6T24LUpXzluUjvDraZ_Yn6ho"
bot = telebot.TeleBot(TOKEN)

print("Здравствуйте.")

print(HELP)

tasks = {}


def add_todo(date, task):
    # Проверка на существование даты в словаре.
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = (f"Задача '{task}', добавлена на дату - {date}")
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = (f"Задача '{task}', добавлена на дату - {date}")
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "- " + task + "\n"
    else:
        text = "Задач на эту дату нет."
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
