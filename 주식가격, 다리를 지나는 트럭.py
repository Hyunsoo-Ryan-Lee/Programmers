# 1. 주식 가격
'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
'''
from abc import abstractproperty


p2 = [1, 2, 3, 2, 3]	
p1 = [6,4,3,7,8,9,7]
a2 = [1,1,4,3,2,1,0]

def solution(p1):
    ans = [0]*len(p1) # 수를 담을 list 만들기
    for i in range(len(p1)): 
        for j in range(i+1,len(p1)): # 위의 i와 i 다음 index인 j들을 비교
            if p1[i] <= p1[j]: # 가격이 내리지 않았다면!
                ans[i] += 1 # 앞에서 만든 ans의 i번재 index에 1을 더함
                # 남은 뒤의 수도 비교하여 가격이 내리지 않았다면 계속 1을 더함
            else: # 가격이 내렸다면 해당 가격은 1초 동안만 유지된다.
                ans[i] += 1 # 가격이 내린 항의 index에 1을 넣는다.
                break 
    return ans


from collections import deque
# deque : 양끝의 어느 쪽에서든 데이터의 출입이 가능한 데이터 행렬


def solution(p):
    ans = []
    while p:
        count = 0
        cut = p.pop(0)
        for i in range(len(p)):
            while len(p) != 0 and cut <= p[i]:
                count += 1
                break
            if cut > p[i]:
                count += 1
                break
        ans.append(count)
    return ans

p = [1,2,4,3,5,3,7,8,6]
#[8,7,1,5,1,3,2,1,0]
print(solution(p))


#2. 다리를 지나는 트럭
'''
def solution(bl,w,tw):

    bridge = [0]*bl # [0,0]
    time = 0
    while bridge:
        bridge.pop(0)
        time += 1 
        if tw:
            if sum(bridge) + tw[0] <= w:
                bridge.append(tw.pop(0))
            else:
                bridge.append(0)
    return time


from collections import deque

def solution(bl,w,tw):
    tw = deque(tw)
    bridge = deque([0]*bl) # [0,0]
    time = 0
    while bridge:
        bridge.popleft()
        time += 1
        if tw:
            if sum(bridge) + tw[0] <= w:
                bridge.append(tw.popleft())
            else:
                bridge.append(0)
    return time



x = 2
y = 10
z = [7,4,5,6]
print(solution(x,y,z))
'''



def solution(bridge_length, weight, truck_weights):
    now = [0]*bridge_length
    count = 0
    while now:
        now.pop(0) # <<<< 이게 중요한 팁!!!
        count += 1
        if truck_weights: 
            if sum(now)+truck_weights[0] <= weight:
                now.append(truck_weights.pop(0))
            else:
                now.append(0)
    return count

x = 2
y = 10
z = [7,4,5,6]
print(solution(x,y,z))



