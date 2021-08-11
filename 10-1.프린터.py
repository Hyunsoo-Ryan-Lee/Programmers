# 프로그래머스 - 프린터

def solution(p,l):
    ind = []
    ind_ans = []
    for i in range(len(p)):
        ind.append([i,p[i]])
    ans = []
    while len(p) != 0:
        if p[0] < max(p):
            p.append(p.pop(0))
            ind.append(ind.pop(0))
        else:
            ans.append(p.pop(0))
            ind_ans.append(ind.pop(0))
    for i in range(len(ind_ans)):
        if ind_ans[i][0] == l:
            fin = ind_ans[i]
    return ind_ans.index(fin)+1