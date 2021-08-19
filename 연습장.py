
# 프로그래머스 - H-Index

# 1번 풀이 - 정답은 맞추는데 런타임 에러남
# def solution(cit):
#     li = []
#     cit.sort() #[0,1,4,5,6]
#     for i in range(cit[-1]):
#         cnt = 0
#         for j in cit:
#             if j >= i:
#                 cnt += 1
#         if cnt >= i:
#             li.append(i)
#     return max(li)

def solution(cit):
    cit.sort()
    for i in range(len(cit)):
        if cit[i] >= len(cit)-i:
            # i번째의 논문 인용수보다 많은 논문이 'len(cit)-i'개 있다.
            return len(cit)-i
    return 0
cit =  [1,3,4,10,14,16,17,20,20,35]
print(solution(cit))