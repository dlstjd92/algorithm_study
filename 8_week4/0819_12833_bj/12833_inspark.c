#include <stdio.h>
#include <stdlib.h>

int main() {

    int n1, n2, cnt;   

    scanf("%d %d %d", &n1, &n2, &cnt);

    if (cnt%2 == 0) printf("%d", n1);
    else printf("%d", n1^n2);

    return 0;
}