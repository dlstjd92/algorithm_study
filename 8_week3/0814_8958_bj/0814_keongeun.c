#include <stdio.h>

int main(void)
{
    int N;
    char A[80];
    int score;
    int s;
    scanf("%d", &N);

    for(int i=0; i<N; i++){
        scanf("%s", A);
        
        score=0;
        s=1;

        for(int j=0; A[j]!='\0'; j++){
            if(A[j] == 'O'){
                score += s;
                s++;             
            }
            else{
                s = 1;
            }
        }

        printf("%d\n", score);
    }

    return 0;
}
