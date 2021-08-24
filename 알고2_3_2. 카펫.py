def solution(brown, yellow):
    tot = brown + yellow
    comp = (brown/2 + 2)
    ans = []
    for i in range(tot//2+1,1,-1):
        if tot%i == 0 and (i + tot//i) == comp:
            ans.append(i)
            ans.append(tot//i)
            break
    return ans

brown = 36
yellow = 64
print(solution(brown, yellow))
