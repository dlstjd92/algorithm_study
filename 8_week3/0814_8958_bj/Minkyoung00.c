#include <stdio.h> 

int main(){
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++){
        int score = 0, pre = 0;
        char str[80];
        char *cur = str;
        
        scanf("%s", str);

        while (*cur){
            if (*cur == 'O'){
                score += pre + 1;
                pre++;
            }
            else pre = 0;
            
            cur++;
        }
        
        printf("%d\n",score);
    }

    return 0;
}