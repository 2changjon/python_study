# 집합 자료형
# 집합 자료형 생성
s1 = set([1, 2, 3])
s2 = set("Hello")
print(s1)
print(s2)

# 집합은 중복을 허용하지 않고 순서가 없음
# 집합은 인덱싱으로 값을 얻을 수 없어 리스트나 튜플로 변환 후 인덱싱 해야됨
l1 = list(s1)
print(l1[1])
t1 = tuple(s2)
print(t1[1])

# 집합 자료형 활용
s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])
print(s3 & s4)  # 교집합
print(s3.intersection(s4))  # s3 & s4 랑 동일
print(s3 | s4)  # 합집합
print(s3.union(s4))  # s3 | s4 랑 동일
print(s3 - s4)  # 차집합 1
print(s4 - s3)  # 차집합 2
print(s3.difference(s4))  # s3-s4 랑 동일
print(s4.difference(s3))  # s4-s3 랑 동일

# 집합 자료형 관련 함수들
s1.add(5)  # s1 집합에 값을 추가
print(s1)
s1.update([6, 4])  # s1 집합에 여러 값을 추가
print(s1)
s1.remove(6)  # s1 집합에서 특정된 값 6 제거
print(s1)
