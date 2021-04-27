# alt + enter =임포트 단축키
import sys

a = 3
b = 3
print("배열 a 랑 b 비교", a is b)  # a,b 변수가 동일한 객체를 가르키는지
print(sys.getrefcount(3))  # 3이라는 정수형 객체를 참조하는 변수가 몇개 인지
# 반환값-35 == 기본-30개 a,b-2개 print(a is b)-2개  print(sys...)-1개

# 튜플 형태
a, b = ('python', 'life')
print("튜플 a " + a)
print("튜플 b " + b)
(a, b) = 'python', 'life'
print("튜플 (a) " + a)
print("튜플 (b) " + b)
# 배열
[a, b] = ['python', 'life']
print("배열 a " + a)
print("배열 b " + b)
# 선언
a = b = 'python'
print("a " + a)
print("b " + b)
# 값 변환
a = 3
b = 5
a, b = b, a
print("a 원래 3 ", a)
print("b 원래 5 ", b)
# 변수 삭제
del (a)
del (b)
# 배열 변수 요소값 복사
a = [1, 2, 3]
b = a
a[1] = 4
print("배열 a ", a)
print("b 배열 a 복사 ", b)
# b 변수에 a 변수의 값을 복사하면서 다른 리스트를 가르키게 함
a = [4, 5, 6]
b = a[:]
a[1] = 7
print("배열 a 값 변경 ", a)
print("b 배열 a 값 변경전 복사 ", b)
# b = a[:] 다른 방법 동일 값
a = [7, 8, 9]
from copy import copy
b = copy(a)
print(b is a)