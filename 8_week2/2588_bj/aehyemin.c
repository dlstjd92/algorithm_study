//  (3)에는 (1) x (2)의 일의자리 수
//  (4)에는 (1) x (2)의 십의자리 85면 80
//  (5)에는 (1) x (2)의 백의자리 
// (6)은 결과

#include <stdio.h>

int main () {
    int a;
    int b;
    int third, fourth, fifth;

    scanf("%d", &a);
    scanf("%d", &b);

    third = a * (b%10);
    fourth = a * (b%100 - b%10);
    fifth = a *(b - b%100);

    printf("%d\n", third);
    printf("%d\n", fourth/10);
    printf("%d\n", fifth/100);
    printf("%d\n",a*b);

    return 0;
}