#include <stdio.h>

int main(void){
    
    char s[1000010];
    int count = 1;

    scanf("%[^\n]s", s);

    int i=0;

    while(s[i] == ' ')
        i++;
    

    if(s[i] == '\0'){
        printf("0");
        return 0;
    }

    while(s[i] != '\0'){
        if(s[i] == ' '){
            if(s[i+1] != '\0')
                count++;
        }
        i++;
    }

    printf("%d", count);

    return 0;
}
