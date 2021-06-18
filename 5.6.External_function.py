import random
import sys
import time
import calendar
import webbrowser

# sys 파이썬 인터프리터가 제공하는 변수들과 함수들을 직접 제어
print(sys.argv)  # 명령 행에서 인수 전달하기
sys.exit()  # 강제로 스크립트 종료
print(sys.path)  # 파이썬 모듈들이 저장되어 있는 위치 반환
sys.path.append("C:/python'")  # 경로명 추가

# OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어
print(os.environ)  # 시스템의 환경 변수 값 반환
print(os.environ['PATH'])  # 시스템의 PATH 환경 변수 반환
print(os.chdir("C:\window"))  # 디렉터리 위치 변경
print(os.getcwd)  # 현재 디렉터리 위치 리턴
print(os.system("dir"))  # 현재 디렉터리에서 시스템 명령어인 dir을 실행
f = os.popen("dir")  # 시스템 명령어를 실행시킨 결과값을 읽기 모드 형태의 파일 객체 반환
print(f.read)  # 읽어 들인 파일 객체의 내용을 보기

# shutil.copy(src, dst) src라는 이름의 파일을 dst로 복사함

# glob 특정 디렉터리에 있는 파일 이름을 모두 알아야 할 때 사용
print(glob.glob("C:/python/q*"))  # C:\python이라는 디렉터리에 있는 파일 중 이름이 문자 q로 시작하는 파일들을 모두 찾음

# time.time()은 UTC(Universal Time Coordinated, 협정 세계 표준시)를 이용하여 현재 시간을 실수 형태로 리턴하는 함수임
print("---time---")
print(time.time())  # 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴 함
print(time.localtime(time.time()))  # 연도, 월, 일, 시, 분, 초, ···의 형태로 바꾸어 주는 함수임
print(time.asctime(time.localtime(time.time())))  # 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수
print(time.ctime())  # ctime은 항상 현재 시간만을 리턴
# time.sleep(1) 1초 간격 java 에서 thread.sleep(1)

# calender 달력
print("---calender---")
print(calendar.calendar(2015))  # 2015년도 전체 달력
print(calendar.prmonth(2015, 12))  # 2015년 12월 달력
print(calendar.weekday(2015, 12, 31))  # 2015년 12월 31일 요일 반환(월:0 일:6)
print(calendar.monthrange(2015,12))  # 2015년 12월 1일 요일과 12월이 몇일까지 있는지 반환

# random 랜덤
print("---random---")
print(random.random())  # 0.0부터 1.0까지의 실수 난수값 반환
print(random.randint(1, 10))  # 1부터 10까지의 난수값
data = [1, 2, 3, 4, 5]
random.shuffle(data)  # data 리스트 요소값을 무작위로 섞음
print(data)

# webbrowser
webbrowser.open("http://google.com")  # 웹 브라우저를 자동으로 실행시키고 해당 URL인 http://google.com으로 가게 해줌
webbrowser.open_new("http://google.co")  # open_new 함수는 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리도록 함