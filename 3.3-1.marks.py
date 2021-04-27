marks = [90, 25, 67, 45, 80]
number = 0
for i in marks:
    number += 1
    if i > 60:
        print("%d번 학생은 합격입니다" % (number))
    else:
        continue
        print("%d번 학생은 탈락입니다" % (number))
print("+" * 17)
print("{0:-^17}".format("new"))
print("+" * 17)
for num in range(len(marks)):  # len 함수는 리스트 내 요소의 개수를 돌려주는 함수
    if marks[num] < 60: continue
    print("%d번 학생은 합격입니다" % (num + 1))
