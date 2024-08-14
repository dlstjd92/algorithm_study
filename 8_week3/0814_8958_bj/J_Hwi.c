#include <stdio.h>
#include <string.h>
int main()
{
    int n;
    scanf("%d", &n);

    char arr[100];

    for (int i = 0; i < n; i++)
    {
        int sum = 0;
        int plus = 1;
        scanf("%s", &arr);
        for (int j = 0; j < strlen(arr); j++)
        {
            if (arr[j] == 'O')
            {
                sum += plus;
                plus++;
            }
            if (arr[j] == 'X')
                plus = 1;
        }
        printf("%d\n", sum);
    }
}