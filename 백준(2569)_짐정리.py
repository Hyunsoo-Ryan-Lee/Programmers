# 백준 - 짐정리
'''
짐 중 가장 적은 무게의 짐을 이용하여 정리하는 알고리즘
'''

# n = int(input())
# bag = []
# for i in range(n):
#     bag.append(int(input()))
# bag = [3, 1, 5, 9]
# sol = sorted(bag)
# ans = 0
# while bag != sol:
#     ind = bag.index(min(bag))
#     if ind != 0:
#         change_ind = bag.index(sol[ind])
#         bag[ind], bag[change_ind] = bag[change_ind], bag[ind]
#         ans += (bag[ind] + bag[change_ind])
#     else:
#         cont = 0
#         for i in range(len(bag)):
#             if bag[i] != sol[i]:
#                 cont += i
#                 break
#         ind2 = bag.index(min(bag[cont:]))
#         bag[0], bag[ind2] = bag[ind2], bag[0]
#         ans += (bag[0] + bag[ind2])
# print(ans)

# def solution(distance, rocks, n):
#     rocks.extend([0,distance])
#     rocks.sort()
#     dis = []
#     for i in range(1,len(rocks)):
#         dis.append(rocks[i]-rocks[i-1])
#     return dis




# dis = 23
# rocks = [3, 6, 9, 10, 14, 17]
# n = 2
# print(solution(dis, rocks, n))



# a = ['ha', 'an', 'nd', 'ds', 'sh', 'ha', 'ak', 'ke']
# b = ['sh', 'ha', 'ak', 'ke', 'ha', 'an', 'nd', 'ds']
# a.sort()
# b.sort()
# if a == b:
#     print('fdd')