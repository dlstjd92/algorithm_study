#include <stdio.h>
# define MIN(x,y) ( (x)<(y) ? (x):(y) )

int main () {
    int x,y,w,h,min;

    scanf("%d %d %d %d", &x, &y, &w, &h);


    min = (x<y)?x:y;
    min = (min<(w-x))?min:(w-x);
    min = (min<(h-y))?min:(h-y);


    printf("%d\n",min);

    return 0;
}