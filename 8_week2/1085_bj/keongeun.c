#include <stdio.h>

int main(void){

  int a, b, c, d;
  scanf("%d%d%d%d", &a, &b, &c, &d);
  int min = 0;

  //x좌표 비교
  min = a<(c-a)?a:c-a;
  
  //y좌표 비교
  if(b<min || d-b<min){
    min = b<(d-b)?b:d-b;
  }

  printf("%d",min);

  return 0;
}
