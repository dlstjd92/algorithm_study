#include <stdio.h>

int main () {
    int a,b,v;
    int cnt=0 
    scanf("%d %d %d", &a,&b,&v);
    //수학 공식을 만들라고? 오우쉣
    

    if (a >= v) {
        printf("1\n");
    } else //첫날에 도착하지 않을떄 
    {   
        int day_move = a-b;
        int one_day_before = v-a;
        int how_day = ((one_day_before + day_move-1) / day_move);
        cnt = 1 + how_day;
        printf("%d\n", cnt);
    }

    return 0;
}

// #include <stdio.h>

// int main () {
//     int a, b, v;
//     int cnt = 0, day_move = 0, how_day = 0;
//     scanf("%d %d %d", &a, &b, &v);
    
//     day_move = a - b;

//     if (a > v) {
//         printf("0");
//     } else {   
//         if ((float)v - a / day_move < (float)v / day_move) {
//             printf("%d", (v - a)/day_move + 1);
//         } else {
//             printf("%d", v / day_move);
//         }
//     }
//     return 0;
// }
// int main () {
//     int a,b,v;
//     int cnt=0 , move= 0;
//     //V미터 높이인 나무 막대
//     //낮에 +A, 밤에 -B. 정상에 도달하면 미끄러지지않음
//     //며칠이 걸리는가?
//     scanf("%d %d %d", &a,&b,&v);
    
//     while (move < v) {
//         move += a;
//         cnt++;
//         if (move >= v) {
//             break;
//         }
//         move -= b;
        
//     }
//     printf("%d", cnt);
//     return 0;

// }