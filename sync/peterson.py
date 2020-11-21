import threading
import time


turn=0
flag = [False,False]


def p(n):
	while True:
		flag[n] = True
		turn=1-n
		while (turn==(1-n) and (flag[1-n]==True)):
			print ('Process ',n,' waiting.')
		print (print ('Process ',n,' inside critical section.'))
		flag[n]=False
		time.sleep(1)


t1 = threading.Thread(target=p, args=(0,))
t1.start()
t2 = threading.Thread(target=p, args=(1,))
t2.start()