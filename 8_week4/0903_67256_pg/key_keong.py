def get_distance(H, N):
    if H in (2, 5, 8, 11):
        #중간패드에 손이 있음
        return abs(N-H)//3
    else:
        #좌우 이동도 해야함.
        h = H
        if H in (1, 4, 7, 10):
            h += 2
        return abs(N+1-h)//3+1
        
def solution(numbers, hand):
    answer = ''
    L = 10 #왼손 오른손 시작 위치
    R = 12
    
    for i in numbers:
        if i ==0:
            i = 11
            
        if i in (1, 4, 7):
            L = i
            answer += 'L'
        elif i in (3, 6, 9):
            R = i
            answer += 'R'
        else:
            l_d = get_distance(L, i)
            r_d = get_distance(R, i)
            
            #거리계산 후 비교
            if l_d < r_d :
                L = i
                answer += 'L'
            elif l_d > r_d :
                R = i
                answer += 'R'
            else:
                #어느쪽손잡인지에 따라 다름
                if hand == 'left':
                    L = i
                    answer += 'L'
                else:
                    R = i
                    answer += 'R'
            
    return answer
