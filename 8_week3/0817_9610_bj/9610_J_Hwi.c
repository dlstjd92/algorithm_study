#include <stdio.h>

int main(void)
{
  int n, q1 = 0, x[1000][2], q2 = 0, q3 = 0, q4 = 0, AX = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
  {
    scanf("%d %d", &x[i][0], &x[i][1]);
    if (x[i][0] > 0 && x[i][1] > 0) // 1사분면
      q1++;
    else if (x[i][0] < 0 && x[i][1] > 0) // 2사분면
      q2++;
    else if (x[i][0] < 0 && x[i][1] < 0) // 3사분면
      q3++;
    else if (x[i][0] > 0 && x[i][1] < 0) // 4사분면
      q4++;
    else
      AX++;
  }
  printf("Q1: %d\n", q1);
  printf("Q2: %d\n", q2);
  printf("Q3: %d\n", q3);
  printf("Q4: %d\n", q4);
  printf("AXIS: %d\n", AX);
}
