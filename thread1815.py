import time
from threading import Thread, current_thread


# Функция задачи для потоков
def task():
    time.sleep(2)
    print(f"Задача выполнена для {current_thread().name}")


# Список кодовых имен
# Полный список вшит в задачу
code_names = [
    "Alpha",
    "India",
    "Hotel",
    "Delta",
    "Bravo",
    "Juliet",
    "Golf",
    "Echo",
    "Charlie",
    "Foxtrot",
    "Mike",
    "November",
    "Oscar",
    "Lima",
    "Kilo",
]


def main():
    for n in range(15):
        p = Thread(target=task)
        p.start()
        print(f"Исходное имя потока: {p.name}")
        p.name = code_names[n]
        print(f"Новое имя потока: {p.name}")


main()
