#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char input[1000000];

    scanf("%[^\n]",input);

    int ans = 1;
    int i;

    for (i = 0; input[i] != '\0' ;i++)
    {
        if (input[i] == ' ') ans++;
    }
    
    if (input[0] == ' ') ans--;
    if (input[i-1] == ' ') ans--;

    printf("%d", ans);
    
    return 0;
}