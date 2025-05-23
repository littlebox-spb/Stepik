class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        # Напишите тут ваш код
        self.queue.append(item)

    def dequeue(self):
        # Напишите тут ваш код
        if self.is_empty():
            return "queue is empty"
        return self.queue.pop(0)

    def peek(self):
        # Напишите тут ваш код
        if self.is_empty():
            return "queue is empty"
        return self.queue[0]


# Демонстрация работы
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())  # Front item: 1
print(q.dequeue())  # Dequeued: 1
print(q.dequeue())  # Dequeued: 2
print(q.peek())  # Front item: 3
print(q.dequeue())  # Dequeued: 3
print(q.dequeue())  # Queue is empty
