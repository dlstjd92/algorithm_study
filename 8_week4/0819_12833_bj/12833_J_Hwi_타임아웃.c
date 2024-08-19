#include <stdio.h>
int main()
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    for (int i = 0; i < C; i++)
        A = A ^ B;
    printf("%d", A);
}