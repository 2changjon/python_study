# input은 문자열만 받기 때문에 int()로 정수변환 시킴
a = int(input("첫번째 숫자를 입력 하세요 :"))
b = int(input("두번째 숫자를 입력 하세요 :"))

result = a + b
print(a, "+", b, "=", result)
result = a - b
print(a, "-", b, "=", result)
result = a * b
print(a, "*", b, "=", result)
result = a / b
print(a, "/", b, "=", result)
