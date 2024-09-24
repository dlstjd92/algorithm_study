def solution(survey, choices):
    answer = ''
    
    #각 점수 배열 만듬
    #4개로 해서 -는 TFMN임.
    
    
    MBTI = [0, 0, 0, 0]
    
    for i in survey:
        score = choices.pop(0)-4
        
        #문제 받은 뒤, 점수에 따라 분리
        if i[0] == "R":
            MBTI[0] -= score
        elif i[0] == "T":
            MBTI[0] += score
            
        elif i[0] == "C":
            MBTI[1] -= score
        elif i[0] == "F":
            MBTI[1] += score
        
        elif i[0] == "J":
            MBTI[2] -= score
        elif i[0] == "M":
            MBTI[2] += score
        
        elif i[0] == "A":
            MBTI[3] -= score
        elif i[0] == "N":
            MBTI[3] += score
    
    if MBTI[0] >= 0:
        answer += "R"
    else:
        answer += "T"
    
    if MBTI[1] >= 0:
        answer += "C"
    else:
        answer += "F"
        
    if MBTI[2] >= 0:
        answer += "J"
    else:
        answer += "M"
        
    if MBTI[3] >= 0:
        answer += "A"
    else:
        answer += "N"
    
    
    return answer
