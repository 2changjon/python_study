# 튜플은 배열과는 다르게 값 변경이 안됨
t1 = ()
t2 = (1,)  # 1개의 요소를 가질때는 ,를 반드시 붙여야함
t3 = (1, 2, 3)
t4 = 1, 2, 3  # 괄호 생략해도 무방
t5 = ('a', 'b', ('ab', 'cd'))
# 값 변화가 없으면 튜플 있으면 리스트 // javascript const == 튜플

t1 = (1, 2, 'a', 'b')
print(t1[0])  # 문자열, 배열 처럼 인덱싱 가능
print(t1[1:])  # 문자열, 배열 처럼 슬라이싱 가능
print(t1 + t2)  # 더하기
print(t2 * 3)  # 곱하기