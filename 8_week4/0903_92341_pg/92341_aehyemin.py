
import math
def solution(fees, records):
    car = {}
    times = {}
    answer = []
    
    for i in records:
        time, number, io = i.split()
        hour, minute = time.split(":")
        t_time = int(hour) * 60 + int(minute)
        
        if io == "IN":
            car[number] = t_time
            
        elif io == "OUT":
            inout_time = t_time - car[number]
            
            if number in times :
                times[number] += inout_time
            else : 
                times[number] = inout_time
            del(car[number])
    print(car, times)
    sort_time = dict(sorted(times.items()))
    print(sort_time)
    
    for num, time in car.items():
        time = 23 * 60 + 59 - time
        if num in times :
            times[num] += time
        else :
            times[num] = time
        
    for num, time in times.items():
        time_d = max(0, time - fees[0])
        money = fees[1] + math.ceil(time_d/fees[2] )* fees[3]
        times[num] = money
        
    times = sorted(times.items())
    
    for num, time in times:
        answer.append(time)
    return answer
        
    
            