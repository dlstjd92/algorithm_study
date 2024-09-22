def solution(survey, choices):
    answer = ''
    #       비동의 동의
    # 1번 지표 R - T
    # 2번 지표 C - F
    # 3번 지표 J - M
    # 4번 지표 A - N
    # 점수는 -3 ~ 3 
    # 점수가 같을시 사전순으로 빠른 성격유형이 정답

    # 음수써서 4개 하기 vs 각각 점수재서 8개 하기

    mbti = [0,0,0,0]
    
    for i,value in enumerate(survey):
        if value == "RT":
            mbti[0] += choices[i]-4
        elif value =="TR":
            mbti[0] += 4-choices[i]
        elif value == "CF":
            mbti[1] += choices[i]-4
        elif value == "FC":
            mbti[1] += 4-choices[i]
        elif value == "JM":
            mbti[2] += choices[i]-4
        elif value == "MJ":
            mbti[2] += 4-choices[i]
        elif value == "AN":
            mbti[3] += choices[i]-4
        elif value == "NA":
            mbti[3] += 4-choices[i]

    if mbti[0] > 0:
        answer += 'T'
    else:
        answer += 'R'
    
    if mbti[1] > 0:
        answer += 'F'
    else:
        answer += 'C'
    
    if mbti[2] > 0:
        answer += 'M'
    else:
        answer += 'J'
    
    if mbti[3] > 0:
        answer += 'N'
    else:
        answer += 'A'



    return answer