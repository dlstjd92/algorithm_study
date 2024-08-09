#include <stdio.h>

//김경은 baekjoon 2558 곱셈

int main(void){

    int a, b;

    scanf("%d", &a);
    scanf("%d", &b);

    //1. 숫자 b를 각 자리수별로 분리함
    int b100 = b/100;
    int b10 = (b%100)/10;
    int b1 = (b%100)%10;

    printf("%d\n", b1*a);
    printf("%d\n", b10*a);
    printf("%d\n", b100*a);
    printf("%d\n", b*a);


    return 0;

    
}
