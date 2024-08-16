#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {

    int n1,n2,n3, day, ans;
    
    scanf("%d %d %d", &n1, &n2, &n3);

    day = (n3 - n2)/ (n1-n2) + 1;

    printf("%d", day);
    
    return 0;
}