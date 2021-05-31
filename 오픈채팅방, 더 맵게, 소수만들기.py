# <<오픈채팅방>>

'''
record의 각 항을 빈칸 단위로 split하여 새로운 list에 담아준다.
{고유 ID : 이름} 이렇게 매치되는 dictionary를 만들어준다.
1) Leave 일때는 그냥 나가니깐 나간다는 메세지만 append 해주면 된다.
2) Enter 일때는 고유 id 값을 비교하여 바뀐 이름으로 dict에 저장 후 들어왔다는 메세지 append
3) change 일때는 고유 id 값 비교 후 dict에 바뀐 이름으로 저장.
4) id와 메시지가 append된 곳의 각 항들을 이제 출력해주면 되는데 만들어진 dict를 이용하여
id key를 name value로 바꿔서 메세지와 함께 출력.
'''
'''
def solution(record):
    ans = []
    log = []
    match = {}
    for a in record:
        b = a.split(' ')
        if b[0] == 'Leave': log.append([b[1],'님이 나가셨습니다.'])
        elif b[0] == 'Enter':
            match[b[1]] = b[2]
            log.append([b[1],'님이 들어왔습니다.'])
        elif b[0] == 'Change':
            match[b[1]] = b[2]
    for c in log:
        ans.append(match[c[0]] + c[1])
    return ans

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",\
    "Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
'''


# <<더 맵게>>
'''
def solution(s,k):
    ans = 0
    while min(s) < k:
        try:
            s.sort()
            s[0] += s[1]*2
            s.pop(1)
            ans += 1
            if s[0] >= k : break
        except IndexError:
            return -1
    return ans
s = [1, 2, 3, 9, 10, 12]
k = 105
print(solution(s,k))
'''


# <<소수 만들기>>
'''
from itertools import* -> combinations 함수 사용!
combinations(리스트, 뽑는 갯수)



from itertools import*
def solution(a):
    b = list(combinations(a,3))
    c = []
    for i in b:
        c.append(sum(i))
    total = 0
    for i in c:
        ans = 0
        for j in range(1,i+1):
            if i%j == 0:
                ans += 1
        if ans == 2:
            total += 1
    return total
'''

# <<기능개발>>

''' 슈레기같은 코드 ㅋㅋㅋ
from collections import deque 
p1 = [93, 30, 55]	
sp = [1, 30, 5]

def solution(p1,sp):

    p2 = [100-i for i in p1] #[5, 10, 1, 1, 20, 1]
    ans_list = []
    for i in range(len(sp)):
        if p2[i]%sp[i] == 0 : ans_list.append(p2[i]//sp[i])
        else : ans_list.append((p2[i]//sp[i])+1)

    ans = []
    for i in range(len(ans_list)-1):
        for j in range(i+1,len(ans_list)):
            if ans_list[i] < ans_list[j] :
                ans.append(ans_list.index(ans_list[j]))
                
    real_ans = [ans[0]]
    if len(ans)>=2:
        for a in range(len(ans)-1):
            if ans[a+1]-ans[a] != 0:
                real_ans.append(ans[a+1]-ans[a])
    real_ans.append(len(ans)-ans[-1]+1)
    return real_ans'''



import math
def solution(pr, sp):
    n = len(pr)
    remain = [] # [7,3,9]  [5,10,1,1,20,1]
    for i in range(n):
        p = math.ceil((100-pr[i])/sp[i])
        remain.append(p)
    ans = []
    while remain:
        cut = remain.pop(0)
        count = 1
        while len(remain) != 0 and cut >= remain[0]:
            count += 1
            remain.pop(0)
        ans.append(count)
    return ans


pr = [93, 30, 55]	
sp = [1, 30, 5]
print(solution(pr,sp))