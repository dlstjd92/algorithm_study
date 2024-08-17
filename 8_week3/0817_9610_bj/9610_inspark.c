#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int num=0, a1=0, a2=0, q1=0, q2=0, q3=0, q4=0, axis = 0;

    scanf("%d", &num);

    for (int i = 0; i < num; i++)
    {
        scanf("%d %d", &a1, &a2);

        if (a1 == 0 || a2 == 0) axis++;
        else if (a1 > 0 && a2 > 0) q1++;
        else if (a1 < 0 && a2 > 0) q2++;
        else if (a1 < 0 && a2 < 0) q3++;
        else if (a1 > 0 && a2 < 0) q4++;
    }

    printf("Q1: %d\n",q1);
    printf("Q2: %d\n",q2);
    printf("Q3: %d\n",q3);
    printf("Q4: %d\n",q4);
    printf("AXIS: %d\n",axis);

    
    return 0;
}