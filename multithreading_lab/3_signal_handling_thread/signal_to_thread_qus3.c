#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

/*
Here producer will produce 20 items in each second. 
But the consumer will consume 100 items from the container. 
So the consumer has to wait for 100 items without holding the lock on the container. 
The producer will send a signal to the consumer each time after producing 20 new items.
*/

// Shared variable between producer and consumer.
// Producer will pul produced item into the container.
// Consumer will consume those items from the container.
int container = 0;

// Mutex for lock on container while producing or consuming from container.
pthread_mutex_t mutex;
// Control will be used for signaling threads.
pthread_cond_t control;

// The produder thread will produce by 20 and wait for a second.
void *producer()
{
    for (int i = 0; i < 10; i++)
    {
        // Taking lock.
        pthread_mutex_lock(&mutex);
        // Adding 20.
        container += 20;
        printf("Produced : %d\n", container);
        // Releasing lock.
        pthread_mutex_unlock(&mutex);

        // Signal to thread waiting for producer to produce.
        pthread_cond_signal(&control);
        // Wait for a second.
        sleep(1);
    }
}

// The consumer will consume 100 from the container.
void *consumer()
{
    // Taking lock.
    pthread_mutex_lock(&mutex);
    // Checking if value of container.
    while (container < 100)
    {
        printf("Consumer waiting...\n");
        // If we leave this like that! producer can not add anything to container
        // because mutex lock is taken by the consumer.
        // but consumer can not the 100 from the container because container.
        // So consumer must release the lock and come and check after a while.
        pthread_cond_wait(&control, &mutex);
        // equivalent to:
        // pthread_mutex_unlock(&mutex); -> unlock mutex.
        // wait for a singal from generator.
        // pthread_mutex_lock(&mutex); -> lock mutex
    }
    container -= 100;
    printf("Ramining : %d\n", container);
    // Releasing the lock.
    pthread_mutex_unlock(&mutex);
}

int main()
{
    // Initializing mutex and control.
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&control, NULL);

    // Starting producer and consumer in two threads.
    pthread_t producer_th, consumer_th;
    pthread_create(&producer_th, NULL, &producer, NULL);
    pthread_create(&consumer_th, NULL, &consumer, NULL);

    // Waiting for completion.
    pthread_join(producer_th, NULL);
    pthread_join(consumer_th, NULL);

    // Destroty mutex after completion.
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&control);

    return 0;
}