# ctrl+alt+l 자동 정렬
# ctrl+shift_f10 현재파일 실행

# if 문
money = 2
if money:
    print("money =", money)
else:
    print("money = 0")

a = [1, 2, 3]
if 1 in a:
    print("{0:=^15}".format("List"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 15
    print("i in", a, "=", 1 in a)
    print("a.index(1)=", a.index(1))
else:
    print("{0:=^15}".format("List"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 15
    print("1 in", a, "=", 1 in a)
    print("a.index(1)=", a.index(1))

b = (4, 5, 6)
if 5 in b:
    print("{0:=^15}".format("Tuple"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 15
    print("5 in", b, "=", 5 in b)
    print("b.index(5)=", b.index(5))
else:
    print("{0:=^15}".format("Tuple"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 15
    print("5 in", b, "=", 5 in b)
    print("b.index(5)=", b.index(5))

c = {7: 7, 8: 8}
if 8 in c:
    print("{0:=^15}".format("Dictionary"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 15
    print("8 in", c, "=", 8 in c)
    print("c.keys()=", c.keys())
    print("c.values()=", c.values())
    print("c.get(8) == c[8]", c.get(8) is c[8])
else:
    print("{0:=^15}".format("Dictionary"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 15
    print("8 in", c, "=", 8 in c)
    print("c.keys()=", c.keys())
    print("c.values()=", c.values())
    print("c.get(8) == c[8]", c.get(8) is c[8])

d = "abcd"
if 'a' in d:
    print("{0:=^15}".format("String"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 15
    print("a in", d, "=", "a" in d)
    print("d.index('a')=", d.index('a'))
else:
    print("{0:=^15}".format("String"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 15
    print("a in", d, "=", "a" in d)
    print("d.index('a')=", d.index('a'))

