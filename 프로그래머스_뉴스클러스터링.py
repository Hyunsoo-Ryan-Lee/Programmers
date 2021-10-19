    # word1 = ''.join(filter(str.isalnum,str1)).lower()
    # word2 = ''.join(filter(str.isalnum,str2)).lower()
    # if set(word1) == set(word2):
    #     return int(65536)
'''
https://programmers.co.kr/learn/courses/30/lessons/17677
'''
def solution(str1, str2):
    word1 = []
    word2 = []
    for i in range(1,len(str1)):
        letter = str1[i-1:i+1]
        if letter.isalpha():
            word1.append(letter.lower())

    for i in range(1,len(str2)):
        letter = str2[i-1:i+1]
        if letter.isalpha():
            word2.append(letter.lower())
    word1.sort()
    word2.sort()
    if word1 == word2:
        return int(65536)
    tot = list(set(word1+word2))
    union = []
    minus = []
    for j in tot:
        union.extend([j]*int(max(word1.count(j), word2.count(j))))
        if j in word1 and j in word2:
            minus.extend([j]*int(min(word1.count(j), word2.count(j))))
    return int(65536*(len(minus)/len(union)))
    

s1 = 'aa1+aa2'
s2 = 'AAAA12'
print(solution(s1,s2))