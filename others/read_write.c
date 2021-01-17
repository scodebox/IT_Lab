int rc = 0;
semaphore mutex = 1;
semaphore db = 1;

void reader(void)
{
    while (1)
    {
        down(mutex);
        rc++;
        if (rc == 1)
            down(db);
        up(mutex);
        /*
            READ
        */
        down(mutex);
        rc--;
        if (rc == 0)
            up(db);
        up(mutex);
    }
}

void writer(void)
{
    while (1)
    {
        down(db);
        /*
           WRITE
        */
        up(db);
    }
}