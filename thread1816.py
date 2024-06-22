import random
import time
from threading import Thread, current_thread

# Словарь имен потоков и их миссий
# Полный словарь вшит в задачу
missions = {
    "Thread-Scan": "Сканирование данных",
    "Thread-Hack": "Взлом системы",
    # ...,
}


# Описание задачи для потоков
def mission(mission_name):
    print(f"[{mission_name}] Миссия началась.")
    time.sleep(random.randint(1, 3))
    print(f"[{mission_name}] Миссия успешно выполнена!")


def main():
    plst = []
    for m, mv in missions.items():
        p = Thread(target=mission, args=(mv,), name=m)
        print(f"[{p.name} ({mv})] Статус миссии до запуска: {p.is_alive()}")
        plst.append(p)
        p.start()
        print(f"[{p.name} ({mv})] Миссия активна: {p.is_alive()}")
    while len(plst) > 0:
        for p in plst:
            if not p.is_alive():
                plst.remove(p)
                print(
                    f"[{p.name} ({missions[p.name]})] Статус миссии после завершения: {not p.is_alive()}"
                )


main()
