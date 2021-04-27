def sum1(a, b):
    result = a + b
    return result


def sum2(a, b):
    print("sum2 %d, %d의 합은 %d입니다." % (a, b, a + b))


def say1():
    return 'Hi'


def say2():
    print('say2 hi')


a = sum1(3, 4)
print("sum1", a)
sum2(1, 2)

a = say1()
print("say1", a)
say2()


# 변수명 앞에 *을 붙이면 입력값들을 전부 모아서 튜플로 만듬
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


result = sum_many(1, 2, 3)
print("sum_many ", result)


def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


result = sum_mul('sum', 1, 2, 3, 4, 5)
print("sum_mul sum", result)
result = sum_mul("mul", 1, 2, 3, 4, 5)
print("sum_mul mul", result)


def sum_and_mul(a, b):
    return a + b, a * b


result = sum_and_mul(3, 4)
print("sum_and_mul", result)
sum, mul = sum_and_mul(3, 4)
print("sum", sum, " mul", mul)
