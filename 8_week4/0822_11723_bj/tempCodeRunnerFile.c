#include <stdio.h>
#include <string.h>
int main () {
    int m,x, s=0;
    char cal[20];
    scanf("%d", &m);
    for (int i=0; i<m; i++) {

        scanf("%s %d", &cal, &x);

        if (strcmp(cal, "add") == 0) {
            s = s | (1 << (x-1));

        } else if (strcmp(cal, "remove") == 0) {
            s = s & ~(1 << (x-1));

        } else if (strcmp(cal, "check") == 0) {
            if (s & (1 << (x-1))) {
                printf("1\n");
            } else {
                printf("0\n");
            }
            

        } else if (strcmp(cal, "toggle") == 0) {
            s = s ^ (1 << (x-1));

        } else if (strcmp(cal, "all") == 0) {
            s = (1 << 20) -1;

        } else {//empty
            s = 0;

        }
     
    }
    return 0;
}