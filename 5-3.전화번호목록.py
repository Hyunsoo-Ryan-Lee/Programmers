#전화번호 목록

# a = ["123","1235","567","88"]
# a.remove("123")
# a.sort(key=len)

import re
#  정규표현식 써서 ~~로 시작되는 숫자 판별문 작성
def aaa(p):
    p.sort(key=len)
    for i in p:
        p.remove(i)
        for j in p:
            if i in j:
                return "false"
    return "true"
        
        
a =["1234", "1235", "567"]
print(aaa(a))