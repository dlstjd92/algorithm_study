N = int(input())
balls = input()
cnt = []
#왼쪽 오른쪽을 다 자른다
#rstrip, lstrip

#우측으로 레드 모으기
red_to_right = balls.rstrip("R")
cnt.append(red_to_right.count("R"))

#우측으로 블루 모으기
blue_to_right = balls.rstrip("B")
cnt.append(blue_to_right.count("B"))

#좌측으로 레드 모으기
red_to_left = balls.rstrip("R")
cnt.append(red_to_left.count("R"))
#좌측으로 블루 모으기

blue_to_left = balls.rstrip("B")
cnt.append(red_to_left.count("B"))

print(min(cnt))
