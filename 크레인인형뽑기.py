# <<크레인 인형뽑기>>

# [0,0,0,0,0]
# [0,0,1,0,3]
# [0,2,5,0,1]
# [4,2,4,4,2]
# [3,5,1,3,1]      moves = [1,5,3,5,1,2,1,4]	

def solution(board,moves):
    stack = [0]
    ans = 0
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                stack.append(b[m-1])
                b[m-1] = 0
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    ans += 2
                break
    return ans

a = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
b = [1,5,3,5,1,2,1,4]
print(solution(a,b))