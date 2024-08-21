#include <stdio.h>
int main()
{
    int N, res = 0, num, n1, n10, n100, cnt = 0;
    scanf("%d", &N);

    if (N < 100)res = N;
    else
    {
        for (int i = 110; i <= N; i++)
        {
            num = i;
            n1 = i % 10;
            n10 = (i / 10)%10;
            n100 = (i / 100);
            if (n10 - n1 == n100 - n10)cnt++;
        }
        res = cnt+99;
    }
    printf("%d\n", res);
}