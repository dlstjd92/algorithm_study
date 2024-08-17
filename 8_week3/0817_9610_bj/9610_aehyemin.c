#include <stdio.h>

int main() {
    int x,y,n,i;
    int q1=0, q2=0, q3=0, q4=0, axis=0;
    scanf("%d", &n);
    for (i=0; i<n; i++) {
    scanf("%d %d", &x, &y);
    //각 사분면과 축에 점이 몇 개 있는지
    if(x > 0 && y > 0) {
        q1 += 1;

    } else if (x < 0 && y > 0) {
        q2 += 1;

    } else if (x < 0 && y < 0) {
        q3 += 1;


    } else if (x > 0 && y < 0) {
        q4 += 1;

    } else {
        axis += 1;
    }
}

    printf("Q1: %d\n", q1);
    printf("Q2: %d\n", q2);
    printf("Q3: %d\n", q3);
    printf("Q4: %d\n", q4);
    printf("AXIS: %d\n", axis);

    return 0;
}