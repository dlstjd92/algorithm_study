#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int input,n1 = 1;

    char string[11];

    int ans[10] = {0};

    for (int i = 0; i <3;i++)
    {
        scanf("%d", &input);

        n1 *= input;
    }

    sprintf(string, "%d", n1);

    for (int i = 0; string[i]!='\0'; i++)
    {   
        if(string[i] == '0') ans[0]++;
        else if(string[i] == '1') ans[1]++;
        else if(string[i] == '2') ans[2]++;
        else if(string[i] == '3') ans[3]++;
        else if(string[i] == '4') ans[4]++;
        else if(string[i] == '5') ans[5]++;
        else if(string[i] == '6') ans[6]++;
        else if(string[i] == '7') ans[7]++;
        else if(string[i] == '8') ans[8]++;
        else if(string[i] == '9') ans[9]++;
    }

    for (int i = 0; i<10; i++)
    {   
        printf("%d\n",ans[i]);
    }
    
    return 0;
}