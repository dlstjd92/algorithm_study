#include <stdio.h>

int main(void){
    int N, t, count;
    int t1, t10, t100;
    count = 0;
    scanf("%d", &N);

    if(N<100){
        printf("%d", N);
    }else{
        //100보다 큰 수는 각 자리수 검사...
        //N보다 작은 수 모두 검사
        for(int i=100; i<=N; i++){
            t = i;
            while(1){
                t100 = (t%1000)/100; //자리수 분리
                t10 = (t%100)/10;
                t1 = t%10;
                //등차수열이 아니라면 빠져나감
                if( (t10-t1) != (t100-t10) ){
                    break;
                }

                //등차수열 통과하면 다음 수 검사
                t = t/10;
                if(t/100 == 0){
                    //다 검사했다면
                    count++;
                    break;
                }
            }
        }
        printf("%d", count+99);
    }

    return 0;
}