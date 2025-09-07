# python3 -m venv shopee_test
# sudo apt-get install python3-pip
# sudo apt-get install python3-bs4
# pip3 install beautifulsoup4
# pip3 install selenium
# pip3 install requests
# wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
# sudo tar -xzvf geckodriver-v0.32.0-linux64.tar.gz -C /usr/local/bin
# chmod +x /usr/local/bin/geckodriver
# export PATH=$PATH:/usr/local/bin/geckodriver

import time
from selenium import webdriver

driver = webdriver.Firefox() #使用火狐瀏覽器 

url = r"https://www.selenium.dev/selenium/web/web-form.html"

driver.get(url)

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=webdriver.common.by.By.NAME, value="my-password")
submit_button = driver.find_element(by=webdriver.common.by.By.CSS_SELECTOR, value="button")

text_box.send_keys("WTFFFF")
submit_button.click()

message = driver.find_element(by=webdriver.common.by.By.ID, value="message")
text = message.text

driver.quit()
print(text)

url_2 = r"https://shopee.tw/"
driver = webdriver.Firefox()
driver.get(url_2) #進到蝦皮登錄頁面
driver.implicitly_wait(3)
#time.sleep(10) #等待(10秒)瀏覽器解析html資料（因為我的網路有點慢）
#driver.find_element(By.CSS_SELECTOR, "[name = loginKey]").send_keys(user_account)
#driver.find_element(By.CSS_SELECTOR, "[name = password]").send_keys(user_password)
#driver.find_elements(By.CSS_SELECTOR, "button")[2].click()
#time.sleep(300) #這段時間內(5分鐘)請盡快完成簡訊驗證登錄

#shopee_cookie = driver.get_cookies() #取出cookie
#with open("shopee.json", "w") as f:
#    f.write(json.dumps(shopee_cookie)) #將cookie寫入shopee.json，檔案存在跟主程式同目錄
driver.quit() #關閉瀏覽器

