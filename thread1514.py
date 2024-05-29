#Импортируйте все необходимое
import threading
import time


#Создайте целевую функцию
def f1():
    for i in range(1, 6):
        time.sleep(.5)
        print(i)

def f2():
    for i in range(6, 11):
        time.sleep(1)
        print(i)

#Создайте и запустите потоки согласно условию задачи
thread1 = threading.Thread(target=f1)
thread2 = threading.Thread(target=f2)
thread1.start()
thread2.start()
#Дождитесь завершения потоков
thread1.join()
thread2.join()
#Не забудьте вывести информацию о завершении работы потоков
print("Оба потока завершили свою работу.")