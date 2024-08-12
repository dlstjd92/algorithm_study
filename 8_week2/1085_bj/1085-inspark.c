#define _CRT_SECURE_NO_WARNINGS // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int n1, n2, s1, s2;   

    scanf("%d %d %d %d", &n1, &n2, &s1, &s2);     

    // scanf("%s", &s2); 

    // if (n1 > s1 && n2 > s2) 이런 경우는 일어나지 않네
    // {
    //     printf("%d",sqrt((n1-s1)*(n2-s2)));
    // }

    int min = s1-n1;
    int a = s2-n2;
    int b = n1;
    int c = n2;

    if (a < min) min = a;
    if (b < min) min = b;
    if (c < min) min = c;

    printf("%d",min);

}