def ceil(a):
    if a > round(a):
        return round(a) + 1
    else:
        return round(a)
        
def solution(fees, records):
    answer = []
    cars_info = {}
    cars_num = []

    for record in records:
        time, num, in_out = record.split()
        
        h, m = time.split(":")
        time = int(h) * 60 + int(m)

        if in_out == "IN":
            time = -time
        
        if num in cars_info:
            cars_info[num].append(time)
        else:
            cars_info[num] = [time]
            cars_num.append(num)

    cars_num.sort()

    for car_n in cars_num:
        t_sum = 0

        if len(cars_info[car_n]) % 2 != 0:
            t_sum += 23 * 60 + 59

        t_sum += sum(cars_info[car_n])
        if t_sum < fees[0]:
            charge = fees[1]
        else:
            charge = fees[1] + ceil((t_sum - fees[0]) / fees[2]) * fees[3]
        answer.append(charge)

    return answer

solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"] )