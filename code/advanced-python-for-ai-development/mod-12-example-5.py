from threading import Semaphore

sem = Semaphore(10)  # Max 10 concurrent

def access_limited_resource():
    with sem:
        # Only 10 threads execute here simultaneously
        gpu_operation()