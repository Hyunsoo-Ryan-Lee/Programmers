#전화번호 목록

# a = ["123","1235","567","88"]
# a.remove("123")
# a.sort(key=len)


# def aaa(p):
#     p.sort(key=len)
#     for i in p:
#         p.remove(i)
#         for j in p:
#             if i in j:
#                 return "false"
#     return "true"
        
        
# a =["1234", "1235", "567"]
# print(aaa(a))

def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


