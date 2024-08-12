#include <stdio.h>
#include <stdlib.h>

int main() {

     int n1;   

    scanf("%d", &n1);

    if (n1%4 == 0 && n1%100 != 0)
    {
        printf("%d",1);
    }
    else if (n1%400 == 0)
    {
        printf("%d",1);
    }
    else
    {
        printf("%d",0);
    }

    return 0;
}