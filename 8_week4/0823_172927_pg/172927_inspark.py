def solution(picks, minerals):
    answer = 0
    long = sum(picks)*5
    depth = len(minerals)

    # 일단 5개 묶음으로 끊어서 몇 구획인지 나누기

    # sector = len(minerals) / 5 # 인트로 바꾸는 로직 필요함
    if len(minerals) % 5 != 0:
        sector = len(minerals) // 5 + 1
    else:
        sector = (int)(len(minerals) / 5)
    # matrix = [[0].copy() for _ in range(6)]
    matrix = [[None for _ in range(5+1)] for _ in range(sector)] # 끝은 풋터로 메타데이터값 넣을 예정

    # print(matrix)

    for i in range(sector - 1): # 제일 마지막은 5로 안나눠 떨어질 수 있어서 세그먼트에러 방지
        for j in range(5):
            # print(i,j)
            matrix[i][j] = minerals.pop(0)  # 시간초과 되면 바꾸기 데크로

        # 풋터에 피로도 지수 넣기
        matrix[i][5] = matrix[i].count("diamond")*25 + matrix[i].count("iron")*5 + matrix[i].count("stone")


    for i,j in enumerate(minerals):
        matrix[sector-1][i] = j # 남은 부분 마저 넣기

    matrix[sector-1][5] = matrix[sector-1].count("diamond") * 25 + matrix[sector-1].count("iron") * 5 + matrix[sector-1].count("stone")

    
    # print(matrix)
    # 여기서 범위를 정해줘야함... 곡괭이수가 부족한경우...
    # print(sum(picks)*5, len(minerals))
    if (long<depth):
        matrix = matrix[:sum(picks)]
        print(matrix)
    
    
    matrix.sort(key = lambda x:x[5])

    # print(matrix)

    for i in range(3):
        for j in range(picks[i]):
            # print(answer)

            if len(matrix) == 0:
                return answer

            temp = matrix.pop()
            if i == 0:
                answer += 5
            elif i == 1:
                answer += temp.count("diamond")*5 + temp.count("iron") + temp.count("stone")
            elif i == 2:
                answer += temp[5]

    return answer


