ball = int(input())

ball_list = list(input())

left_ptr = 0
right_ptr = len(ball_list)-1

left_color = ball_list[left_ptr]
right_color = ball_list[right_ptr]

r_count = ball_list.count('R')
b_count = ball_list.count('B')

while(left_ptr < len(ball_list) and ball_list[left_ptr] == left_color):
    left_ptr +=1

while(right_ptr > 0 and ball_list[right_ptr] == right_color):
    right_ptr -=1

# print(left_ptr, right_ptr)

answer = 0

# if left_ptr > len(ball_list)-1-right_ptr:

#     if left_color == 'B':
#         b_count -= left_ptr

#         if b_count > r_count:

#             # BB R BBBB R <- 예외 발견
#             if right_color != left_color:
#                 answer = r_count-right_ptr
#             else:
#                 answer = r_count
            
#         else:
#             answer = b_count
#             # R BBB R B RRR
#     else: # left_color가 R 일떄

#         r_count -= left_ptr

#         if r_count> b_count:

#             if right_color != left_color:
#                 answer = b_count-right_ptr
#             else:
#                 answer = b_count
#         else:
#             answer = r_count

# else:
#     if right_color == 'B':
#         b_count -= right_ptr

#         if b_count > r_count:

#             # BB R BBBB R <- 예외 발견
#             if right_color != left_color:
#                 answer = r_count-left_ptr
#             else:
#                 answer = r_count
            
#         else:
#             answer = b_count
#             # R BBB R B RRR
#     else: # left_color가 R 일떄
#         r_count -= right_ptr

#         if r_count> b_count:

#             if right_color != left_color:
#                 answer = b_count-left_ptr
#             else:
#                 answer = b_count
#         else:
#             answer = r_count

    # 구석지에 무슨색이 몇개 있는지 알아냄 -> 폐기
# if left_ptr != len(ball_list)-1-right_ptr:
    
#     break

    # 만약 구석 색 길이가 같다면.. 색 갱신해서 다음 청크 확인
# left_color = ball_list[left_ptr]
# right_color = ball_list[right_ptr]
    # 11110110011

left_r_moves = r_count - ball_list[:left_ptr].count('R')
right_r_moves = r_count - ball_list[right_ptr + 1:].count('R')

left_b_moves = b_count - ball_list[:left_ptr].count('B')
right_b_moves = b_count - ball_list[right_ptr + 1:].count('B')

# 최소 이동 횟수 계산
answer = min(left_r_moves, right_r_moves, left_b_moves, right_b_moves)

# 결과 출력
# print(answer)

print(answer)