# ctrl+alt+l로 자동정렬
odd = [1, 3, 5, 7, 9]
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
f = [1, 2, ['a', 'b'['Life', 'is']]]

# 리스트 인덱싱
print(b[0])  # 1
print(b[0] + b[2])  # 4
print(b[-1])  # 3
print(e[0])  # 1
print(e[-1])  # ['Life', 'is']
print(e[2])  # ['Life', 'is']
print(e[-1][0])  # 'Life'
print(e[2][1])  # 'is'
print(f[2][2][0])  # 'Life'

# 리스트의 슬라이싱
print(odd[0:2])  # 1,3,5
print(odd[:2])  # 1,3
print(odd[2:])  # 5,7,9
print(f[1:3])  # 1,3,5
print(f[2][2])  #
