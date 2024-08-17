#include <stdio.h>
#include <string.h>
int main(void)
{
  char S[100];
  scanf("%s", &S);
  int len = strlen(S);
  for (int i = 97; i < 123; i++)
  {
    int num = -1;
    for (int j = 0; j < len; j++)
    {
      char alp = i;
      if (S[j] == alp)
      {
        num = j;
        break;
      }
    }
    printf("%d ", num);
  }
}