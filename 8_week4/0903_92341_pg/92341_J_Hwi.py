import math
def solution(fees, records):
    answer = []

    # 딕셔너리 키는 차량 번호
    car_parking_time = dict() # 차들이 들어온 시간
    car_parking_final = dict() # 차들의 총 주차 시간

    for i in records:
        car_time, car_num, car_state = i.split()

        if car_state == "IN":
            car_parking_time[car_num] = car_time

        else: # 아웃이면
            time = car_parking_time[car_num] # 입차시간 가져오기
            acctime = (int(car_time[:2]) - int(time[:2])) * 60 + (int(car_time[3:5]) - int(time[3:5]))

            del car_parking_time[car_num]

            car_parking_final[car_num] = car_parking_final.get(car_num, 0) + acctime

    for car_num in car_parking_time:
        time = car_parking_time[car_num]
        car_time = "23:59"
        acctime = (int(car_time[:2]) - int(time[:2])) * 60 + (int(car_time[3:5]) - int(time[3:5]))

        car_parking_final[car_num] = car_parking_final.get(car_num, 0) + acctime

    for car_num in car_parking_final:
        acctime = car_parking_final[car_num]

        result = 0

        if acctime <= fees[0]:
            result = fees[1]

        else:
            result = fees[1] + math.ceil((acctime - fees[0])/fees[2]) * fees[3]

        car_parking_final[car_num] = result

    total_cars = sorted(car_parking_final)

    for i in total_cars:
        answer.append(car_parking_final[i])

    return answer