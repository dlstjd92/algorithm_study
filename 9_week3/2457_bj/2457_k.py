n = int(input())
f=[]
count = 0

for i in range(n):
  f.append(list(map(int, input().split())))


# 피는 시기가 제일 빠른 날짜대로 정렬함
f = sorted(f, key=lambda x: x[1])
f = sorted(f, key=lambda x: x[0])

e_m, e_d = 3, 1


while e_m <= 11:
  list_f = []

  #원하는 날짜 이전에 피는 꽃을 찾아서 배열에 넣음
  for i in f:
    if i[0] < e_m:
      list_f.append(i)
    elif i[0] == e_m and i[1] <= e_d:
      list_f.append(i)

  #제일 늦은 날까지 피는 꽃을 찾음
  list_f = sorted(list_f, key=lambda x: x[3])
  list_f = sorted(list_f, key=lambda x: x[2])
  
  if not list_f:
    count = 0
    break
  a = list_f.pop(-1)
  count += 1
  f.remove(a)
  #print("출력")
  #print(a)

  #원하는 날짜 갱신
  e_m, e_d = a[2], a[3]


print(count)
