# 숨바꼭질

#내가 작성한 코드는 수가 커지면 느려져서 pass 안되는듯ㅜㅜ

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


from collections import deque

n = 5
k = 17
graph = [-1] * 101
dq = [1, -1, 2]

def bfs(start):
    queue = deque()
    queue.append(start)
    graph[start] = 0
    
    while queue:
        q = queue.popleft()
        
        for i in dq:
            nq = q * 2 if i == 2 else q + i
            if 0 <= nq <= 100 and graph[nq] == -1:
                queue.append(nq)
                graph[nq] = graph[q] + 1
            if nq == k:
                return graph[nq]

print(bfs(n))
