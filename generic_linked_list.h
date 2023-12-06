#include <stdint.h>

#define N 3

// (Root) Event Info
typedef struct
{
    uint8_t id;
    uint32_t time;
    // uint8_t root_id;    // who created this root
    // uint32_t pvc[N];    // Physical Vector Clock
} __attribute__((packed)) Event;

// Token
typedef struct {
    uint8_t pid;
    uint32_t eid;   // event id - time
    uint32_t pvc[N];
    uint32_t gcut[N];
    uint32_t depend[N];
    uint8_t target_id;
    uint32_t target_time;
    // uint8_t waiting;
} Token;

typedef struct node {
    void *data;
    struct node *next;
} Node;

void append(Node **head, void *data);
void insert_event(Node **head, Event *ev);
void print_list(Node *head, void (*print)(void *));