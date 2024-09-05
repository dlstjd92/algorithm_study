import math

def solution(fees, records):
    
    # 나는 주차장 입출 기계다..
    car_list = {}
    time_check={}
    answer = []
    
    for i in records:
        i = i.split()
        if i[2] == 'IN':
            car_list[i[1]] = i[0]
        else:
            in_time = car_list.pop(i[1])
            out_time = i[0]
            
            # 시간계산 기릿
            in_time = list(map(int,in_time.split(":")))
            out_time = list(map(int,out_time.split(":")))
            
            if out_time[1] < in_time[1]:
                out_time[1] += 60
                out_time[0] -= 1
            
            result = out_time[1] - in_time[1] + (out_time[0] - in_time[0])*60
            # print(i[1])
            if int(i[1]) in time_check: # 시간 더하기
                
                time_check[int(i[1])] += result
            else:
                time_check[int(i[1])] = result
            
    print(car_list)
    for i in car_list: # 키를 순회하는 형태 여긴 아웃타임까지 나오지 않은 23:59 차량들 처리

        in_time = car_list[i]
        out_time = '23:59'
        
        # 시간계산 기릿
        in_time = list(map(int,in_time.split(":")))
        out_time = list(map(int,out_time.split(":")))
        
        if out_time[1] < in_time[1]:
            out_time[1] += 60
            out_time[0] -= 1
        
        result = out_time[1] - in_time[1] + (out_time[0] - in_time[0])*60

        if int(i) in time_check: # 시간 더하기
            time_check[int(i)] += result
        else:
            time_check[int(i)] = result

    time_check = sorted(time_check.items())

    for i in time_check: # 하루 요금 정산시간
        # fee0 기본시간 fee1 기본요금 fee2 단위시간 fee3 단위요금
        print(i)
        if i[1] > fees[0]:

            temp = math.ceil((i[1]-fees[0])/fees[2])*fees[2] # 일의자리 반올림
            print()
            
            answer.append(int(fees[1] +(temp/fees[2])*fees[3]))
        else:
            answer.append(fees[1])

    
    print(answer)
    return answer


solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])