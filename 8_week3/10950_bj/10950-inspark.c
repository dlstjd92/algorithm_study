#include <stdio.h>
#include <stdlib.h>

int main() {

     int n1;   

    scanf("%d", &n1);

    for (int i = 0; i <n1; i++)
    {
        int a,b = 0;

        scanf("%d %d", &a, &b);

        printf("%d\n", a+b);
    }

    return 0;
}