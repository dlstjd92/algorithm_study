#include <stdio.h>
#include <string.h>
int main()
{
  char txt[1000000];
  scanf("%[^\n]", txt);
  int N = strlen(txt);
  int cnt = 0;

  if (txt[0] != ' ')
    cnt++;
  for (int i = 1; i < N; i++)
  {
    if (txt[i - 1] == ' ' && txt[i] != ' ')
      cnt++;
  }
  printf("%d\n", cnt);
}