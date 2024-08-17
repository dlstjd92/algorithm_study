#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int music[9];

    for (int i = 0; i < 8; i++)
    {
        scanf("%d", &music[i]);
    }

    switch (music[0])
    {
    case 1:
        for (int i =0; i < 7 ; i++)
        {   
            if (music[i]+1 != music[i+1])
            {
                printf("mixed");
                return 0;
            }
            else if (i == 6 && music[i]+1 == music[i+1])
            {
                printf("ascending");
                return 0;
            }
        }
    case 8:
        for (int i =0; i < 7 ; i++)
        {   
            if (music[i] != music[i+1]+1)
            {

                printf("mixed");
                return 0;
            }
            else if (i == 6 && music[i] == music[i+1]+1)
            {
                printf("descending");
                return 0;
            }
        }
    default:
        printf("mixed");
        break;
    }

    
    return 0;
}