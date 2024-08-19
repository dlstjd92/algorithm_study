#include <stdio.h>

int main()
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    
    if(C%2==1)
        printf("%d", A^B);
    else
        printf("%d", A);

    return 0;
}
