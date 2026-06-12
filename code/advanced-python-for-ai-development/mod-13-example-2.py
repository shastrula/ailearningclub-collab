import threading

thread_local = threading.local()

def worker():
    thread_local.model = load_model()
    predictions = thread_local.model.predict(X)

threads = [Thread(target=worker) for _ in range(4)]
for t in threads:
    t.start()