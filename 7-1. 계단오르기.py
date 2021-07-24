# 백준 계단오르기



s = [6,10,20,15,25,10,20]
s.reverse() # [20, 10, 25, 15, 20, 10, 6]  
ans = [20]
for i in range(1, len(s)-1):
    ans.append(max(ans[i], ans[i-1]+s[i]))
print(ans)

