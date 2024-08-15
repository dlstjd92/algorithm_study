#include <stdio.h>
#include<stdlib.h>


int main () {
    //1. 로꾸꺼 해주기
    //2. 크기비교하기
    int i;
    char a[4], b[4];
    char reverse_a[4], reverse_b[4];
    int int_reverse_a, int_reverse_b;

    scanf("%s %s", a, b);
    
    
    for (i=3; i>=0; --i) {
        reverse_a[2-i] = a[i];
        reverse_b[2-i] = b[i];
    }

    int_reverse_a = atoi(reverse_a);
    int_reverse_b = atoi(reverse_b);


    if (int_reverse_a > int_reverse_b) {
        printf("%d", int_reverse_a);
    } else {
        printf("%d", int_reverse_b);
    }

    return 0;
}