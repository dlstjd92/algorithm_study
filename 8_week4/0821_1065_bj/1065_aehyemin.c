#include <stdio.h>
// typedef int bool;
// #define true 1
// #define false 0
#include <stdbool.h>

bool check(int n) {
    int len=0,  arithmetic=0;
    int arr[4] = {0};
    int original = n;

    while (n > 0) {
        arr[len++] = n % 10;
        n /= 10;
    }

    if (len <= 2) {
        return true;
    }
    
    arithmetic = arr[1] - arr[0];
    for (int i=2; i<len; i++) {
        if (arr[i] - arr[i-1] != arithmetic) {
            return false;
        }
    }
    return true;
}


int main() {
    int n, cnt=0;
    scanf("%d", &n);
    
    for (int i=1; i<=n; i++) {
        if (check(i)) {
            cnt++;
        }
    }
    printf("%d\n", cnt);
    return 0;
}
