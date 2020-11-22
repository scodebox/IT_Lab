import threading

# Initialization of semaphore for two process.
semaphore = threading.Semaphore(2)


def fact(n):
    # acquiring the semaphore.
    semaphore.acquire()
    # Showing the value of semaphore.
    print('fun : ', n, ': semaphore value : ', semaphore._value)
    # Showing the name of the thread.
    print('fun : ', n, ': semaphore name : ', threading.current_thread().name)

    f = 1
    name = n
    while (n > 0):
        f = f*n
        print('fact: ', name)
        n -= 1

    print('fun : ', name, 'complete')
    # Releasing the semaphore.
    semaphore.release()


# Creating three thread to check semaphore.
t1 = threading.Thread(target=fact, args=(10,))
t2 = threading.Thread(target=fact, args=(8,))
t3 = threading.Thread(target=fact, args=(7,))
# Starting all the thread.
t1.start()
t2.start()
t3.start()
# Showing main thread details.
print('main Thread: ', threading.main_thread())
