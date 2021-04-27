# 자료형의 참과 거짓 ??????
a = [1, 2, 3, 4]
while a:
    print(a.pop())
a = [1]
if a:  # 배열이 비워있으면 false
    print("배열 a =", a, "if []: ", not not a, "로 이동")
else:
    print("배열 a =", a, "if []: ", not not a, "로 이동")

if [1, 2, 3]:  # a 배열에 1,2,3이 있으면 true
    print("True")
else:
    print("False")
