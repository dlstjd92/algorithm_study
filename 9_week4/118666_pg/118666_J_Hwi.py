def solution(survey, choices):
    answer = ''
    R = T =  C = F = J = M = A = N = 0

    for i in range(len(survey)):
        VS1 = survey[i][0]
        VS2 = survey[i][1]

        cho = choices[i]

        if cho == 1:
            if VS1 == 'R':
                R += 3
            elif VS1 == 'T':
                T += 3
            elif VS1 == 'C':
                C += 3
            elif VS1 == 'F':
                F += 3
            elif VS1 == 'J':
                J += 3
            elif VS1 == 'M':
                M += 3
            elif VS1 == 'A':
                A += 3
            elif VS1 == 'N':
                N += 3

        elif cho == 2:
            if VS1 == 'R':
                R += 2
            elif VS1 == 'T':
                T += 2
            elif VS1 == 'C':
                C += 2
            elif VS1 == 'F':
                F += 2
            elif VS1 == 'J':
                J += 2
            elif VS1 == 'M':
                M += 2
            elif VS1 == 'A':
                A += 2
            elif VS1 == 'N':
                N += 2

        elif cho == 3:
            if VS1 == 'R':
                R += 1
            elif VS1 == 'T':
                T += 1
            elif VS1 == 'C':
                C += 1
            elif VS1 == 'F':
                F += 1
            elif VS1 == 'J':
                J += 1
            elif VS1 == 'M':
                M += 1
            elif VS1 == 'A':
                A += 1
            elif VS1 == 'N':
                N += 1

        elif cho == 4:
            continue
        elif cho == 5:
            if VS2 == 'R':
                R += 1
            elif VS2 == 'T':
                T += 1
            elif VS2 == 'C':
                C += 1
            elif VS2 == 'F':
                F += 1
            elif VS2 == 'J':
                J += 1
            elif VS2 == 'M':
                M += 1
            elif VS2 == 'A':
                A += 1
            elif VS2 == 'N':
                N += 1

        elif cho == 6:
            if VS2 == 'R':
                R += 2
            elif VS2 == 'T':
                T += 2
            elif VS2 == 'C':
                C += 2
            elif VS2 == 'F':
                F += 2
            elif VS2 == 'J':
                J += 2
            elif VS2 == 'M':
                M += 2
            elif VS2 == 'A':
                A += 2
            elif VS2 == 'N':
                N += 2

        elif cho == 7:
            if VS2 == 'R':
                R += 3
            elif VS2 == 'T':
                T += 3
            elif VS2 == 'C':
                C += 3
            elif VS2 == 'F':
                F += 3
            elif VS2 == 'J':
                J += 3
            elif VS2 == 'M':
                M += 3
            elif VS2 == 'A':
                A += 3
            elif VS2 == 'N':
                N += 3
    if R >= T:
        answer += 'R'
    else:
        answer += 'T'

    if C >= F:
        answer += 'C'
    else:
        answer += 'F'
    
    if J >= M:
        answer += 'J'
    else:
        answer += 'M'

    if A >= N:
        answer += 'A'
    else:
        answer += 'N'
    return answer