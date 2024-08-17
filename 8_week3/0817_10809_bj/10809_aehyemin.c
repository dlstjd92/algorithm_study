#include <stdio.h>
#include <string.h>

int main () {
    //알파벳 소문자 단어S
    char S[100];
    int alpha[26]={0}, i,j,index,len;
    scanf("%s",S);

    for (i = 0; i < 26; i++) {
        alpha[i] = -1;
    }

    len = strlen(S);

    for (i=0; i<len; i++) { 
        index = S[i] - 'a';
        if (alpha[index] == -1) {
            alpha[index] = i;
        } else {
            continue;
        }
    }
    
    for (j=0; j<26; j++) {
        printf("%d ", alpha[j]);
    }
    return 0;

}
