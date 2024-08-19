#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void quick (int arr[], int start, int end) {

        if (start >= end) {
        return;
    }
    int mid = (start+end)/2;

    if (arr[start] > arr[mid]) {
        int temp = arr[start];
        arr[start] = arr[mid];
        arr[mid] = temp;
    }
    if (arr[start] > arr[end]) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
    }
    if (arr[mid] > arr[end]) {
        int temp = arr[mid];
        arr[mid] = arr[end];
        arr[end] = temp;
    }
    int pivot = arr[mid];
    int ptr1 = start+1 ,ptr2 = end-1;

    while (ptr1<=ptr2)
    {
        while (arr[ptr1]< arr[mid])
        {
            ptr1++;
        }
        while (arr[mid]< arr[ptr2])
        {
            ptr2--;
        }

        if (ptr1 <= ptr2) {
            // ptr1과 ptr2의 값을 교환
            int temp = arr[ptr1];
            arr[ptr1] = arr[ptr2];
            arr[ptr2] = temp;

            ptr1++;
            ptr2--;
        }

        // -99 -100 4 6 5 90 98
    }

    quick(arr, start, ptr2);
    quick(arr, ptr1,end);

}

int main() {

    int a, num1, num2;

    scanf("%d", &a);

    int arr[a];
    for (int i = 0; i < a; i++) scanf("%d", &arr[i]);

    quick(arr, 0, a-1);

    // if (arr[0] > 0 )
    // {
    //     printf("%d %d",arr[0], arr[1]);
    // } else if (arr[a-1]<0)
    // {
    //     printf("%d %d", arr[a-2], arr[a-1]);
    // }


    num1 = 0, num2 = a-1;

    int ans = 1000001;

    int ansN1, ansN2; 

    while (num1 < num2)
    {
        if (arr[num1]+arr[num2]> 0)
        {
            if (abs(arr[num1]+arr[num2]) < ans)
            {
                ans = abs(arr[num1]+arr[num2]);
                ansN1 = num1, ansN2 = num2;
            }

            num2--;
        }
        else
        {
            if (abs(arr[num1]+arr[num2]) < ans)
            {
                ans = abs(arr[num1]+arr[num2]);
                ansN1 = num1, ansN2 = num2;
            }

            num1++;
        }
    }

    printf("%d %d",arr[ansN1], arr[ansN2]);
    
    return 0;
}

