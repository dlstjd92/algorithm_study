def score_adder(chars, MBTI, score):
    if chars in MBTI:
        MBTI[chars] += score

def solution(survey, choices):
    answer = ''
    MBTI = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}

    for i in range(len(survey)):
        VS1 = survey[i][0]
        VS2 = survey[i][1]

        cho = choices[i]

        if cho == 1:
            score_adder(VS1, MBTI, 3)
        elif cho == 2:
            score_adder(VS1, MBTI, 2)
        elif cho == 3:
            score_adder(VS1, MBTI, 1)
        elif cho == 4:
            continue
        elif cho == 5:
            score_adder(VS2, MBTI, 1)
        elif cho == 6:
            score_adder(VS2, MBTI, 2)
        elif cho == 7:
            score_adder(VS2, MBTI, 3)

    if MBTI['R'] >= MBTI['T']:
        answer += 'R'
    else:
        answer += 'T'

    if MBTI['C'] >= MBTI['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if MBTI['J'] >= MBTI['M']:
        answer += 'J'
    else:
        answer += 'M'

    if MBTI['A'] >= MBTI['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer