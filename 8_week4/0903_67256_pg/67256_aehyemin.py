import numpy as np
def solution(numbers, hand):
    # 1 4 7 왼쪽손가락
    # 3 6 9 오른손가락
    # 2 5 8 0 손가락의 거리가 가까운 곳, 거리가 가깝다면 왼손잡이 오른손잡이 따라
    # 왼손은 * 에서 시작, 오른손은 # 에서 시작
    # 내지금 손의 위치 now_hand
    keypad = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ])
    result = []
    left_now = (3, 0)  # '*'의 위치
    right_now = (3, 2)  # '#'의 위치
    
    
    for num in numbers:
        num_pos = tuple(map(int, np.where(keypad == str(num))))
        if num in [1, 4, 7]:
            result.append("L")
            left_now = num_pos
            
        elif num in [3, 6, 9]:
            result.append("R")
            right_now = num_pos
        else :
            l_p = abs(num_pos[0] -left_now[0]) + abs(num_pos[1] - left_now[1])
            r_p = abs(num_pos[0] -right_now[0]) + abs(num_pos[1] - right_now[1])
            if l_p > r_p:
                result.append("R")
                right_now = num_pos
                
            elif l_p < r_p:
                result.append("L")
                left_now = num_pos
                
            else :
                if hand == "left":
                    result.append("L")
                    left_now = num_pos
                elif hand == "right":
                    result.append("R")
                    right_now = num_pos
                    
                    
    return "".join(result)
        