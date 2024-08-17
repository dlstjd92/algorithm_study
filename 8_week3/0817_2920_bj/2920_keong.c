#include <stdio.h>

int main(void){
    char scale[16];

    char *p = scale;

    scanf("%[^\n]s", scale);

    switch(*p){
        case '1':
            while((int)(*p)+1 == (int)*(p+2)){
                p+=2;
            }
            if(p == &scale[14]){
                printf("ascending\n");
                break;
            }
        case '8':
            while((int)(*p)-1 == (int)*(p+2)){
                p+=2;
            }
            if(p == &scale[14]){
                printf("descending\n");
                break;
            }

        default:
            printf("mixed\n");
    }

    return 0;
}
