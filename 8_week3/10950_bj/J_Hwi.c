#include <stdio.h>
int main()
{
    int A, B, T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        scanf("%d %d", &A, &B);
        printf("%d\n", A + B);
    }
}