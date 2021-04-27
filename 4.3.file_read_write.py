# 파일 객체 = open(파일 이름, 파일 열기 모드) r,w,a(읽고 쓰고 추가)

# 읽기 전체1
f = open("C:\python_study\새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 읽기 전체2
f = open("C:\python_study\새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print("lines", line)
f.close()

# 읽기 전체3
f = open("C:\python_study\새파일.txt", 'r')
data = f.read()
print("data", data)
f.close()

# 쓰기
f = open("C:\python_study\새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 추가
f = open("C:\python_study\새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# whth문 사용시 자동 close
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

with open("foo.txt", "r") as f:
    print(f.read())

with open("foo.txt", "a") as f:
    f.write("end")