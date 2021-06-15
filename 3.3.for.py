a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print("%d+%d = %d" % (first, last, first + last))

print("-"*12)
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print("-"*12)
test_tuple = ('a', 'b', 'c')
for a in test_tuple:
    print(a)

print("-"*12)
test_string = "abcde"
for i in test_string:
    print(i)

print("-"*12)
sum = 0
for i in range(1, 11):  # range(시작 숫자, 끝 숫자)
    print("%d+%d=%d" % (sum, i, sum + i))
    sum += i

print("-"*12)
b = [1, 2, 3, 4]
result = [num * 3 for num in b]  # [표현식 for 항목 in 반복 가능 객체]
print(result)
result = [num * 3 for num in b if num % 2 == 0]  # [표현식 for 항목 in 반복 가능 객체 if 조건]
print(result)
