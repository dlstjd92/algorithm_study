#include <stdio.h>

int main(void)
{
  int n, x[1000][2];
  int arr[5] = {0, 0, 0, 0, 0};
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
  {
    scanf("%d %d", &x[i][0], &x[i][1]);
    if (x[i][0] > 0 && x[i][1] > 0) // 1사분면
      arr[0]++;
    else if (x[i][0] < 0 && x[i][1] > 0) // 2사분면
      arr[1]++;
    else if (x[i][0] < 0 && x[i][1] < 0) // 3사분면
      arr[2]++;
    else if (x[i][0] > 0 && x[i][1] < 0) // 4사분면
      arr[3]++;
    else
      arr[4]++;
  }
  printf("Q1: %d\n", arr[0]);
  printf("Q2: %d\n", arr[1]);
  printf("Q3: %d\n", arr[2]);
  printf("Q4: %d\n", arr[3]);
  printf("AXIS: %d\n", arr[4]);
}
