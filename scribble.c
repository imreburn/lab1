#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h> // memcpy

typedef enum
{
    LEFT = 0,
    RIGHT,
    NOTUSE,
} __attribute__((packed)) RootType ;

int main(void) {
    // int a, b;
    // a = b = 0;
    // printf("a %d and b %d\n", a, b);
    RootType type = NOTUSE;
    int cpy = 0;
    printf("size of enum: %lu\n", sizeof(RootType));
    printf("size of int : %ld\n", sizeof(unsigned long));
    memcpy(&cpy, &type, sizeof(RootType));
    printf("cpy: %d\n", cpy);
}

int practice_fork(void)
{
    unsigned int pc = 0;
    pid_t pid;
    for (int i = 0; i < 2; i++) {
        pid = fork();
        if (pid == 0) {
            printf("child and i = %d\n", i);
            exit(0);
        }
    }
}