#include <stdio.h>
#include <stdlib.h>

int main() {

    int n1;
     

    scanf("%d", &n1);

    int arr[21] = {0};

    for (int i = 0; i < n1; i++)
    {
        char s[7];
        int a;

        scanf("%s %d", &s, &a);

        switch (s[0])
        {
        case 'a':
            if (s[1] == 'd') 
            {
                // printf("%s", s);
                arr[a] = 1;
                // printf("더함");
            }
            
            else for (int j = 0; j < 22; j++) arr[j] = 1;
            break;

        case 'r':
            arr[a] = 0;
            break;

        case 'c':
            if (arr[a] == 1) printf("%d\n",1);
            else printf("%d\n",0);
            break;

        case 't':
            if (arr[a] == 1) arr[a] = 0;
            else arr[a] = 1;
            break;
        case 'e':
            for (int j = 0; j < 22; j++) arr[j] = 0;
            break;

        default :
            printf("아무곳도 거치지 않았다");
        }

        
        
    }


    return 0;
}