from selenium import webdriver
from selenium.webdriver.common.by import By
import time # 페이지 로딩을 기다리는데에 사용할 모듈
chrome_path = 'C:\py_test08\chromedriver.exe' # 크롬 드라이버의 경로
url = 'https://codepen.io/' # 들어가고 싶은 url
id = '0109jhs@naver.com'
pw = 'zhfldkIT11!'
browser = webdriver.Chrome(chrome_path) # 크롬드라이버 실행
browser.get(url) # 크롬 드라이버에 url 주소 넣고 실행
time.sleep(3) # 페이지가 완전히 로딩되도록 3초동안 기다림
# browser.find_element_by_xpath('//*[@id="react-page"]/div[1]/a[2]').click()
browser.find_element(By.XPATH, '//*[@id="react-page"]/div[1]/a[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="login-email-field"]').send_keys(id)
browser.find_element(By.XPATH, '//*[@id="login-password-field"]').send_keys(pw)
browser.find_element(By.XPATH, '//*[@id="log-in-button"]').click()