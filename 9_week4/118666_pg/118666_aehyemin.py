def solution(survey, choices):
    # answer = ''
    # return answer
    score = {'R':0, 'T':0,
             'C':0, 'F':0,
             'J':0, 'M':0,
             'A':0, 'N':0}
    for q, answer in zip(survey, choices):
        if answer < 4 :
            score[q[0]] += (4 - answer)
        elif answer > 4 :
            score[q[1]] += (answer - 4)
    result = ''
    if score["R"] >= score["T"] :
        result += "R"
    else :
        result += "T"
        
    if score["C"] >= score["F"] :
        result += "C"
    else :
        result += "F"
        
    if score["J"] >= score["M"] :
        result += "J"
    else :
        result += "M"
        
    if score["A"] >= score["N"] :
        result += "A"
    else :
        result += "N"
        
    return result


    
    
