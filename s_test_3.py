import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


    # 有cookie之後即可用以下登錄
url_shopee = "https://shopee.tw/"
my_options = Options() #用my_options 儲存對於瀏覽器的設定
driver = webdriver.Firefox() #使用火狐瀏覽器 
driver.get(url_shopee)
time.sleep(3)
try:
    with open("shopee.json", "r") as f:
        data = json.loads(f.read())
    for c in data:
        driver.add_cookie(c)  #將cookie載入
    driver.refresh() #重新整理


except FileNotFoundError:
    print("請輸入帳號密碼")
    user_account = input("帳號:")
    user_password = input("密碼:")

    url = "https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F"

    driver.get(url) #進到蝦皮登錄頁面
    time.sleep(10) #等待(10秒)瀏覽器解析html資料（因為我的網路有點慢）
    driver.find_element(By.CSS_SELECTOR, "[name = loginKey]").send_keys(user_account)
    driver.find_element(By.CSS_SELECTOR, "[name = password]").send_keys(user_password)
    time.sleep(0.5)
    driver.find_elements(By.CSS_SELECTOR, "button")[2].click()
    print("請5分鐘內完成簡訊驗證登錄")
    time.sleep(300) #這段時間內(5分鐘)請盡快完成簡訊驗證登錄

    shopee_cookie = driver.get_cookies() #取出cookie
    with open("shopee.json", "w") as f:
        f.write(json.dumps(shopee_cookie)) #將cookie寫入shopee.json，檔案存在跟主程式同目錄


free_url = "https://shopee.tw/m/free-shipping"  #蝦皮免運頁面
driver.get(free_url)
time.sleep(5)
scroll_bar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div") #定位至滾動軸
for i in range(15):
    scroll_bar.send_keys(Keys.PAGE_DOWN)
    scroll_bar.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
buttons = driver.find_elements(By.XPATH, "//*[text()='領取']")  #所有可領取按鈕
for button in buttons:
    button.click()
driver.quit()
print("所有免運券領取完成")
