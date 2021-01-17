#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

/*
In this example, two thread will take a lock on two mutex variable in a different order 
to illustrate the deadlock occurrence in multi-threading environment. 
For example, 
assume the thread 1 executing function 1 and thread 2 executing function 2. 
If thread one started first then thread 1 will take lock on mutex 1. for the sleep()
thread 1 will be waiting for a while. By that moment thread 2 will take lock on mutex 2.

The next instruction for thread 1 is to take lock on mutex 2 which is not possible 
because thread 2 already taken that. 
The next instruction of thread 2 is to take lock on mutex 1 which is not possible 
because thread 1 already taken that. 

So the program will be stuck there for an indefinite amount of time because it is in deadlock.  
*/

// Two mutex for locking.
pthread_mutex_t mutex1;
pthread_mutex_t mutex2;

// The function 1 will first take a lock on mutex1 and then mutex2.
void *fun1()
{
    // Lock on mutex 1.
    pthread_mutex_lock(&mutex1);
    printf("fun 1 : Lock mutex 1\n");
    // wait for a second so other thread can get lock on if this first thread started executing.
    sleep(1);
    // lock on mutex 2.
    pthread_mutex_lock(&mutex2);
    printf("fun 1 : Lock mutex 2\n");

    printf("fun 1 : Got both \n");

    // Unlock mutex 1.
    pthread_mutex_unlock(&mutex1);
    printf("fun 1 : Unlock mutex 2\n");
    // Unlock mutex 2.
    pthread_mutex_unlock(&mutex2);
    printf("fun 1 : Unlock mutex 2\n");
}

// Thi function 2 will first take a lock on mutex2 then mutex1.
// reverse order locking to make chance of deadlock high.
void *fun2()
{
    // Lock on mutex 2.
    pthread_mutex_lock(&mutex2);
    printf("fun 2 : Lock mutex 2\n");
    // wait for a second so other thread can get lock on if this first thread started executing.
    sleep(1);
    // Lock on mutex 1.
    pthread_mutex_lock(&mutex1);
    printf("fun 2 : Lock mutex 1\n");

    printf("fun 2 : Got both \n");

    // Unlock mutex 1.
    pthread_mutex_unlock(&mutex1);
    printf("fun 1 : Unlock mutex 2\n");
    // Unlock mutex 2.
    pthread_mutex_unlock(&mutex2);
    printf("fun 1 : Unlock mutex 2\n");
}

int main()
{
    // Initializing mutex1 and mutex2.
    pthread_mutex_init(&mutex1, NULL);
    pthread_mutex_init(&mutex2, NULL);

    // Creating two thread.
    // One thread will be executing function 1.
    // another thread will be executing function 2.
    pthread_t t1, t2;
    if (0 != pthread_create(&t1, NULL, &fun1, NULL))
        exit(1);
    if (0 != pthread_create(&t2, NULL, &fun2, NULL))
        exit(1);

    // Main thread will wait for the completion of two thread.
    if (0 != pthread_join(t1, NULL))
        exit(1);
    if (0 != pthread_join(t2, NULL))
        exit(1);

    // Destroty mutex after completion.
    pthread_mutex_destroy(&mutex1);
    pthread_mutex_destroy(&mutex2);
    return 0;
}