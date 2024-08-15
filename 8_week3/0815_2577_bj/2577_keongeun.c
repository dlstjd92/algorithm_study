#include <stdio.h>

int main(void){
    int a,b,c;
    scanf("%d%d%d", &a, &b, &c);
    
    int s = a*b*c;
    int count;

    for(int i=0; i<10; i++){
        int j = 1;
        count = 0;

        while(j<s){
            if(((s%(j*10))/j)==i){
                count++;
            }

            j = j*10;
        }

        printf("%d\n", count);
    }
}
