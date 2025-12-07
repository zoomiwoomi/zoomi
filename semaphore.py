import threading
import time

semaphore = threading.Semaphore(2)

def worker(i):
    print(f"Worker {i} waiting...")
    with semaphore:
        print(f"Worker {i} entered critical section.")
        time.sleep(1)
        print(f"Worker {i} leaving...")

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Semaphore example completed.")
