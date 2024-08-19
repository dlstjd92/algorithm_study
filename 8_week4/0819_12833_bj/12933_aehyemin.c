#include <stdio.h>

int main () {
    int a,b,c , i;

    scanf("%d %d %d", &a,&b,&c);  
    if (c % 2 != 0){
        a = a^b;
    }

    printf("%d\n", a);
    return 0;
}





// #include <stdio.h>

// int main () {
//     int a,b,c , i;

//     scanf("%d %d %d", &a,&b,&c);

//     for (i=0; i<c; i++) {
//         a = a^b;
//     }
//     printf("%d\n", a);

//     return 0;
// }