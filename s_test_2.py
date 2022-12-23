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
