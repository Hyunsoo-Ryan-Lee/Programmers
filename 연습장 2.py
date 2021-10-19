

# def solution(begin, target, words):
#     if target not in words:
#         return 0
#     cnt = 0
#     target = list(target)
#     arr = []
#     start = [list(begin)] # [['h', 'i', 't']]
#     comp = []
#     for i in words:
#         arr.append(list(i))

#     while target not in comp:
#         comp = []
#         for i in arr:
#             for j in start: # j = ['h', 'i', 't']
#                 if len(j) + len(set(j+i))-len(j+i) == 1:
#                     comp.append(i)
        
#         arr = [x for x in arr if not x in comp]
#         start = comp
#         cnt += 1
#     return cnt
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
# print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]))
# print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]))

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# print(solution(begin, target, words))

# a = [['h', 'o', 't'], ['d', 'o', 't'], ['d', 'o', 'g'], ['l', 'o', 't'], ['l', 'o', 'g'], ['c', 'o', 'g']]
# b = [['h', 'o', 't'],['d', 'o', 't']]

# p = [i for i in a if not i in b]
# print(p)

# 백준 - 짐정리
'''
짐 중 가장 적은 무게의 짐을 이용하여 정리하는 알고리즘
'''

# n = int(input())
# bag = []
# for i in range(n):
#     bag.append(int(input()))
bag = [3, 1, 5, 9]
sol = sorted(bag)
ans = 0
while bag != sol:
    ind = bag.index(min(bag))
    if ind != 0:
        change_ind = bag.index(sol[ind])
        bag[ind], bag[change_ind] = bag[change_ind], bag[ind]
        ans += (bag[ind] + bag[change_ind])
    else:
        cont = 0
        for i in range(len(bag)):
            if bag[i] != sol[i]:
                cont += i
                break
        ind2 = bag.index(min(bag[cont:]))
        bag[0], bag[ind2] = bag[ind2], bag[0]
        ans += (bag[0] + bag[ind2])
print(ans)

