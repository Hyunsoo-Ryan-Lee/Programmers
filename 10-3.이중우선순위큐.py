# 프로그래머스 - 이중우선순위큐


# min, max가 2개 이상일 경우 모두 다 지워질 수 있는 상황이 생기지 않도록 고려

def solution(op):
    ans = []
    for i in op:
        if i.startswith('I'):
            ans.append(int(i[2:]))
        elif i == "D 1":
            for j in ans:
                if j == max(ans):
                    ans.pop(ans.index(j))
        elif i == "D -1":
            for j in ans:
                if j == min(ans):
                    ans.pop(ans.index(j))            
    if len(ans) == 0:
        return [0,0]
    else:
        return [max(ans), min(ans)]




op = ["I 5", "I 5", "D 1", "I 7", "D -1", "I 8"]
print(solution(op))
