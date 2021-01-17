#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

/*
In multithreading system, the memory space of the process is shared among the threads. 
So the variable var is shared memory for two threads. 
After the execution of two threads, the value of variable var will be 10. 
Because each thread will increase the value of the variable five times.
*/

// Global variable.
int var = 0;

// Function will be running in different threads.
void *fun()
{
    // increase the value of the variable five times
    for (int i = 0; i < 5; i++)
        ++var;
    // show the result about execution of the thread.
    printf("Value of var : %d\n", var);
}

int main()
{
    // Creating threads.
    pthread_t t1, t2;
    // If pthread_create return 0 then threads are not created.
    if (0 != pthread_create(&t1, NULL, &fun, NULL))
        exit(1);
    if (0 != pthread_create(&t2, NULL, &fun, NULL))
        exit(1);

    // The main thread will wait here for the completion of two threads.
    // If pthread_join returns 0 then failed to join those thread.
    if (0 != pthread_join(t1, NULL))
        exit(1);
    if (0 != pthread_join(t2, NULL))
        exit(1);

    return 0;
}