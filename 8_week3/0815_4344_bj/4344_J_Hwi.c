#include <stdio.h>
int main()
{
  int C;

  scanf("%d", &C);
  for (int i = 0; i < C; i++)
  {
    int N;
    scanf("%d", &N);
    float arr[1000];
    float sum = 0;
    float avg = 0;

    for (int j = 0; j < N; j++)
    {
      scanf("%f", &arr[j]);
      sum += arr[j];
    }
    avg = sum / N;

    int cnt = 0;
    for (int j = 0; j < N; j++)
    {
      if (arr[j] > avg)
      {
        cnt++;
      }
    }
    printf("%.3f%%\n", (cnt * 100.0) / N);
  }
}