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