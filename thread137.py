# Импортируйте все необходимое
import threading

# Напишите необходимые функции для вычисления суммы и произведения
total_sum = 0
total_mul = 1

def _sum(start,end):
    return sum([i for i in range(start,end+1)])

def _mul(start,end):
    t=1
    for i in range(start,end+1):
        t*=i
    return t

# Создайте и запустите потоки с целевыми функциями
def thread_sum(*args):
    global total_sum
    total_sum=_sum(args[0],args[1])

def thread_mul(*args):
    global total_mul
    total_mul=_mul(args[0],args[1])

threadS = threading.Thread(target=thread_sum,args=(1,1000))
threadM = threading.Thread(target=thread_mul,args=(1,10))
threadS.start()
threadM.start()

# Выведите результаты работы потоков согласно условиям задачи
print(f"Сумма чисел от 1 до 1000: {total_sum}")
print(f"Произведение чисел от 1 до 10: {total_mul}")
