def solution(numbers, hand):
    answer = ''
    L = (3, 0)
    R = (3, 2)
    num_len = len(numbers)

    numpad = {
        1 : (0, 0), 2 : (0, 1), 3 : (0, 2),
        4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
        7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
        '*' : (3 ,0), 0 : (3, 1), '#' : (3, 2)
    }
    print(numbers)
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            L = numpad[i]
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            R = numpad[i]
        else:
            R_road = abs(R[0] - numpad[i][0]) + abs(R[1] - numpad[i][1])
            L_road = abs(L[0] - numpad[i][0]) + abs(L[1] - numpad[i][1])
            if L_road < R_road:
                answer += "L"
                L = numpad[i]
            elif L_road > R_road:
                answer += "R"
                R = numpad[i]
            else:
                if hand == "left":
                    answer += "L"
                    L = numpad[i]
                else:
                    answer += "R"
                    R = numpad[i]
    return answer