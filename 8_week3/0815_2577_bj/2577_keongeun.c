#include <stdio.h>

int main(void){

    int a,b,c;
    scanf("%d%d%d", &a, &b, &c);
    
    int s = a*b*c;
    int j = 1;
    int V[10] = {0,};
    int n = 10;


    while((s/n)!=0){
        V[(s%n)/(n/10)] += 1;
        s -= (s%n);
        n = n*10;
    }

    V[(s%n)/(n/10)] += 1;

    for(int i=0; i<10; i++){
        printf("%d\n", V[i]);
    }

    /*  방법 2
    int a,b,c;
    scanf("%d%d%d", &a, &b, &c);
    int s = a*b*c;
    int count;

    for(int i=0; i<10; i++){
        int j = 1;
        count = 0;

        while(j<s){
            if(((s%(j*10))/j)==i)
                count++;
            j = j*10;
        }
        printf("%d\n", count);
    }
    */
    return 0;
}
