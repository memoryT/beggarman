import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import json
# 有cookie之後即可用以下登錄
url_shopee = "https://shopee.tw/"
driver = webdriver.Firefox()
driver.get(url_shopee)
time.sleep(3)
with open("shopee.json", "r") as f:
    data = json.loads(f.read())
for c in data:
    driver.add_cookie(c)  #將cookie載入
driver.refresh() #重新整理
free_url = "https://shopee.tw/m/free-shipping"
driver.get(free_url)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div/div[3]/div/div[1]/div/div[1]/div").click()

#嘗試點擊優惠券專區結果報錯，無法點擊後出現免運券領取
