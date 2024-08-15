#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int n1,n2, stud = 0;

    float ans;

    scanf("%d", &n1);

    for (int i = 0; i < n1; i++)
    {   
        ans = 0;
        stud = 0;
        
        scanf("%d", &n2);

        int list[n2], sum = 0;

        for (int j = 0; j < n2; j++)
        {
            scanf("%d", &list[j]);

            sum+=list[j];
        }

        sum /= n2;

        for (int j = 0; j < n2; j++)
        {
            if (list[j]>sum) stud++;
        }

        ans = ((float)stud/(float)n2) * 100;

        printf("%.3f%%\n", ans);

    }
    
    
    return 0;
}