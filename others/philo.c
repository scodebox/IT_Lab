#define N 5
#define THINKING 0
#define EATING 1
#define HUNGRY 2
#define LEFT (i + N - 1) % N
#define RIGHT (i + 1) % N

semaphore mutex = 1;
semaphore s[N]; // all s[i] are initilized to zero.

int state[N]; // an array keep track everyones state.

void philosophers(int i)
{
    while (1)
    {
        take_fork(i);
        eat(i);
        put_fork(i);
    }
}

void take_fork(int i)
{
    down(mutex);
    state[i] = HUNGRY;
    test(i);
    up(mutex);
    down(s[i])
}

void put_fork(int i)
{
    down(mutex);
    state[i] = THINKING;
    test(LEFT);
    test(RIGHT);
    up(mutex);
}

void test(int i)
{
    if (state[i] == HUNGRY && state[LEFT] != EATING && state[RIGHT] != EATING)
    {
        state[i] = EATING;
        up(s[i]);
    }
}