#include <stdio.h>
#include <stdlib.h>
int main () {
    int n,x,a,i;
    scanf("%d %d", &n,&x);

    int *arr = (int *)malloc(n * sizeof(int));

    for(i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    for(i=0; i<n; i++) {
        if (arr[i] < x ) {
            printf("%d ", arr[i]);
        }
    }
    free(arr);
    return 0;
}