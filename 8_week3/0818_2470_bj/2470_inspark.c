#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int a, min = 100001, num1, num2;

    scanf("%d", &a);

    int arr[a];
    for (int i = 0; i < a; i++) scanf("%d", &arr[i]);

    for (int i = 0; i < a; i++)
    {
        for (int j = i+1; j < a; j++)
        {
            if (abs(arr[i]+arr[j]) < min)
            {
                min = abs(arr[i]+arr[j]);
                num1 = arr[i];
                num2 = arr[j];
            }
            
        }
    }

    printf("%d %d",num1, num2);
    
    return 0;
}