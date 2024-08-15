#include <stdio.h>

int main() { 
    int i,j, C, N; 
    float sum;
    int score[1000];
   
    scanf("%d", &C);
    //테스트 케이스의 개수C
    //각 테스트 케이스마다 학생의 수 N, N명의 점수 score
    for (i = 0; i<C; i++) {
        scanf("%d", &N);

        sum = 0;

        for (j= 0; j<N; j++) {
            scanf("%d", &score[j]);
        }
        // printf("%d", score[i]);
        for (j=0; j<N; j++) {
            sum += score[j];
        }

        float avr = sum / N;
        int cnt = 0;

        for (j=0; j<N; j++) {
            if(score[j] > avr) {
                cnt++;
            }
        }

        float percentage =  (float)cnt / N * 100;
        printf("%.3f%%\n", percentage);

    }
    return 0;
}