// filename server-IP port_no
// argv[0] -> filename
// argv[1] -> server IP
// argv[2] -> PORT NO

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
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
    // If IP | PORT is not provided!
    if (argc < 3)
    {
        printf("argv missing! \n");
        exit(1);
    }

    // # SOCKET
    // Create a new socket of type TYPE in domain DOMAIN, using
    // protocol PROTOCOL. If PROTOCOL is zero, one is chosen automatically.
    // Returns a file descriptor for the new socket, or -1 for errors.
    int socket_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_fd < 0)
        error_handle("While opening socket!\n");

    // # BIND
    int port_no = atoi(argv[2]);
    struct hostent *server = gethostbyname(argv[1]);
    if (NULL == server)
        error_handle("Error : gethostbyname\n");

    struct sockaddr_in server_addr;
    // Set N bytes of S to 0.
    bzero((void *)&server_addr, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    // Copy N bytes of SRC to DEST (like memmove, but args reversed)
    bcopy((void *)server->h_addr, (void *)&server_addr.sin_addr.s_addr, server->h_length);
    server_addr.sin_port = htons(port_no);

    // # CONNECT
    // Open a connection on socket FD to peer at ADDR (which LEN bytes long).
    // For connectionless socket types, just set the default address to send to
    // and the only address from which to accept transmissions.
    // Return 0 on success, -1 for errors.
    if (connect(socket_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
        error_handle("Connection failed!\n");

    while (1)
    {
        // Clear the buffer.
        bzero(buffer, MAX_BUF_SIZE);

        // # SEND
        // Take the msg from user.
        printf("Message : ");
        fgets(buffer, MAX_BUF_SIZE, stdin);

        // Send the msg
        if (write(socket_fd, buffer, strlen(buffer)) < 0)
            error_handle("Error while writing!\n");
        // Clear the buffer.
        bzero(buffer, MAX_BUF_SIZE);

        // # RECEIVE
        // Read the msg from server.
        if (read(socket_fd, buffer, MAX_BUF_SIZE) < 0)
            error_handle("Error while reading!\n");
        // Show the msg.
        printf("Server: %s", buffer);
    }

    // # CLOSE
    // closing the connection.
    close(socket_fd);
    return 0;
}