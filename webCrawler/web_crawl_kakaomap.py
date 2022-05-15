from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import time

chromedriver = '/home/kimdj/Downloads/chromedriver_linux64/chromedriver' #chromedriver(String): chromedriver 위치지정

# ---------------- id_list data 불러오기 ----------------
import csv
id_lists = []
f = open('kakao_id_data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    id_lists.append(line[0])
f.close()
# ---------------- id_list data 불러오기 ----------------
f = open('review_data.csv', 'w', encoding='utf-8', newline='') # data를 작성할 file open
for id in id_lists:

    url = f'https://place.map.kakao.com/{id}#review'
    options = webdriver.ChromeOptions()
    options.add_argument('headless')       # 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
    options.add_argument('disable-gpu')    # GPU 사용 안함
    options.add_argument('lang=ko_KR')     # 언어 설정
    driver = webdriver.Chrome(chromedriver, options=options)
    driver.get(url)

    try:    # 정상 처리
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'txt_comment'))
        )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
        review_datas = driver.find_elements_by_class_name('txt_comment')
        title_data = driver.find_elements_by_class_name('tit_location')
        for review_data in review_datas:
            wr = csv.writer(f)
            if len(review_data.text) >= 10:
                wr.writerow([title_data[0].text, review_data.text])
        print('해당 페이지에 리뷰 정보를 성공적으로 불러왔습니다.')
    except TimeoutException:    # 예외 처리
        print('해당 페이지에 리뷰 정보가 존재하지 않습니다.')

    finally:
        driver.close()          # 종료

f.close() # data를 작성할 file close

# 783995964


