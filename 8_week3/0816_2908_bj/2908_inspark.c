#include <stdio.h>

int main() {
    char num1[4], num2[4];  

    scanf("%3s %3s", num1, num2);

    int a1, a2;

    for (int i = 2; i > -1 ; i--) {
        a1 = num1[i] - '0';  
        a2 = num2[i] - '0';  

        if (a1 > a2) {
            printf("%c%c%c", num1[2], num1[1], num1[0]);
            break;
        } else if (a1 < a2) {
            printf("%c%c%c", num2[2], num2[1], num2[0]);
            break;
        }
    }

    return 0;
}
