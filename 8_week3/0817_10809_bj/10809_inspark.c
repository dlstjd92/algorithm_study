#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char s1[100];

    int alph[26];
    memset(alph, -1, sizeof(alph)); // 배열 전체를 -1로 하는 포문같은 친구

    int a;

    scanf("%s", s1);

    for (int i =0; s1[i] != '\0'; i++)
    {   
        a=s1[i]-'a';
        

        if (alph[a] == -1)
        {
            alph[a] = i;
        }
    }
    
    for (int i = 0; i < 26 ; i++)
    {
        printf("%d ", alph[i]);
    }
    
    return 0;
}