from threading import Thread


def task1():
    for n in range(1,6):
        print(n)
    
def task2():
    for b in 'abcde':
        print(b)
    
def main():    
    thread1 = Thread(target=task1)
    thread1.start()
    thread1.join()
    thread2 = Thread(target=task2)
    thread2.start()
    thread2.join()
    print("Готово!")
    
if __name__ == "__main__":
    main()      



