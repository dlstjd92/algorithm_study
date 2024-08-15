#include <stdio.h>
#include <string.h>
//몇개의 단어가 있을까? 띄어쓰기 기준으로
int main () {
    int cnt=0;
    char words[1000000];
    scanf("%[^\n]", words);

    char *ptr = strtok(words, " ");

    
    while (ptr != NULL) {
        ptr = strtok(NULL, " ");
        cnt++;
    }

    printf("%d\n",cnt);

    return 0;
}