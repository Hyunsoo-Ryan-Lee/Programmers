# 타겟넘버

# def solution(numbers, target):
#     tree = [0]
#     for num in numbers: #1,2,3,4,5
#         sub_tree = []
#         for tree_num in tree: # 0
#             sub_tree.append(tree_num + num)
#             sub_tree.append(tree_num - num)
#         tree = sub_tree
#     return tree


# a = [1,2,3,4,5]
# b = 3

# print(solution(a,b))

'''
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


from itertools import product

numbers = [1,2,3,4,5]
b = 3
l = [(x, -x) for x in numbers] # [(1, -1), (2, -2), (3, -3), (4, -4), (5, -5)]
s = list(map(sum, product(*l))) # *l 하면 (1, -1), (2, -2), (3, -3), (4, -4), (5, -5) 요래 unpacking 되어 나옴
p = list(product(*l)) # product 하면 원하는 순서쌍이 출력된다.
q = list(product(numbers))


abc = [(1,2),(3,4)] # *abc로 하게되면 unpacking되어 (1,2),(3,4) 요래 나옴
#unpacking 하지 않으면 (1,2) 요게 하나의 숫자처럼 취급되어 우리가 원하는 숫자끼리의 조합쌍이 이루어지지 않게됨!!
a = list(product(abc)) # (1,2),(3,4) 요 쌍으로 product 돌리는거임
print(a)
print(*abc)
'''

# from itertools import product

# def solution(numbers,target):
#     ans = []
#     for i in numbers:
#         a = (i,-i)
#         ans.append(a)
    
#     fin = list(map(sum,product(*ans)))
#     return fin.count(target)

# x = [1, 1, 1, 1, 1]
# y = 3
# print(solution(x,y))