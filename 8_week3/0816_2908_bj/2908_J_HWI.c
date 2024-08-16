#include <stdio.h>
int main(void)
{
  int A, B, C, D;
  scanf("%d %d", &A, &B);
  C = ((A % 10) * 100) + ((A % 100) - (A % 10)) + ((A - (A % 100)) / 100);
  D = ((B % 10) * 100) + ((B % 100) - (B % 10)) + ((B - (B % 100)) / 100);
  if (C < D)
    printf("%d", D);
  else
    printf("%d", C);
}
