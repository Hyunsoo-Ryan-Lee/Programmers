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





# 백준 2606번. 바이러스


# total1 = []
# total2 = []
# ans = {}
# while True:
#     a = list(map(int,input().split(' ')))
#     if a[0] != 0:
#         total1.append(a)
#     else:
#         break

# for i in total1:
#     for j in i:
#         total2.append(j)

# for x in set(total2):
#     ans[x] = total2.count(x)
# print(ans)




# 백준 - DFS와 BFS

n=4
p = [(1,2),(1,3),(1,4),(2,4),(3,4)]
graph = [[0]*(n+1) for i in range(n+1)]
visited = [0]*(n+1)
for i in p:
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1
'''
print(graph) -> 방문한 곳을 좌표형식으로 찍어서 행렬처럼 보이게 list에 저장

graph = [[0, 0, 0, 0, 0], 
         [0, 0, 1, 1, 1], 
         [0, 1, 0, 0, 1], 
         [0, 1, 0, 0, 1], 
         [0, 1, 1, 1, 0]]

visited = [0, 0, 0, 0, 0]
'''

def dfs(v):
    visited[v] = 1 # 방문한 곳의 숫자를 1로 변경시킴
    print(v, end='')
    for i in range(1,n+1): # v를 기준으로 나머지 짝이 어떤 녀석인지 찾는다.
        if visited[i] == 0 and graph[v][i]==1:
            dfs(i) # 짝을 찾았으면 해당 숫자로 이동하여 다시 dfs 함수 반복.
print(dfs(1))


