#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#define MAX_BUF_SIZE 1024

// Buffer for storing read and write data
char buffer[1024];

// Function for printing the error.
int error_handle(const char *err)
{
    // Print a message describing the meaning of the value of errno.
    perror(err);
    exit(1);
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("PORT missing! \n");
        exit(1);
    }

    // # SOCKET
    // Create a new socket of type TYPE in domain DOMAIN, using
    // protocol PROTOCOL. If PROTOCOL is zero, one is chosen automatically.
    // Returns a file descriptor for the new socket, or -1 for errors.
    int socket_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_fd < 0)
        error_handle("While opening socket!\n");

    struct sockaddr_in server_addr;
    struct sockaddr_in client_addr;
    socklen_t client_len = sizeof(client_addr);

    // Set N bytes of S to 0.
    bzero((void *)&server_addr, sizeof(server_addr));
    // Port number.
    int port_no = atoi(argv[1]);
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(port_no);

    // # BIND
    // Give the socket FD the local address ADDR (which is LEN bytes long).
    if (bind(socket_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
        error_handle("Binding failed!\n");

    // # LISTEN
    // Prepare to accept connections on socket FD.
    // N(3) connection requests will be queued before further requests are refused.
    // Returns 0 on success, -1 for errors.
    listen(socket_fd, 3);
    printf("Listening..\n");

    // # ACCEPT
    // Await a connection on socket FD.
    // When a connection arrives, open a new socket to communicate with it,
    // set *ADDR (which is *ADDR_LEN bytes long) to the address of the connecting
    // peer and *ADDR_LEN to the address's actual length, and return the
    // new socket's descriptor, or -1 for errors.
    int client_fd = accept(socket_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0)
        error_handle("Error while accepting connection!\n");

    while (1)
    {
        // Clearing the buffer.
        bzero(buffer, MAX_BUF_SIZE);

        // # RECEIVE
        // Read NBYTES into BUF from FD. Return the
        // number read, -1 for errors or 0 for EOF.
        if (read(client_fd, buffer, MAX_BUF_SIZE) < 0)
            error_handle("Error while reading client!\n");
        // Show the msg.
        printf("Client: %s", buffer);

        // Clearing the buffer.
        bzero(buffer, MAX_BUF_SIZE);

        // Taking msg input.
        printf("Message : ");
        fgets(buffer, MAX_BUF_SIZE, stdin);

        // # SEND
        // Send to the client.
        if (write(client_fd, buffer, strlen(buffer)) < 0)
            error_handle("Error while writing client!\n");
    }

    // # CLOSE
    // Closing the connection.
    close(client_fd);
    close(socket_fd);

    return 0;
}