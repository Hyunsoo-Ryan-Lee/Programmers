from itertools import combinations


n = 6

a = list(range(1,n+1))
tot = list(combinations(a,int(n/2)))
fir = tot[:int(len(tot)/2)]
sec = tot[int(len(tot)/2):][::-1]
print(fir)
print(sec)
one = []
two = []

