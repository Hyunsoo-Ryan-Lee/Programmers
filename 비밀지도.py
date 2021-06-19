# <<비밀지도>>

def solution(n,arr1,arr2):
     b1 = []
     b2 = []
     b3 = []
     ans = []
     for i in arr1:
          b1.append(bin(i)[2:].zfill(n))
     for j in arr2:
          b2.append(bin(j)[2:].zfill(n))
     for k in range(n):
          b3.append(str(int(b1[k]) + int(b2[k])).zfill(n))
     
     for a in range(n):
          p=''
          for b in range(n):
               if b3[a][b] != '0':
                    p += '#'
               else:
                    p += ' '
          ans.append(p)

     return ans
n = 6
arr =[46, 33, 33 ,22, 31, 50]
brr =[27 ,56, 19, 14, 14, 10]
print(solution(n,arr,brr))