import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
# BeautifulSoup(<받은 텍스트>, <텍스트를 파싱할 파서>)
# 첫번째 값에는 웹에서 받은 텍스트임
# 두번째 값은 데이터를 뽑아내는(파싱) 프로그램인 "html.paeser" 임

top_right = bs_obj.find("div", {"class": "service_area"})
# .find() 명령어는 <div> 태그 중에 class가 service_area인 중에 첫번째로 나오는 div 태그를 찾으라는 명령 임
print("1", top_right)

first_a = top_right.find("a")
# 첫번째로 나오는 a태그

print(first_a.text)
