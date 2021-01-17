#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

/*
This is a multithreading problem in a real-time environment. 
In the case of serial execution, the counter value will be 2000000 
after completion of the program. But in the case of multithreading environment, 
we may get the value that is less than 2000000. The reason the race condition. 
Each thread is reading the value of the counter variable adding 1 to it and write it back. 
Both are working in parallel so sometimes 
both thread reading the same value and writing the by incrementing by one. 
So instead of 2 increment counter variable getting one increment overall.
*/

// The counter variable shared between threads.
int counter = 0;

// The function will increase counter by 1 for 1000000 times.
// The same function will be running in two different threads.
void *fun()
{
    for (int i = 0; i < 1000000; i++)
        ++counter;
}

int main()
{
    // Creating two thread for counter.
    pthread_t t1, t2;
    if (0 != pthread_create(&t1, NULL, &fun, NULL))
        exit(1);
    if (0 != pthread_create(&t2, NULL, &fun, NULL))
        exit(1);

    // Waiting for completion.
    if (0 != pthread_join(t1, NULL))
        exit(1);
    if (0 != pthread_join(t2, NULL))
        exit(1);

    // Printing the final result after execution two threads.
    printf("Total Count : %d\n", counter);

    return 0;
}