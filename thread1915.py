import threading
import time

students_info = {
    "Варлаам Бирюкова": {
        "Возраст": 25,
        "Специальность": None,
        "Город": None,
        "Страна": "Россия",
        "Университет": "ЗАО «Миронова-Прохоров»",
        "Курс": 3,
        "Группа": "CK008",
        "Электронная почта": "ostaplitkin@example.com",
        "Телефон": None,
        "Дата рождения": "2005-08-22",
        "Пол": "Женский",
        "Хобби": ["Физика", "Астрономия"],
        "Время обработки": 6,
    },
    "Никандр Мамонтов": {
        "Возраст": 20,
        "Специальность": "Компьютерные науки",
        "Город": "к. Октябрьский (Башк.)",
        "Страна": "Россия",
        "Университет": None,
        "Курс": 3,
        "Группа": "LE057",
        "Электронная почта": "jakub_2001@example.org",
        "Телефон": "+7 919 424 9512",
        "Дата рождения": "2002-01-13",
        "Пол": None,
        "Хобби": None,
        "Время обработки": 5,
    },
}


# Напишите ваш код
def thread_function(data):
    thread_data.data = data
    thread_data.sleep_time = data.get("Время обработки")
    for key, value in thread_data.data.items():
        if value:
            print(
                f"Имя потока - {threading.current_thread().name}, локальные данные потока - {key}: {value}"
            )
        time.sleep(thread_data.sleep_time / 10 if thread_data.sleep_time else 3)


thread_data = threading.local()


for key, value in students_info.items():
    thread = threading.Thread(target=thread_function, args=(value,))
    thread.name = key
    thread.start()
