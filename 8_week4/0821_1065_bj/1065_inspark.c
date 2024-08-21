#define _CRT_SECURE_NO_WARNINGS // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int num;
    int ans = 0;
    
    scanf("%d", &num);

    for (int i = 1; i < num+1;i++)
    {
        char str[5];
        int gap = 1000;
        int flag = 1;

        sprintf(str, "%d", i);

        for (int j = 0; str[j] != '\0'; j++)
        {
            if (str[j+1] != '\0')
            {
                int temp1, temp2;
                temp1 = str[j] - '0';
                temp2 = str[j+1] - '0';

                if (gap == 1000) gap = temp1 - temp2;
                else if (gap != temp1 - temp2) 
                {
                    flag = 0;
                    break;
                }
            }
        }
        if (flag) {

            ans++;
        }
        
    }
    printf("%d",ans);
}