#include <stdio.h>
#include <stdint.h>

static uint8_t right_roots[5];

// int main(void)
// {
//     for (int i = 0; i < 5; i++) {
//         printf("i = %d\n", i);
//     }

//     printf("i = %d\n", i);
// }

// global variable initialization
int main(void)
{
    for (int i = 0; i < 5; i++) {
        printf("right_roots[%d] = %u\n", i, right_roots[i]);
    }
    return 0;
}