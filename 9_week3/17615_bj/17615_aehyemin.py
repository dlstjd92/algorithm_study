N = int(input())
ball = input()
sp_ball = list(ball)

blue = 0
red = 0
cnt = 0
ans = []

#우측으로 빨간공 보내기
for i in range(N):
    if ball[i] == "R":
        red += 1
    if ball[i] == "B" and red:
        cnt += red
        red = 0
ans.append(cnt)

#우측으로 파란공
blue = 0
cnt = 0
for i in range(N):
    if ball[i] == "B":
        blue += 1
    if ball[i] == "R" and blue:
        cnt += blue
        blue = 0
ans.append(cnt)


#좌측으로 빨간공 보내기
sp_ball.reverse()
red = 0
cnt = 0
for i in range(N):
    if ball[i] == "R":
        red += 1
    if ball[i] == "B" and red:
        cnt += red
        red = 0
ans.append(cnt)

#좌측으로 파란공
blue = 0
cnt = 0
for i in range(N):
    if ball[i] == "B":
        blue += 1
    if ball[i] == "R" and blue:
        cnt += blue
        blue = 0

ans.append(cnt)

print(min(ans))


# print(N)
# print(sp_ball)
# cnt = 0

# B_first = 0
# R_first = 0
# B_final = 0
# R_final = 0
# cnt = 0

# if sp_ball[0] == "R":
#     R_first += 1
#     for i in range(len(sp_ball)):
#         if sp_ball[i+1] == "R":
#             R_first += 1
#         else :
#             break
            
# elif sp_ball[0] == "B":
#     B_first += 1
#     for i in range(len(sp_ball)):
#         if sp_ball[i+1] == "B":
#             B_first += 1
#         else :
#             break

# last = len(sp_ball) - 1  
# if sp_ball[last] == "R":
#     R_final += 1
#     for i in range(last -1, -1, -1):
#         if sp_ball[i] == "R":
#             R_final += 1
#         else :
#             break
            
# elif sp_ball[last] == "B":
#     B_final += 1
#     for i in range(last -1, -1, -1):
#         if sp_ball[i] == "B":
#             B_final += 1
#         else :
#             break
        
# #공은 모두 왼쪽 끝이나 오른쪽 끝으로 이동해야함
# #맨 앞에 연속된 볼의 개수와 맨 뒤에 연속된 볼의 개수를 비교
# # R_first 값이 더 크면 B를 뒤로 옮기거나 맨 앞으로 옮긴다
# if R_first != 0 and R_final !=0 : #앞뒤가 모두 R
#     #R이 적은 쪽을 많은쪽으로 옮긴다
#     if R_first > R_final :
        
  
        
            
    
# if B_first != 0 and B_final !=0 : #앞뒤가 모두 B
#     #B가 적은쪽을 많은쪽으로 옮긴다
    
# if R_first != 0 and B_final !=0 : #앞이 R, 뒤가 B
#     #
    
# if B_first != 0 and R_final !=0 : #앞이 B, 뒤가 R
#     #
    
    
# # # B_first 값이 더 크면 R을 뒤로 옮기거나 맨 앞으로 옮긴다.
# # if R_first < B_first:
    

# print(R_first, B_first, R_final, B_final)