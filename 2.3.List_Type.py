# ctrl+alt+l로 자동정렬
from typing import List, Union

odd = [1, 3, 5, 7, 9]
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
# f = [1, 2, ['a', 'b'['Life', 'is']]]
g = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

# 리스트 인덱싱
print(b[0])  # 1
print(b[0] + b[2])  # 4
print(b[-1])  # 3
print(e[0])  # 1
print(e[-1])  # ['Life', 'is']
print(e[2])  # ['Life', 'is']
print(e[-1][0])  # 'Life'
print(e[2][1])  # 'is'
# print(f[2][2][0])  # 'Life'

# 리스트의 슬라이싱
print(odd[0:2])  # 1,3,5
print(odd[:2])  # 1,3
print(odd[2:])  # 5,7,9
print(g[2:5])  # [3,['a', 'b'],4]
print(g[3][:2])  # ['a', 'b']

# 리스트 연산자
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # [1,2,3,4,5,6,]
print(a * 3)  # [1,2,3,1,2,3,1,2,3]
print(str(a[2]) + "hi")  # 3hi 문자열을 더하려고 하면 숫자를 문자열로 바꿔야됨
a[2] = 4  # [1, 2, 4] 배열 요소 값 수정
print(a)
a[1:2] = ['a', 'b', 'c']  # [1, 'a', 'b', 'c', 4] 배열에서 연속된 범위의 값 수정
print(a)
a[1:3] = []  # [1, 'c', 4] 배열에서 연속된 값 삭제
print(a)
del a[1]  # [1, 4] 배열에서 요소 값 삭제
print(a)
a.append(5)  # 배열의 마지막에 5를 추가
print(a)
a.append([6, 7])  # 배열의 마지막에 배열을 추가
print(a)
c = [1, 3, 2, 7, 4]
c.sort()  # 숫자 배열 정렬
print(c)
d = ['b', 'a', 'd', 'c']
d.sort()  # 문자 배열 정렬
print(d)
c.reverse()  # 배열을 역순으로 뒤집음
print(c)
print(a.index(4))  # 숫자 4가 있는 위치 반환
a.insert(1, 2)  # a배열 1번째 위치에 2을 삽입
print(a)
a.remove(5)  # a 배열에서 맨처음 나오는 5 삭제
print(a)
print(a.pop())  # a 배열에서 맨 마지막 요소를 반환하고 삭제
print(a)
print(a.pop(2))  # a 배열에서 2번째 요소를 반환하고 삭제
print(a)
print(a.count(1))  # a 배열에서 1의 개수 반환
a.extend([3, 4])  # a 배열에 [3,4] 추가 extend는 배열만 가능
print(a)
a.extend(b)  # a 배열에 b 배열 추가
print(a)
