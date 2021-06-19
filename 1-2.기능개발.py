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


'''
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

'''
# 다시 연습
import math
def solution(pr,sp):
    ans = [] # [7, 3, 9]
    r_ans = []
    [ans.append(math.ceil((100-pr[i])/sp[i])) for i in range(len(pr))]

    while ans:
        cut = ans.pop(0)
        count = 1
        while len(ans) != 0 and cut >= ans[0]:
            count += 1
            ans.pop(0)
        r_ans.append(count)
    return r_ans


pr = [95, 90, 99, 99, 80, 99]
sp = [1, 1, 1, 1, 1, 1]
print(solution(pr,sp))