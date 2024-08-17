#include <stdio.h>

int main(void){
    
    int n,x,y; //점의 갯수, 좌표
    int d[5] ={0}; //사분면

    scanf("%d", &n);

    for(int i =0; i<n; i++){
        scanf("%d%d", &x, &y);

        if(x==0 || y==0){
            d[4]++;
            continue;
        }

        if(x<0)
            y<0 ? d[2]++ : d[1]++;
        else if(x>0)
            y<0 ? d[3]++ : d[0]++;
    }

    printf("Q1: %d\n", d[0]);
    printf("Q2: %d\n", d[1]);
    printf("Q3: %d\n", d[2]);
    printf("Q4: %d\n", d[3]);
    printf("AXIS: %d\n", d[4]);
        
    return 0;
}
