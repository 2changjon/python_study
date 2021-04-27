# 문자열 생성
a = "Hello World"
b = 'Python is fun'
c = """Life is too short, You need python"""
d = '''Life is too short, You need python'''

# 문자열에 ', " 포함시키기
food = "Python's favorite food is perl"
print("food=", food)
say = '"Python is very easy." he says.'
print("say=", say)
multiline = '''
    Life is too short
    You need python
'''
multiline2 = """
    Life is too short
    You need python
"""

# 출력
print(multiline)

# 문자열 연산
head = "Python"
tail = ' is fun! '
head + tail  # 문자열 연결
print("head + tail =", head + tail)
a * 2  # 문자열 반복
print("=" * 50)

# 문자열 인덱싱, 슬라이싱
a = "Life is too short, You need Python"
print(a[0] + "  " + a[-1])  # 'L  n' 처음과 마지막 값
print(a[0:5])  # 'Life' 0~4까지 a[4]는 공백이라서 자동 제거
print(a[5:])  # 'is too short, You need Python' 5~끝까지
print(a[:5])  # 'Life ' 5까지
print(a[:])  # 처음부터 끝까지

# 문자열 포매팅
print("I eat %d apples." % 3)  # 숫자
print("I eat %s apples." % "five")  # 문자열
number = 3
print("I eat %d apples." % number)  # 숫자변수
day = "three"
print("I ate %d%% apples. so I was sick for %s days." % (number, day))  # 2개 이상의 값 넣기

# 문자열 관련 함수
a = " hob by "
print(a.count('b'))  # 해당 문자 개수 반환
print(a.find('b'))  # 해당 문자 위치 반환, 문자나 문자열이 존재하지 않으면 -1반환
print(a.index('b'))  # 해당 문자 위치 반환, 문자나 문자열이 존재하지 않으면 오류발생
print(a.join('222'))  # 해당 문자열의 각각의 문자 사이에 변수 a의 값을 삽입
print(a.upper())  # 문자열 변수의 소문자를 대문자로 변환
print(a.lower())  # 문자열 변수의 대문자를 소문자로 변환
print(a.strip())  # 문자열 중 양쪽에 있는 한칸 이상의 연속된 공백 제거(r,l 있음)
print(a.replace("h", "o"))  # 문자열 내에서 특정한 값을 다른 값으로 치환
print(a.split())  # 공백을 기준으로 문자열을 나눔

# 고급 문자열 포맷팅
print("I ate {0} apples. So I was sick for {1} days.".format(number, day))  # 문자열 중 {0}은 number {1}은 day으로 변경됨
print("I ate {0} apples. So I was sick for {day} days".format(10, day=3))  # 문자열 중 {0}은 10 {day}은 3으로 변경됨
print("{0:<10}".format("hi"))  # 문자열은 좌측 문자열의 총 자리수는 10
print("{0:>10}".format("hi"))  # 문자열은 우측 문자열의 총 자리수는 10
print("{0:^10}".format("hi"))  # 문자열은 가운데 문자열의 총 자리수는 10
print("{0:=^10}".format("hi"))  # 문자열은 가운데 남은 공백에 "=" 문자열의 총 자리수는 10
y = 3.42134234
print("{0:0.4f}".format(float(y)))  # 소수점 4자리까지 표현
print("{0:10.4f}".format(float(y)))  # 소수점 4자리까지 표현 하는데 자릿수를 10으로
print("{{ and }}".format())  # 특수문자 { } 출력
