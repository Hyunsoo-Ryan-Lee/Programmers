# 백준 15829번

word = "abcdefghijklmnopqrstuvwxyz"

a,b = input().split(" ")
a = int(a)
# a = 3
# b = "zzz"
ans = 0
for i in range(a):
    ans += (word.index(b[i])+1)*(31**i)

print(ans)

# print(type(a), type(b))

