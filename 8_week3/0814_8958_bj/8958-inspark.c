#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int n1, cnt, ans = 0;
    char str[80];

    scanf("%d", &n1);

    for (int i =0; i <n1; i++)
    {   
        // printf("%s",str);
        // char* list = malloc(strlen(str)*sizeof(char));
        cnt = 0;
        scanf("%s", str);

        

        for (int j = 0; str[j] != '\0'; j++)
        {
            if (str[j] == 'O')
            {
                cnt++;
                ans+=cnt;

            }else{
                cnt = 0;
            }
        }
        printf("%d\n",ans);
        ans=0;
    }
    
    
    return 0;
}