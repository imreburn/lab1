#include <stdio.h>

int main(void)
{
    int a[5];
    for (int i=0; i<5; i++) {
        a[i] = i;
    }
    int *p1 = &a[1];
    int *p2 = &a[4];
    int res = p2 - p1;
    printf("%d\n", res);
    return 0;
}