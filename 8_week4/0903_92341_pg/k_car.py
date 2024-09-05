import math

def solution(fees, records):
    answer = []
    
    i = 0 #배열의 위치 포인터
    num = {} #자동차 배열
    car = []
    
    for j in records:
        t, n, s = j.split()
        h, m = map(int, t.split(':'))
        m += (h*60)
        
        #입차 출차 분리
        if s == 'IN':    
            #입차 기록이 없다면 추가
            if not n in num: 
                car.append([n,0])
                num[n] = [i, m]
                i+=1
            else:
                #입차시 시간 기록.
                num[n][1] = m
            
        else:
            #출차. 기존 기록
            car[num[n][0]][1] += m - num[n][1]
            num[n][1] = -1
            
    #모든 입출차 기록 조회 완료. 입차만 되고 출차 안된 차량 처리
    for j1, j2 in num.items():
        if j2[1] != -1:
            car[j2[0]][1] += (23*60)+59 - j2[1]
            num[j1][1] = -1 
        
        
    #주차 요금 계산
    car.sort()
    
    for c in car:
        c1 = c[1]
        
        charge = c1-fees[0]
        if charge <= 0:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil(charge/fees[2])*fees[3]))

  
    return answer
