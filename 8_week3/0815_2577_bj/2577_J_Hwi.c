#include <stdio.h>
int main()
{
  int A, B, C, all;
  scanf("%d", &A);
  scanf("%d", &B);
  scanf("%d", &C);
  all = A * B * C;
  for (int i = 0; i <= 9; i++)
  {
    int val = all;
    int cnt = 0;
    while (val > 0)
    {
      if (val % 10 == i)
      {
        cnt++;
      }
      val /= 10;
    }
    printf("%d\n", cnt);
  }
}