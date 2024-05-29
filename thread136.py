import threading

# Массив для суммирования
array = [123456, 7890123, 987654, 114455, 995423, 1000000]

# Глобальная переменная для хранения результата
total_sum = 0

# Функция для вычисления суммы элементов массива
def sum_array():
    return sum(array)

# Функция для потока, обрабатывающего массив
def thread_task():
    global total_sum
    total_sum=sum_array()
    
# Создайте поток
thread = threading.Thread(target=thread_task)

# Запустите поток
thread.start()

# Дождитесь завершения потока
thread.join()

# Напечатайте сумму массива array
print(total_sum)