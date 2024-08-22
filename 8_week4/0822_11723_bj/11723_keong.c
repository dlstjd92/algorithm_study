#include <stdio.h>
#include <string.h>

int main(void){
    int M, N, S  = 0;
    char str[10];
    char *p;
    scanf("%d", &M);

    for(int i=0; i<M; i++){
        getchar(); //버퍼 비움
        scanf("%[^\n]s", str);
        if(strstr(str, "add")){
            p = strstr(str, "add") + 4;
            N = 1 << (atoi(p)-1); 
            S = S | N;
        }else if(strstr(str, "remove")){
            p = strstr(str, "remove") + 7;
            N = 1 << (atoi(p)-1); 
            S = S & ~N;
        }else if(strstr(str, "check")){
            p = strstr(str, "check") + 6;
            N = 1 << (atoi(p)-1);
            if((S&N)!= 0)
                printf("1\n");
            else
                printf("0\n");
        }else if(strstr(str, "toggle")){
            p = strstr(str, "toggle") + 7;
            N = 1 << (atoi(p)-1); 
            if((S&N)!= 0)
                S = S & ~N;
            else
                S = S | N;
        }else if(strstr(str, "all")){
            S = 1048575;
        }else if(strstr(str, "empty")){
            S = 0;
        }
    }
    return 0;
}
