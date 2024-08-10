#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, y, w, h;
    int pos[4];
    int minval;
    scanf("%d %d %d %d", &x, &y, &w, &h);

    pos[0] = w - x;
    pos[1] = x;
    pos[2] = h - y;
    pos[3] = y;

    minval = pos[0];
    for (int i = 1; i < 4; i++)
    {
        if (minval > pos[i])
        {
            minval = pos[i];
        }
    }
    printf("%d\n", minval);
}