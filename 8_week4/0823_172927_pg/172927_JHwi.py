def solution(picks, minerals):
    answer = 0

    # pink = [dia, iron, stone]
    # minerals = diamond, iron stone

    # 곡괭 수
    total_picks = 0
    for i in picks:
        total_picks += i

    # 캘 수 있는 최대 광물 수
    max_mine = total_picks * 5
    if len(minerals) > max_mine:
        minerals = minerals[:max_mine]

    # 동굴 탐사 [C, Fe, rock]
    cav = [[0, 0, 0] for _ in range(len(minerals) //5 + 1)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            cav[i//5][0] += 1
        elif minerals[i] == 'iron':
            cav[i//5][1] += 1
        else:
            cav[i//5][2] += 1
    # 귀한 금속 순으로 정렬
    cav.sort(key = lambda x:(-x[0], -x[1], -x[2]))

    # play minecreaft
    for i in cav:
        C, Fe, rock = i
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += C + Fe + rock
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += C * 5 + Fe + rock
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += C * 25 + Fe * 5 + rock
                break
    return answer