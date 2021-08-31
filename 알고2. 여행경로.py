# 프로그래머스 - 여행경로

'''
1. list 내 원소들의 0번 index를 key로 가지는 dictionaty를 만든다.
2. values들을 역순정렬한다.
3. ans = ['ICN'] 여기서부터 출발해서 key값이 같은 녀석의 value를 빼서 추가한다.
4. 이 과정 반복
'''


def solution(tic):
    start = {}
    for i in tic:
        start[i[0]] = start.get(i[0],[]) + [i[1]]

    for i in start:
        start[i].sort(reverse=True)
    
    ans = ['ICN']
    path = []
    while ans:
        if ans[-1] not in start or len(start[ans[-1]]) == 0:
            path.append(ans.pop())
        else:
            ans.append(start[ans[-1]].pop())

    return path[::-1]


tic = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tic))