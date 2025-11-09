# python3 -m venv shopee_test
# sudo apt-get install python3-pip
# sudo apt-get install python3-bs4
# pip3 install beautifulsoup4
# pip3 install selenium
# pip3 install requests
# sudo tar -xzvf geckodriver-v0.32.0-linux64.tar.gz -C /usr/local/bin
# chmod +x /usr/local/bin/geckodriver
# export PATH=$PATH:/usr/local/bin/geckodriver

import time
from selenium import webdriver
import subprocess

#common
options = webdriver.FirefoxOptions()
options.browser_version = "stable"
options.page_load_strategy = "normal"
print(options.platform_name)
options.platform_name = "linux"
options.accept_insecure_certs = True
print(options.timeouts)
options.timeouts = {"script":30000, "pageLoad":300000, "implicit":0}
options.unhandled_prompt_behavior = "dismiss and notify"
options.set_window_rect = True
options.strict_file_interactability = False
options.enable_downloads = True

service = webdriver.FirefoxService(port = 59475, log_output=r"./.logtext", service_args=['--log', 'debug'])
print(service.port)

#firefox specific
# options.add_argument("-headless")
firefox_profile = webdriver.firefox.firefox_profile.FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile


driver = webdriver.Firefox(options = options, service = service) #使用火狐瀏覽器 
driver.maximize_window()
# driver.install_addon(r"./sidebery-5.3.3.xpi")
driver.implicitly_wait(5)

url = r"https://www.selenium.dev/selenium/web/web-form.html"

driver.get(url)
driver.save_full_page_screenshot(r"./screenshot.png")
title = driver.title

driver.implicitly_wait(5)

# text_box = driver.find_element(by=webdriver.common.by.By.NAME, value="my-password")
text_box = driver.find_element(by = webdriver.common.by.By.CSS_SELECTOR, value="#my-text-id")
# wait = WebDriverWait(driver, timeout=2)
# wait.until(lambda _ : revealed.is_displayed())
# submit_button = driver.find_element(by=webdriver.common.by.By.CSS_SELECTOR, value="button")
submit_button = driver.find_element(by = webdriver.common.by.By.CLASS_NAME, value="btn")

text_box.send_keys("WTFFFF")
submit_button.click()
message = driver.find_element(by=webdriver.common.by.By.ID, value="message")
text = message.text

driver.quit()

# url_2 = r"https://shopee.tw/"
# driver = webdriver.Firefox()
# driver.get(url_2) #進到蝦皮登錄頁面
# driver.implicitly_wait(3)
#time.sleep(10) #等待(10秒)瀏覽器解析html資料（因為我的網路有點慢）
#driver.find_element(By.CSS_SELECTOR, "[name = loginKey]").send_keys(user_account)
#driver.find_element(By.CSS_SELECTOR, "[name = password]").send_keys(user_password)
#driver.find_elements(By.CSS_SELECTOR, "button")[2].click()
#time.sleep(300) #這段時間內(5分鐘)請盡快完成簡訊驗證登錄

#shopee_cookie = driver.get_cookies() #取出cookie
#with open("shopee.json", "w") as f:
#    f.write(json.dumps(shopee_cookie)) #將cookie寫入shopee.json，檔案存在跟主程式同目錄
# driver.quit() #關閉瀏覽器

