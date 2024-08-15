#include <stdio.h>
#include <string.h>

int main () {
    int t, cnt, i, j;
    char ox[80];

    scanf("%d", &t);

    for (i=0; i<t; i++) {
        scanf("%s\n", ox);

        int cnt = 0;
        int score = 0;

        for (j=0; j<strlen(ox); j++) {
            if (ox[j] == 'O') {
                cnt++;
                score += cnt;
            } else {
                cnt = 0;
            }
        }
        printf("%d\n", score);
    }

    return 0;
}
