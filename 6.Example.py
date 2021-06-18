# 구구단
import os
import sys


def GuGu(n):
    result_1 = []
    i = 1
    while i < 10:
        result_1.append(n * i)
        i = i + 1
    return result_1


# 3과 5의 배수 더하기
result_2 = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result_2 += n
print(result_2)


# 페이징
def getTotalPage(m, n):
    if m % n == 0:
        return m // n  # 소수점 아래수를 버리기 위해 // 사용
    else:
        return m // n + 1


# 메모장 만들기
# python memo.py –a “Life is too short” 실행시
# sys.argv[0] 은 memo.py 여서 필요없음
option = sys.argv[1]  # 옵션 저장

if option == '-a':  # 쓰기
    memo = sys.argv[2]  # 메모 저장
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':  # 읽기
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)

# 탭을 4개의 공백으로 변환
src = sys.argv[1]  # 변환 전 파일
dst = sys.argv[2]  # 변환 후 파일

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()


# 하위 디렉터리 검색
def search(dirname):
    try:
        filenames = os.listdir(dirname)  # 경로를 포함한 검색을 위해 dirname도 받음
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)  # 디렉터리를 포함란 전체 경로를 받을 수 있게함
            if os.path.isdir(full_filename):  # 디렉터리인지 파일인지 확인 / 하위 파일까지 찾아야되서
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]  # 파일의 확장자 명
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass


search("C: / ")