#include <stdio.h>

int main(void){
    int N = 0;
    scanf("%d", &N);

    int sol_neg[100000] = {0,}; 
    int sol_pos[100000] = {0,};
    int temp = 0, neg_cur = 0, pos_cur = 0;
    int sol1 = 0, sol2 = 0, min = 2000000001;
    int sum = sol1 + sol2;

    for (int i = 0; i < N; i++){
        scanf("%d", &temp);

        if (temp < 0) {
            sol_neg[neg_cur];
            neg_cur++;
        }
        else {
            sol_pos[pos_cur];
            pos_cur++;
        }
    }

    if (neg_cur == N){
        // sol_neg에서 제일 큰 수 2개
        sol1 = sol_neg[neg_cur];
        for(; neg_cur>=0; neg_cur++){
            if(sol1 < sol_neg[neg_cur]){
                
            }
        }
    }
    else if (neg_cur == 0){
        // sol_pos에서 제일 작은 수 2개
    }
    else{
        while(neg_cur >= 0){
            while(pos_cur >= 0){
                sum = sol_neg[neg_cur] + sol_pos[pos_cur];

                if (sum > 0 && sum < min) {
                    min = sum;
                    sol1 = sol_neg[neg_cur];
                    sol2 = sol_pos[pos_cur];
                }
                else if(sum < 0 && -sum < min) {
                    min = -sum;
                    sol1 = sol_neg[neg_cur];
                    sol2 = sol_pos[pos_cur];
                }
                pos_cur--;
            }
            neg_cur--;
        }
    }

    printf("%d %d", sol1, sol2);

    return 0;
}