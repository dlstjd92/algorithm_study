#define _CRT_SECURE_NO_WARNINGS // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s1[4];   // 크기가 10인 char형 배열을 선언

    char s2[4];

    // printf("\n입력");
    scanf("%s", &s1);     // 표준 입력을 받아서 배열 형태의 문자열에 저장
    // printf("\n입력");
    scanf("%s", &s2); 

    // printf("\n입력");
    int s1_int = atoi(s1);
    // char a = s2[2];

    // printf("\n%s",s1);
    // printf("\n%s",s2);

    // printf("%s", a);
    int s2_100 = s2[0]-'0';
    int s2_10 = s2[1]-'0';
    int s2_1 = s2[2]-'0';

    // printf("%d",s112_int);
    // printf("%d",s2_100);

    printf("%d\n",s1_int*s2_1);
    printf("%d\n",s1_int*s2_10);
    printf("%d\n",s1_int*s2_100);
    printf("%d\n",s1_int*s2_100*100 + s1_int*s2_10*10 + s1_int*s2_1);

    return 0;
}
