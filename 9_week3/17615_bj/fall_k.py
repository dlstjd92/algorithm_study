def move_colors(s):
    s = list(s)  # 문자열을 리스트로 변환
    left = len(s) // 2 - 1  # 중간에서 왼쪽 인덱스
    right = len(s) // 2     # 중간에서 오른쪽 인덱스

    # 'R'과 'B'가 붙어 있는 지점을 찾기
    while left > 0:
        if s[left] != s[right]:
            break
        left -= 1
        right -= 1

    if s[left] == s[right]:
        left = len(s) // 2 - 1  # 중간에서 왼쪽 인덱스
        right = len(s) // 2     # 중간에서 오른쪽 인덱스

        while right < len(s):
            if s[left] == 'R' and s[right] == 'B':
                break
            left += 1
            right += 1

    count = 0


    n_b=0

    #왼쪽에 B가 많은지 R이 많은지 체크함
    for i in range(left):
      if s[i]=='B':
        n_b +=1 
      
    if n_b > (left+1)/2:
      l_char = 'B'
    else:
      l_char = 'R'

    # 왼쪽과 오른쪽을 번갈아 검사
    while left >= 0 or right < len(s):
        if left >= 0:  # 왼쪽 인덱스가 유효하면
            if s[left] != l_char:  # 'R'이면 오른쪽으로 보냄
                r = s.pop(left)

                # 오른쪽에 있는 'B'와 교환
                for i in range(left, len(s)):
                    if s[i] == l_char:
                        s.insert(i, r)
                        count += 1
                        break

        left -= 1  # 커서 이동

        if right < len(s):  # 오른쪽 인덱스가 유효하면
            if s[right] == l_char:  # 'B'이면
                b = s.pop(right)

                # 왼쪽에 있는 'R'과 교환
                for i in range(right - 1, -1, -1):
                    if s[i] != l_char:
                        s.insert(i, b)
                        count += 1
                        break

        right += 1  # 커서 이동

    return count  # 총 이동한 횟수 반환

# 테스트 예시
n = input()
s = input()
c = move_colors(s)
print(c)
