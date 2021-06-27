# <<로또의 최고순위와 최저순위>>

def solution(lotto,win):
     a = lotto.count(0)
     b = list(filter(lambda x:x>0,lotto))
     ans = 0
     for i in range(len(b)):
          if b[i] in win:
               ans += 1
     good = a+ans
     bad = ans
     rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
     final = [rank[good],rank[bad]]

     return final

lottos = [44, 1, 0, 0, 31, 25]
wins = 	[31, 10, 45, 1, 6, 19]
print(solution(lottos,wins))