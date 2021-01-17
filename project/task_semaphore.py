# Importing the libraries
import threading
import random
import time

# Using semaphore to allowd one thread at a time.
semaphore = threading.Semaphore(1)
# List for sensor data.
sensor_data = [0]*5


# Function for sensing object.
# Argument n is sensor number.
# After sensing if the object found then n th index of list will be 1 else 0.
def sense(n):
    while True:
        # Sensor will get activated 1 second interval.
        time.sleep(1)
        # Down operation on semaphore.
        semaphore.acquire()
        # Showing the details of semaphore and the cueent thread.
        print("locked by : "+threading.current_thread().name)
        print("Semaphore value : ", semaphore._value)
        # For testing ramdomly take value from 1 or 0.
        sensor_data[n] = random.choice([0, 1])
        print("N : ", n)
        print("Unlocked by : "+threading.current_thread().name)
        # Up operation on semaphore.
        semaphore.release()
        print("Semaphore value : ", semaphore._value)
        print()


# Function to print the file with 1 second interval.
# To check that thread synchronization implemented correctly.
def show_data():
    while True:
        # 1 second interval.
        time.sleep(1)
        # Down operation on semaphore.
        semaphore.acquire()
        # Showing the details of semaphore and the cueent thread.
        print("locked by : "+threading.current_thread().name)
        print("Semaphore value : ", semaphore._value)
        # Showing the data.
        print("\tSENSOR DATA :: ", sensor_data)
        # Up operation on semaphore.
        print("Unlocked by : "+threading.current_thread().name)
        semaphore.release()
        print("Semaphore value : ", semaphore._value)
        print()


# Creating threads.
t1 = threading.Thread(target=sense, args=(0,))
t2 = threading.Thread(target=sense, args=(1,))
t3 = threading.Thread(target=sense, args=(2,))
t4 = threading.Thread(target=sense, args=(3,))
t5 = threading.Thread(target=sense, args=(4,))
data = threading.Thread(target=show_data)
# Starting five threads and one thread for showing the list.
data.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
