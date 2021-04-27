# ctrl+alt+l 자동 정렬
# ctrl+shift_f10 현재파일 실행

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        print("%d %% 2 = %d" % (a, a % 2))
        continue
    print(a)
