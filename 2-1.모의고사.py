    # 모의고사

def solution(ans):
    x = [1,2,3,4,5]
    y = [2,1,2,3,2,4,2,5]
    z = [3,3,1,1,2,2,4,4,5,5]
    p = [0,0,0]
    total = []
    for i in range(len(ans)):
        if x[i%5] == ans[i]:
            p[0] += 1
        if y[i%8] == ans[i]:
            p[1] += 1
        if z[i%10] == ans[i]:
            p[2] += 1
    
    return p

ans = [1,3,2,4,2]
print(solution(ans))