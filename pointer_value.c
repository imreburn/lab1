#include <stdio.h>

void setval(int arr[], int val)
{
    int sval = val;
    arr[0] = sval;
}


int main(void) {
    int arr[3];
    setval(arr, 1);
    printf("%d\n", arr[0]);
    return 0;
}