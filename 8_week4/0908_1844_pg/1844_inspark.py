def solution(maps):
    trace=[]

    answer = find_road(maps,0,0,0,trace)
    # print("최종값", answer)
    return answer

def find_road(map,h,w,times,trace):
    times+=1
    trace = trace + [[h, w]]
    # print(h,w)
    # 골인지점에 도착햇을떄 멈춤. 막혓을떄 고려안함
    if len(map)-1 == h and len(map[0])-1 == w:
        # print("도착은함?")
        return times
    a = -1
    b = -1
    c = -1
    d = -1
    
    if h+1 < len(map) and map[h+1][w] != 0 and [h+1,w] not in trace:
        a = find_road(map,h+1,w,times, trace)

    if w+1 < len(map[0]) and map[h][w+1] != 0 and [h,w+1] not in trace:
        b = find_road(map,h,w+1,times, trace)

    if h-1 > -1 and map[h-1][w] != 0 and [h-1,w] not in trace and a == -1 and b == -1:
        c = find_road(map, h-1, w, times, trace)

    if w-1 > -1 and map[h][w-1] != 0 and [h,w-1] not in trace and a == -1 and b == -1:
        d = find_road(map, h, w-1,times, trace)
    
    if a == -1 and b == -1 and c == -1 and d == -1:
        return -1
    else:
        if a == -1: a = 10000
        if b == -1: b = 10000
        if c == -1: c = 10000
        if d == -1: d = 10000
        return min(a,b,c,d)
        # return min(x for x in [a, b, c, d] if x != -1) 아주 기가맥힌 문법
    # print(trace)
# solution([[1,1],[1,1]])