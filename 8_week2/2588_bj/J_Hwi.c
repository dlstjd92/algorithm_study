#include <stdio.h>

int main()
{
    int n1, n2;
    int r1, r10, r100;
    int value;

    scanf("%d", &n1);
    scanf("%d", &n2);

    r1 = n1 * (n2 % 10);
    r10 = (n1 * ((n2 % 100) / 10));
    r100 = (n1 * ((n2 % 1000) / 100));

    printf("%d\n", r1);
    printf("%d\n", r10);
    printf("%d\n", r100);
    printf("%d\n", n1 * n2);
}
