#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int n1, n2;

    scanf("%d %d", &n1, &n2);

    int num;

    for (int i =0; i <n1; i++)
    {
        scanf("%d", &num);

        if (num < n2)
        {
            printf("%d ", num);
        }
    }

    return 0;
}