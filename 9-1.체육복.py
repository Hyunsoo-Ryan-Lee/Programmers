#프로그래머스 - 체육복

def solution(n, lost, reserve):
    a = n-len(lost)
    b = []
    for i in lost:
        b.append(i+1)
        b.append(i-1)
    b = list(set(b))
    for i in reserve:
        if i in b:
            a += 1
    return n if a>=n else a



# def solution(n, lo, re) :
#     ans = 0
#     a = n-len(lo)
#     for i in lo :
#         if i-1 in re : 
#             ans += 1
#             re.remove(i-1)
#         elif i+1 in re : 
#             ans += 1
#             re.remove(i+1)
#     return a+ans