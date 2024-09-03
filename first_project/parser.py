import re
import requests
from bs4 import BeautifulSoup

# 가져오고자 하는 웹페이지의 URL
url = 'http://sunsa.gangdong.go.kr/site/main/home'

# URL에 GET 요청을 보내서 응답을 받음
response = requests.get(url)

# 응답으로 받은 HTML 내용을 BeautifulSoup으로 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# HTML 문서에서 텍스트만 추출
text_content = soup.get_text()
parts = text_content.split('\n')  # 줄바꿈을 기준으로 나눔
for i in parts:
    parts = i.split(' ')  # 줄바꿈을 기준으로 나눔
    for j in parts:
        parts = j.split('\n')
        # print(i)
print(len(parts))
