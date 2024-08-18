#include <stdio.h>
#include <stdlib.h> //절대값 변환 abs() 함수 위함

//qsort 비교함수
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main(void){
    int n, zero1, zero2;
    int v[100010];
    int *front, *back; //포인터 두개

    scanf("%d", &n);

    for(int i =0; i<n; i++)
        scanf("%d", &v[i]);

    qsort(v, n, sizeof(int), compare);
    //정렬함
    front = &v[0];
    back = &v[n-1];
    zero1 = v[0];
    zero2 = v[n-1];

    //두 포인터가 만날때까지
    while(front != back){

        //만약 두 수를 더한값이 기존 값보다 더 작다면.
        if(abs(*front+*back) < abs(zero1+zero2)){
            zero1 = *front;
            zero2 = *back;
        }

        //둘중에 절대값이 더 큰 수를 움직임
        if(abs(*front) > abs(*back))
            front ++;
        else
            back--;
    }

    printf("%d %d\n", zero1, zero2);


    return 0;
}
