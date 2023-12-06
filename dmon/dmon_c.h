#ifndef _DMON_C_H_
#define _DMON_C_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <unistd.h>
#include <sys/select.h>
#include <time.h>

#define N           2   // number of agents
// #define NUM_EVENT   20  // size of local buffer
#define E           0   // clock skew

// Define type and data structures
typedef unsigned int Agent;
typedef double Time;

// Root type
typedef enum {
    LEFT,
    RIGHT,
} RootType;

// Event info
typedef struct {
    Agent agent;
    Time time;
    Time *pvc;  // Physical Vector Clock
    RootType type;
} Event;

// Linked list for local buffers
typedef struct node {
    Event event;
    struct node *next;
} ListNode;

void append(ListNode **ptr_head, Event event) {
    if (*ptr_head == NULL){
        *ptr_head = (ListNode *)malloc(sizeof(ListNode));
        (*ptr_head)->event = event;
        (*ptr_head)->next = NULL;
        return;
    }

    ListNode *current = *ptr_head;
    while (current->next != NULL)
        current = current->next;

    current->next = (ListNode *)malloc(sizeof(ListNode));
    current->next->event = event;
    current->next->next = NULL;
}

void print_list(ListNode *head) {
    ListNode *current = head;

    while (current != NULL) {
        printf("{%d, %.2f, %d} -> ", current->event.agent, current->event.time, current->event.type);
        current = current->next;
    }

    printf("NULL");
    printf("\n");
}

// Define functions
// void abstractor()

#endif