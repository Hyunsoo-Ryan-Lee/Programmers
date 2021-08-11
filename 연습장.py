# def sol(n,d):
#     ans = []
#     d.sort() 
#     for i in range(len(n)):
#         for j in range(len(d)):
#             if int(n[i]) == len(d[j]):
#                 ans.append(d[j])
#                 d.pop(j)
#                 d.append('')
#                 break
#     return ans


# n = "2222"
# d = ["ab","cd","ef","a","b","ab"]
# print(sol(n,d))


# def sol(s):
#     ans = []
#     rev = []
#     for i in range(len(s)+1):
#         ans.append(s.zfill(i+len(s)))
#         rev.append(s.zfill(i+len(s))[::-1])
    
    
#     arr =[]
#     arr2 = []
#     for j in range(len(ans)):
#         cnt = 0
#         for p in range(len(ans[j])):
#             if ans[j][p] == rev[j][p]:
#                 cnt += 1
#         arr.append(cnt)
#         arr2.append(len(ans[j])-cnt)
    


#     return ans, rev, arr, arr2

# s = "qwerty"
# print(sol(s))

# # a = ['abab', '0abab', '00abab', '000abab', '0000abab']
# # print(a[1][0])
a = [1,2,3,4,5,6,7]


# b = 0
# while b<2:
#     a.append(a.pop(0))
#     b += 1

print(a.pop(2))