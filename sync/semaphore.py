import threading

semaphore = threading.Semaphore(2)

def fact(n):
	semaphore.acquire()
	print ('fun : ',n,': semaphore value : ',semaphore._value)
	print ('fun : ',n,': semaphore name : ',threading.current_thread().name)
	f=1
	name=n
	while (n>0):
		f=f*n
		print ('fact: ',name)
		n-=1

	print('fun : ',name,'complete')
	semaphore.release()


t1 = threading.Thread(target=fact, args=(10,))
t2 = threading.Thread(target=fact, args=(8,))
t3 = threading.Thread(target=fact, args=(7,))
t1.start()
t2.start()
t3.start()
print ('main Thread: ',threading.main_thread())