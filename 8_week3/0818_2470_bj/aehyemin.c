#include <stdio.h>
#include <stdlib.h>
#include <limits.h>


int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b); // 오름차순 정렬
}

int main () {//전체 용액의 수N, 용액의 특성값 N개의 정수
    int N,i,a,b;
    scanf("%d", &N);
    int *arr = (int *)malloc(sizeof(int) * N);
    

    for (i=0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), compare);
    
    int min_abs_sum = INT_MAX;
    int liq1 = 0;
    int liq2 = 0;

    int l = 0;
    int r = N - 1;
        
    while (l < r) {
        int sum = arr[l] + arr[r];
        int abs_sum = abs(sum);

        if (abs_sum < min_abs_sum) {
            min_abs_sum = abs_sum;

            liq1 = l;
            liq2 = r;
        } 

        if (sum < 0) {
            l++;

        } else {
            r--;
        }

    }
    
    printf("%d %d\n", arr[liq1], arr[liq2]);

    free(arr);
    return 0;

}

//    if (N % 2 == 0) {
//         int mid1 = N/2;
//         int mid2 = N/2 + 1;
//         printf("%d %d", arr[mid1], arr[mid2]);
//    } else {//N이 홀수일때
//         int mid1 = N/2-1;
//         int mid2 = N/2+1;
//         printf("%d %d", arr[mid1], arr[mid2]);
//    }