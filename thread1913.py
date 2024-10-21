import threading
import time


def print_thread_id():
    time.sleep(1)
    if not hasattr(thread_local_storage, "thread_id"):
        thread_local_storage.thread_id = threading.get_ident()
    print(f"Thread ID: {thread_local_storage.thread_id}")


thread_local_storage = threading.local()
threads = [threading.Thread(target=print_thread_id) for _ in range(5)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
