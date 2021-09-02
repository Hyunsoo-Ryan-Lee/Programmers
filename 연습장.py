# n = 11
# line = [802, 743, 457, 539]

# start = 1
# end = max(line)

# while start <= end:
#     ans = 0
#     mid = (start+end)//2
#     for i in line:
#         ans += i//mid
    
#     if ans<n:
#         end = mid-1
#     else:
#         start = mid+1

# print(end)


# def max_no(num):
#     return max(num[0], num[-1])
'''
def solution(num):
    me = 0
    friend = 0
    if len(num) == 1:
        return num[0]

    if len(num)%2 == 1:
        while len(num) != 1:
            max_no1 = max(num[0], num[-1])
            if max_no1 == num[0]:
                me += num.pop(0)
                max_no2 = max(num[0], num[-1])
                if max_no2 == num[0]:
                    friend += num.pop(0)
                elif max_no2 == num[-1]:
                    friend += num.pop()
            
            if max_no1 == num[-1]:
                me += num.pop()
                max_no2 = max(num[0], num[-1])
                if max_no2 == num[0]:
                    friend += num.pop(0)
                elif max_no2 == num[-1]:
                    friend += num.pop()
        me += num[0]
        
    else:
        while len(num) != 2:
            max_no1 = max(num[0], num[-1])
            if max_no1 == num[0]:
                me += num.pop(0)
                max_no2 = max(num[0], num[-1])
                if max_no2 == num[0]:
                    friend += num.pop(0)
                elif max_no2 == num[-1]:
                    friend += num.pop()
            
            if max_no1 == num[-1]:
                me += num.pop()
                max_no2 = max(num[0], num[-1])
                if max_no2 == num[0]:
                    friend += num.pop(0)
                elif max_no2 == num[-1]:
                    friend += num.pop()
        me += max(num)
        friend += min(num)
    return me, friend      

# num = [3,4,8,2,5]
num = [7,7,6,5,8,7,7]
print(solution(num))
'''

# 네트워크



# def solution(n,com):
#     visited = [False]*n
#     node = []
#     ans = 0
#     while False in visited:
#         no = visited.index(False)
#         node.append(no)
#         visited[no] = True
#         while node:
#             current = node.pop(0)
#             for i in range(n):
#                 if com[current][i] == 1 and visited[i] == False:
#                     visited[current] = True
#                     node.append(i)
#         ans += 1
#     return ans
# n = 3
# com = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# print(solution(n,com))

# 백준 - 촌수계산
# n = 9
# a = [[1,2],[1,3],[2,7],[2,8],[2,9],[4,5],[4,6]]
# graph = [[0]*(n+1) for _ in range(n+1)]

# for i in a:
#     graph[i[0]][i[1]] = 1
#     graph[i[1]][i[0]] = 1

# def bfs(start):
#     visited = [True] + [False]*n
#     ans = 0
#     node = [start]
#     while node:
#         v = node.pop(0)
#         visited[v] = True
#         if v == 3:
#             break
#         for i in range(1,n+1):
#             if graph[v][i] == 1 and visited[i] == False:
#                 node.append(i)
#                 visited[i] == True
#                 ans += 1
#     return ans
# print(bfs(7))


# 숨바꼭질

# end = 17
# s = 5

# [s,end] = list(map(int,input().split(' ')))
# def solution(s, end):
#     ans = 1
#     arr = [s-1, s+1, s*2]
#     if end in arr:
#         return ans
#     while True:
#         node = []
#         ans += 1

#         for i in arr:
#             node.append(i-1)
#             node.append(i+1)
#             node.append(i*2)
#             if end in node:
#                 return ans
#         arr = node.copy()

# print(solution(s,end))








