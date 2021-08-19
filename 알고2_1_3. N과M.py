def solution(a,b):
    li = list(range(1, a+1)) # 1,2,3,4
    ans_list = []
    for i in li:
        s = [i]
        for j in range(i+1,li[-1]+1):
            if j in s:
                continue
            if j>s[-1]:
                s.append(j)
                if len(s) == b:
                    ans_list.append(s)
                    s = s[:-1]
            
    for ans in ans_list:
        print(*ans)

print(solution(6,2))