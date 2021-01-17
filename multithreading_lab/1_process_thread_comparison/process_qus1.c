#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<sys/wait.h>

/*
In this case, the value of variable var will be 5 for both.
Because here unlike threads total memory code variable all are replicated in the child process.
So the child process having their copy of variable var. 
At the end of the program, both the child and parent process will be printing the value of var 5. 
*/


// Global variable.
int var=0;

int main(){
    // Creating child process.
    int pid = fork();

    // If fork() returns -1 then child process has not created.
    // If fork() returns 0 then child process has creaed.
    if(-1==pid) exit(1);

    // Check the process id.
    if(0==pid){
        // Child process.
        // Child process will be executing this if part of the code.
        for(int i=0;i<5;i++) ++var;
    }else{
        // Parent process.
        // Parent process will be executing else part of the code.
        for(int i=0;i<5;i++) ++var;
    }

    // The parent process will be waiting for the child process.
    if(0!=pid) wait(NULL);

    // Printing the value of variable var.
    // This line of code will be executed by both process.
    printf("Value of var : %d\n",var);

    return 0;
}