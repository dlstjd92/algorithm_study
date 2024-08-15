#include <stdio.h>
#include <math.h>


int main(void){

    int c; 
    scanf("%d", &c);
    int n;
    int V[1000];
    int s;
    int count;

    for(int i=0; i<c; i++){
        
        scanf("%d", &n);
        s = 0;
        count =0;

        for(int j=0; j<n; j++){
            scanf("%d", &V[j]);
            s += V[j];
        }

        for(int j=0; j<n; j++){
            if(V[j] > (s/n) ){
                count++;
            }
        }

        double p = (count/(double)n)*100;
        p = floor(p*1000+0.5)/1000;


        printf("%.3lf%%\n", p);
    }

    return 0;
}
