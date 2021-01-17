import threading
import time

# Using semaphore to allowd one thread at a time.
semaphore = threading.Semaphore(1)

# Function will be running concurrently
def fact(num):
    # Down operation
    semaphore.acquire()
    for i in range(num):
        time.sleep(1)
        # Showing thread number and value of i.
        print("value %d :: %s" % (i, threading.current_thread()._name))
    # Up operation.
    semaphore.release()


# Creating threads.
t1 = threading.Thread(target=fact, args=(5,))
t2 = threading.Thread(target=fact, args=(7,))
# Starting threads.
t1.start()
t2.start()
