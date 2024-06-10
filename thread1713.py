# Импортируйте все необходимое
import time
from threading import Thread, current_thread


# Напишите целевую функцию
def worker2():
    print(f"Поток {current_thread().name} запустился.")
    time.sleep(2)


def worker3():
    print(f"Поток {current_thread().name} запустился.")
    time.sleep(3)


# Напишите и вызовите функцию main()
def main():
    t1 = Thread(target=worker2, name="A")
    t2 = Thread(target=worker3, name="B")
    t1.start()
    t2.start()
    t1.join(timeout=2.1)
    if t2.is_alive():
        print(f"Поток {t2.name} не завершился за установленное время.")


if __name__ == "__main__":
    main()
