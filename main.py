HELP = """
help - напечатать справку о программке.
add - добавить задачу в список (название задачи уточняем у пользователя).
show - напечатать все добавленные задачи.
exit - Выход из программы.
"""
print(HELP)

tasks = {

}

print("Здравствуйте.")

while True:
    command = input("Введите команду: ")

    if command == "help":
        print(HELP)
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        # Проверка на существование даты в словаре.
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date].append(task)
        print(f"Задача, '{task}', добавлена на дату, {date}")
    elif command == "show":
        date = input("Введите дату для отображение задачи: ")
        if date in tasks:
            for task in tasks[date]:
                print(f"- {task}")
        else:
            print("В ваших задачах такой даты нет.")
    elif command == "exit":
        print("До свидания!")
        break
    else:
        print("Неизвестная команда.")
