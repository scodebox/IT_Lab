# Importing the libraries
import threading
import time

# Using semaphore to allowd one thread at a time.
semaphore = threading.Semaphore(1)

def show(n):
    while True:
        # Sensor will get activated 1 second interval.
        time.sleep(1)
        # Down operation on semaphore.
        semaphore.acquire()
        print('Value of n : ', n)
        # Up operation on semaphore.
        semaphore.release()

# Creating threads.
t1 = threading.Thread(target=show, args=(0,))
t2 = threading.Thread(target=show, args=(1,))
t3 = threading.Thread(target=show, args=(2,))
t4 = threading.Thread(target=show, args=(3,))
t5 = threading.Thread(target=show, args=(4,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
