#include <stdio.h>
#include <stdlib.h>

#include "generic_linked_list.h"

// void append(Node **head, void *data);
// void insert_event(Node **head, void *data);
// void print_list(Node *head, void (*print)(void *));

void append(Node **head, void *data)
{
    Node *new_node = malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;

    if (*head == NULL) {
        *head = new_node;
        return;
    }

    Node *current = *head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = new_node;    
}

void insert_event(Node **head, Event *ev)
{
    Node *new_node = malloc(sizeof(Node));
    new_node->data = ev;
    new_node->next = NULL;

    if (*head == NULL || 
    ev->time < ((Event *)(*head)->data)->time) {
        new_node->next = *head;
        *head = new_node;
        return;
    }

    Node *current = *head;
    while (current->next != NULL && 
    ev->time >= ((Event *)current->next->data)->time)
        current = current->next;
    new_node->next = current->next;
    current->next = new_node;
}

void print_event(void *data)
{
    Event *ev = (Event *)data;
    printf("ID: %u, time: %u\n", ev->id, ev->time);
}

void print_list(Node *head, void (*print)(void *))
{
    Node *current = head;
    while (current != NULL) {
        print(current->data);
        current = current->next;
    }
    printf("\n");
}

Event *new_event(uint8_t id, uint64_t time)
{
    Event *ev = (Event *)malloc(sizeof(Event));
    ev->id = id;
    ev->time = time;
    return ev;
}

int main(void) 
{
    Node *head = NULL;
    Event *ev1 = new_event(1, 100);
    insert_event(&head, ev1);
    print_list(head, print_event);
    Event *ev3 = new_event(1, 50);
    insert_event(&head, ev3);
    print_list(head, print_event);
    Event *ev4 = new_event(1, 150);
    insert_event(&head, ev4);
    print_list(head, print_event);
    Event *ev5 = new_event(1, 20);
    insert_event(&head, ev5);
    print_list(head, print_event);
    Event *ev6 = new_event(1, 70);
    insert_event(&head, ev6);
    Event *ev7 = new_event(1, 200);
    insert_event(&head, ev7);
    print_list(head, print_event);

    return 0;
}