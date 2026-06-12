from queue import Queue
from threading import Thread

def producer(queue):
    for i in range(100):
        queue.put(f'batch_{i}')

def consumer(queue):
    while True:
        batch = queue.get()
        if batch is None:
            break
        process(batch)
        queue.task_done()

q = Queue()
Thread(target=producer, args=(q,)).start()
Thread(target=consumer, args=(q,)).start()