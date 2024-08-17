#include <stdio.h>
#include <string.h>

int main(void){
    char str[100];
    int D[26];
    
    // -1로 배열 초기화. byte 단위로 초기화하므로 0과 -1로 초기화할 수 있다.
    memset(D,-1,sizeof(D));


    scanf("%s", str);

    for(int i =0; str[i]!='\0'; i++){
        int c = (int)str[i]-97;
        if( D[c] == -1 )
            D[c] = i;
    }

    for(int j=0; j<26; j++){
        printf("%d ", D[j]);
    }


    return 0;
}
