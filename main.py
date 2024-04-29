import random

HELP = """
help - напечатать справку о программке.
add - добавить задачу в список (название задачи уточняем у пользователя).
show - напечатать все добавленные задачи.
exit - Выход из программы.
random - добавить случайную задачу на сегодня.
"""

RANDOM_TASK = "Учиться программированию."
RANDOM_TASKS = [
    "Начать писать код", "Изучать теорию", "Проходить практикум",
    "Смотреть видосики", "Отдыхать", "Дзен питона"
]

print(HELP)

tasks = {

}


def add_todo(date, task):
    # Проверка на существование даты в словаре.
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
    print(f"Задача, '{task}', добавлена на дату, {date}")


print("Здравствуйте.")

while True:
    command = input("Введите команду: ")

    if command == "help":
        print(HELP)
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)

    elif command == "show":
        date = input("Введите дату для отображение задачи: ")
        if date in tasks:
            for task in tasks[date]:
                print(f"- {task}")
        else:
            print("В ваших задачах такой даты нет.")

    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)

    elif command == "exit":
        print("До свидания!")
        break
    else:
        print("Неизвестная команда.")
