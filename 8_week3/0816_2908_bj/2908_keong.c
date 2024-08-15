#include <stdio.h>

int main(void){
    int a, b, r_a, r_b; //올라가는 a미터 내려가는 b미터
    scanf("%d%d", &a, &b);

    //무조건 세 자리 수
    r_a = (a/100);
    a = a%100;
    r_a += ((a/10)*10) + ((a%10)*100);

    r_b = (b/100);
    b = b%100;
    r_b += ((b/10)*10) + ((b%10)*100);

    if(r_a>r_b)
        printf("%d", r_a);
    else
        printf("%d", r_b);


    return 0;
}
