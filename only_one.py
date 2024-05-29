# Для разовых единичных задач

import threading
import time


def print_numbers(start, end, delay):
    for i in range(start, end + 1):
        time.sleep(delay)
        print(i)


def print_letters(seq, delay):
    for letter in seq:
        time.sleep(delay)
        print(letter)


if __name__ == "__main__":
    start_time = time.perf_counter()
    t1 = threading.Thread(target=print_numbers, args=(1, 5, 1))
    t2 = threading.Thread(target=print_letters, args=('abcde', 0.5))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Run time: {run_time:.2f} seconds")