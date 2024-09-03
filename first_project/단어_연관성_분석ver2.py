import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import pyautogui

# 크롬 드라이버 초기화
driver = webdriver.Chrome()
cultures = ["문화회관", "도서관", "박물관", "기타", "공원장", "미술관", "문화원"]

# 데이터 읽기
data = pd.read_csv('filtered_data_강동.csv', encoding='utf-8')
urls = data['홈페이지']
position = data['문화시설명']

# gangnam 카테고리 초기화
gangnam = {"문화회관": 0, "도서관": 0, "박물관": 0, "기타": 0, "공원장": 0, "미술관": 0, "문화원": 0}

# CSV 파일에 헤더(컬럼 이름) 기록
with open('count_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 헤더 작성 (문화시설명 + gangnam의 키 값들)
    header = ['문화시설명'] + list(gangnam.keys())
    writer.writerow(header)

# 각 홈페이지를 순회하며 텍스트 분석
for homepage, facility_name in zip(urls, position):
    gangdong = {"전시회": 0, "음악 및 무용발표회": 0, "박물관": 0, "전통예술공연": 0, "연극공연": 0, "": 0, "문화원": 0}
    try:
        # 셀레니움으로 페이지 요청 및 로드
        driver.get(homepage)
        WebDriverWait(driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete")
        try:
            close_button = driver.find_element(By.XPATH, '//*[text()="닫기"]')
            for i in len(close_button):
                time.sleep(0.2)
                close_button.click()
        except:
            print('닫기 버튼 없음')

        # 페이지의 body 태그에서 모든 텍스트 가져오기
        body_text = driver.find_element(By.TAG_NAME, 'body').text

        # 텍스트를 줄 단위로 분리
        body_list = body_text.split('\n')
        body_set = set(body_list)
    except Exception as e:
        print(e)
    try:
        # body_list에서 각 줄을 확인하며 카테고리 찾기
        for body in body_list:
            driver.get('https://aiopen.etri.re.kr/demo/WordRel')

            # time.sleep(1)
            # /html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/h4
            try:
                word1 = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/table/tbody/tr[1]/td/input')
            except:
                word1 = driver.find_element(By.ID, 'box3')
            # time.sleep(1)
            try:
                word2 = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/table/tbody/tr[2]/td/input')
            except:
                word2 = driver.find_element(By.ID, 'word2')
            # time.sleep(1)

            try:
                button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[3]/button')
            except:
                try:
                    button = driver.find_element(By.CLASS_NAME, 'btnBlue')
                except:
                    button = driver.find_element(By.CSS_SELECTOR, 'btnBlue')

            WebDriverWait(driver, 10).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete")
            # time.sleep(1)
            word2.click()
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('del')
            word2.send_keys(body)
            # time.sleep(1)
            # 각 장소의 홈페이지에 어떤 키워드가 있는지 분석
            for category in gangnam.keys():
                word1.click()
                time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('del')
                word1.send_keys(category)
                # if category in body:
                time.sleep(0.1)
                button.click()
                time.sleep(0.1)
                try:
                    value = float(
                        driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[5]/table[2]/tbody/tr/td[1]').text)
                except:
                    value = float(
                        driver.find_element(By.XPATH, '//*[@id="api_result_box_3"]/table[2]/tbody/tr/td[1]').text)
                time.sleep(0.1)
                if value > 0.5:
                    gangnam[category] += 1
                    print(gangnam[category])
                time.sleep(0.1)
    except Exception as e:
        print(e)

        # 데이터 CSV 파일에 기록하기
        with open('count_data_gandong.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # gangnam 값을 리스트로 변환하고 position과 결합
            row = [facility_name] + list(gangnam.values())
            writer.writerow(row)

# 결과 출력
print(gangnam)

# 크롬 드라이버 종료
driver.quit()
