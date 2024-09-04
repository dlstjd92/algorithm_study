def solution(numbers, hand):
    lh = 10
    rh = 12
    answer = ''

    while (numbers):
        next = numbers.pop(0)
        # print(lh, rh, next)
        if next == 0: next = 11

        if next in [1, 4, 7]:
            answer += 'L'
            lh = next

        elif next in [3, 6, 9]:
            answer += 'R'
            rh = next

        else:

            a = abs(lh - next)
            b = abs(rh - next)

            if a // 3 + a % 3 < b // 3 + b % 3:
                answer += 'L'
                lh = next
            elif a // 3 + a % 3 > b // 3 + b % 3:
                answer += 'R'
                rh = next
            else:
                if hand == 'left':
                    answer += 'L'
                    lh = next
                else:
                    answer += 'R'
                    rh = next

    # print(answer)
    return answer

# def solution(numbers, hand):
#     lh = 10
#     rh = 12
#     answer = ''

#     while (numbers):
#         next = numbers.pop(0)
#         # print(lh, rh, next)
#         if next == 0: next = 11

#         if next in [1, 4, 7]:
#             answer += 'L'
#             lh = next

#         elif next in [3, 6, 9]:
#             answer += 'R'
#             rh = next

#         else:

#             if lh in [2, 5, 8, 11]:
#                 if lh < next: lh+=2
#                 elif lh > next: lh-=4
#                 elif lh == next:
#                     answer += 'L'
#                     lh = next
#                     continue

#             elif rh in [2, 5, 8, 11]:
#                 if rh < next: rh+=4
#                 elif rh > next: rh-=2
#                 elif rh == next:
#                     answer += 'R'
#                     rh = next
#                     continue

#             if abs(lh - next) < abs(rh - 2 - next):
#                 answer += 'L'
#                 lh = next
#             elif abs(lh - next) > abs(rh - 2 - next):
#                 answer += 'R'
#                 rh = next
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     lh = next
#                 else:
#                     answer += 'R'
#                     rh = next

#     # print(answer)
#     return answer

# # solution([4,5,0], "right")

# # solution([1,2,6,0], "left")
# # solution([7,0,2], "right")