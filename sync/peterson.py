import threading
import time

# Initialization
turn = 0
flag = [False, False]

def p(n):
    while True:
        # Setting flag true and giving turn to other process.
        flag[n] = True
        turn = 1-n

        # Checking other process trun and flag.
        while (turn == (1-n) and (flag[1-n] == True)):
            print('Process ', n, ' waiting.')

        print('Process ', n, ' inside Critical Section.')
        # Setting flag false.
        flag[n] = False
        time.sleep(1)

# Creating thread for process 1.
t1 = threading.Thread(target=p, args=(0,))
t1.start()
# Creating thread for process 2.
t2 = threading.Thread(target=p, args=(1,))
t2.start()
