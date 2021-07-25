# 백준 계단오르기



s = [10,20,15,25,10,20]
s.reverse() # [20, 10, 25, 15, 20, 10]  
ans = [0,s[0]]
for i in range(1, len(s)): 
    ans.append(max(ans[i], ans[i-1]+s[i], ans[i-1]+s[i-1]))
print(ans)

