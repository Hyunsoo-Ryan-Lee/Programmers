# 백준 계단오르기
# s = [0,10,20,15,25,10,20]

# n = int(input())
# s = [0]
# for i in range(n):
#     s.append(int(input()))
# s.reverse()
# ans = [0,s[0]]
# for i in range(1, len(s)): 
#     ans.append(max(ans[i], ans[i-1]+s[i], ans[i-1]+s[i-1]))
# print(ans[-1])

# 6
# 10
# 20
# 15
# 25
# 10
# 20

def solution(floor):
    
    answer = [] # 시작점 점수
    floor.reverse() # 마지막 도착 계단을 무조건 밟아야 하므로 뒤에서부터 내려오기
    answer.append(floor[0]) # 도착 지점의 계단값으로 sum의 최댓값 미리 넣어주기 
    
    answer.append(floor[0]+floor[1])
    answer.append(max(floor[0]+floor[2],floor[1]+floor[2]))
    
    print(answer)
    
    for i in range(3,len(floor)):
        answer.append(max(answer[i-2]+floor[i],answer[i-3]+floor[i-1]+floor[i]))
    print(answer)
    print(floor)
    return answer[-1]
    
print(solution([6,10,20,15,25,10,20])) # 76