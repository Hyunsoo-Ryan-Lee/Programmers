# 진법 변환 

numb = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = list(input('number & 진법 : ' ).split(' '))
a = list(str(n[0]))
a.reverse()
b = [numb.index(i) for i in a] #[12, 11, 10] ,30진법
ans = b[0]
for j in range(1,len(b)):
    ans += b[j]*(int(n[1])**j)

print(ans)