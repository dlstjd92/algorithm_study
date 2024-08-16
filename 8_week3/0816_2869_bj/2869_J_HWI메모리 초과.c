#include <stdio.h>
int main(void)
{
  int A, B, V, move = 0, cnt = 0;
  scanf("%d %d %d", &A, &B, &V);
  while (move < V)
  {
    cnt++;
    move += A;
    if (move >= V)
      break;
    move -= B;
  }
  printf("%d", cnt);
}