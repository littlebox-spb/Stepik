import threading

# Глобальные переменные для массивов
array_descending = [733, 725, 389, 606, 544, 526, 496, 448, 345, 239]
array_ascending = [124, 168, 350, 501, 389, 419, 428, 662, 760, 829]
symbols_array = ['g', 'e', 'k', 'a', 'w', 'z', 'o', 'b', 'm', 'l', 'h', 'n', 'd', 's', 'q']


# Функции для сортировки массивов
def sort_numbers_descending():
    #Допишите функцию сортировки массива по убыванию
    array_descending.sort(reverse=True)

def sort_numbers_ascending():
    #Допишите функцию сортировки массива по возрастанию
    array_ascending.sort()

def sort_symbols():
    #Допишите функцию сортировки массива символов в лексикографическом порядке
    symbols_array.sort()

# Создайте и запустите потоки для сортировки
thread1 = threading.Thread(target=sort_numbers_descending)
thread2 = threading.Thread(target=sort_numbers_ascending)
thread3 = threading.Thread(target=sort_symbols)
thread1.start()
thread2.start()
thread3.start()

# Выведете отсортированные массивы
print(f"Массив чисел (по убыванию): {array_descending}")
print(f"Массив чисел (по возрастанию): {array_ascending}")
print(f"Массив символов (лексикографический порядок): {symbols_array}")