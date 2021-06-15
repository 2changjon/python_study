# try:
# except[발생오류[as 오류메시지 변수]]:
# []는 괄효 안의 내용 생략 가능

try:
    # 무언가를 수행함
    print()  # 내용이 없으면 오류 발생
except:
    print('a')

try:
    4/0
except ZeroDivisionError:
    print('a')

try:
    f = open("나없는파일", 'r')
except FileNotFoundError as e:
    print(str(e))
else:
     data = f.read()
     f.close()

# else절은 예외가 발생하지 않은 경우에 실행되며 반드시 except절 바로 다음에 위치해야 함

f = open("나없는파일", 'w')
try:
    # 무언가를 수행함
    print()  # 내용이 없으면 오류 발생
finally:
     f.close()
# finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행됨

try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
     pass # 파일이 없더라도 오류를 발생시키지 않고 통과함

f.close()


class Bird:
    def fly(self):
        raise NotImplementedError # NotImplementedError 오류 강제로 발생
        # print("very fast")


class Eagle(Bird): # Eagle 클래스는 Bird 클래스를 상속 받음
    pass

eagle = Eagle()
eagle.fly()
# Eagle.fly()
