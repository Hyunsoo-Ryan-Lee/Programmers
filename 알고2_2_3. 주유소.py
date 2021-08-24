# 백준 주유소
'''
1. 첫번째 도시에서 무조건 주유를 하고 최소가격을 갱신
2. 앞에 가격보다 더 낮으면 최소가격 갱신 후 남은 거리 곱해서 더함
3. 다음 도시 도착할때마다 앞에 가격이랑 비교하면서 더 낮으면 2번 반복, 높으면 기존 가격*거리 해서 더함
'''

length = [3,3,4]
city = [1,1,1,1]


gas = [city[0]]
start = length[0]*city[0]

for i in range(1,len(city[1:])):
    if city[i] < gas[0]:
        gas.pop()
        gas.append(city[i])
        start += gas[0]*length[i]
    else:
        start += gas[0]*length[i]
print(start)

# 다른 더 간단한 풀이

n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
res = 0
m = cost[0]
for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    res += m*road[i]
print(res)