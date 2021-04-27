# 딕셔너리는 key, value 형태로 구분된 자료형이다
# key는 고유한 값이어야 된다. 배열은 key가 될수 없지만 튜플은 가능하다
a = {1: 'hi'}
b = {'a': [1, 2, 3]}  # Value 값에 배열 넣을 수 있음
print(a)
print(b)
a[2] = 'b'  # a 딕셔너리에 key, value 추가
print(a)
del a[1]  # a 딕셔너리에서 key가 1인 요소 삭제
print(a)
grade = {'pey': 10, 'julliet': 99, 3: 'c'}
print(grade['pey'])  # grade 딕셔너리에서 key가 pey인 value 반환
print(grade[3])  # grade 딕셔너리에서 key가 3인 value 반환

# 딕셔너리 관련 함수
print(grade.keys())  # grade 딕셔너리에 있는 key 만 모아서 반환
print(list(grade.keys()))  # grade 딕셔너리에 있는 key 만 모아서 반환하고 배열로 변환
print(grade.values())  # grade 딕셔너리에 있는 value 만 모아서 반환
print(list(grade.values()))  # grade 딕셔너리에 있는 value 만 모아서 반환하고 배열로 변환
print(grade.items())  # grade 딕셔너리에 있는 key, value값을 반환
print(grade.get('pey'))  # grade 딕셔너리에서 key가 pey인 value 반환, grade['pey'] 동일
print(grade.get('4', 'd'))  # grade 딕셔너리에서 key가 4인 value를 반환하지만 해당 key가 없으면 d 반환
print('pey' in grade)  # pey라는 key를 grade 딕셔너리에서 가지고 있는지를 반환
grade.clear()  # grade 딕셔너리에 있는 key, value값을 모두 삭제
print(grade)
