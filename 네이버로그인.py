from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip # 클립보드를 사용하여 복사-붙여넣기를 간편하게 할 수 있는 모듈
chrome_path = 'C:\py_test08\chromedriver.exe' # 크롬 드라이버의 경로
url = 'https://www.naver.com/'
browser = webdriver.Chrome(chrome_path)
browser.get(url)
browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/div/div[2]/a').click()
pyperclip.copy("0109jhs")
browser.find_element_by_xpath('//*[@id="id"]').send_keys(Keys.CONTROL,'v')
