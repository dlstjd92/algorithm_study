#include <stdio.h>
#include <string.h>

int main(void)
{
  int arr[8];
  int asc = 0, desc = 0, none = 0;
  for (int i = 0; i < 8; i++)
    scanf("%d", &arr[i]);
  for (int i = 1; i < 8; i++)
  {
    if (arr[i] == arr[i - 1] + 1)
      asc += 1;
    else if (arr[i] == arr[i - 1] - 1)
      desc += 1;
  }
  if (asc == 7)
    printf("ascending");
  else if (desc == 7)
    printf("descending");
  else
    printf("mixed ");
}