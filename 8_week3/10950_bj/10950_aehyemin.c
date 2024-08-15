#include <stdio.h>
#include <stdlib.h>
int main () {

    int a, b, t;
    scanf("%d", &t);

    int *ai = (int *)malloc(t * sizeof(int));

    for (int i=0; i<t; i++) {
        scanf("%d %d", &a, &b);
        ai[i] = a+b;
    }

    for (int i=0; i<t; i++) {
    printf("%d\n", ai[i]);
    }
    free(ai);

    return 0;
}