# 모듈
# 함수나 변수 또는 클래스를 모아 놓은 파일
# 다른 파이썬 프로그램을 불러와 사용 할수 있게 만들어진 파이썬 파일이라고 할 수 있음

# mod1.py 로 만들고 저장
def sum_1(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다")
        return
    else:
        return sum(a, b)


# C:\python>python으로 대화형 인터프리터 실행
# import mod1
# print(mond1.sum_1(3,4))
# 하면 7이 반환됨

# from mod1 import sum_1,safe_sum
# safe_sum(3,4)
# 하면 7이 반환됨


if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum_1(10, 10.4))

# C:\python>python mod1.py 했을 경우에만
# print 실행됨
# 다른 파일이나,대화형 인터프리터에서는 실행 안됨


# mod2.py 로 만들고 저장
PI = 3.141592


class Math:
    def solv(self, r):
        return PI * (r ** 2)  # r**2는 r 을 의미함


def sum_2(a, b):
    return a + b


if __name__ == "__main__":
    print(PI)
    a = Math()  # Math 클래스 안의 함수를 사용하기 위해
    print(a.solv(2))
    print(sum_2(PI, 4.4))

# 새 파일 안에서 이전에 만들 모듈 불러오기
# modest.py 파일과 mod2.py 파일이 동일한 디렉터리에 있어야 함
# modest.py
# import mod2
# result = mod2.sum(3, 4)
# print(result)

