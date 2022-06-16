import time
import os
import func
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

xiaoaishe_res = ''
maozhua_res = ''

def xiaoaishe_sign(browser):
    try:
        # 选择需要打卡的网址，填入你的签到网页
        # browser.get('https://xiaoaishe.com/mission/today')
        browser.get('https://xiaoai986.com/mission/today')
        time.sleep(0.5)
        browser.find_element(By.XPATH,'//div[@class="modal-content b2-radius"]//span[@class="close-button"]').click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,'//button[@class="empty mobile-hidden"]').click()
        time.sleep(0.5)
        # 找到邮件和密码输入框的xpath,并在对应的位置送入账号密码
        browser.find_element(By.XPATH,'//label[@class="login-form-item"]//input[@name="username"]').send_keys(os.environ["xiaoaishe_username"])
        browser.find_element(By.XPATH,'//label[@class="login-form-item"]//input[@name="password"]').send_keys(os.environ["xiaoaishe_password"])
        # 找到登录按钮的xpath，模拟点击
        browser.find_element(By.XPATH,'//div[@class="login-box-in"]//div[@class="login-bottom"]//button').click()
        time.sleep(0.5)
        # 找到签到按钮的xpath，模拟签到
        browser.find_element(By.XPATH,'//div[@class="bar-item bar-mission"]').click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,'//div[@class="bar-user-info-row bar-mission-action"]').click()
        time.sleep(0.5)
        # func.daylylog(browser.find_element(By.XPATH,'//div[@class="bar-user-info-row bar-mission-action"]').text)
        global xiaoaishe_res
        xiaoaishe_res = browser.find_element(By.XPATH,'//div[@class="bar-user-info-row bar-mission-action"]').text
        if '恭喜' in xiaoaishe_res :
            print(xiaoaishe_res)
            return True
        else:
            return False
    except Exception as e:
        print("xiaoaishe有错误:", e)
        return False
    
def maozhua_sign(browser):
    try:
        # 选择需要打卡的网址，填入你的签到网页
        browser.get('https://maozhua.org/mission/today')
        time.sleep(0.5)
        browser.find_element(By.XPATH,'//button[@class="empty mobile-hidden"]').click()
        time.sleep(0.5)
        # 找到邮件和密码输入框的xpath,并在对应的位置送入账号密码
        browser.find_element(By.XPATH,'//label[@class="login-form-item"]//input[@name="username"]').send_keys(os.environ["maozhua_username"])
        browser.find_element(By.XPATH,'//label[@class="login-form-item"]//input[@name="password"]').send_keys(os.environ["maozhua_password"])
        # 找到登录按钮的xpath，模拟点击
        browser.find_element(By.XPATH,'//div[@class="login-box-in"]//div[@class="login-bottom"]//button').click()
        time.sleep(0.5)
        # 找到签到按钮的xpath，模拟签到
        browser.find_element(By.XPATH,'//div[@class="bar-item bar-mission"]').click()
        time.sleep(0.5)
        browser.find_element(By.XPATH,'//div[@class="bar-user-info-row bar-mission-action"]').click()
        time.sleep(0.5)
        # func.daylylog(browser.find_element(By.XPATH,'//div[@class="bar-user-info-row bar-mission-action"]').text)
        global maozhua_res
        maozhua_res = browser.find_element(By.XPATH,'//div[@class="bar-user-info-row bar-mission-action"]').text
        if '恭喜' in maozhua_res :
            print(maozhua_res)
            return True
        else:
            return False
    except Exception as e:
        print("maozhua有错误:", e)
        return False

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('ignore-certificate-errors')
    browser = webdriver.Chrome(options=chrome_options)
    # 找到插件的路径，使用它驱动操作
    if func.isexecuted('xiaoaishe') :
        print('xiaoaishe已签到')
    elif xiaoaishe_sign(browser) :
        func.executesql('xiaoaishe',xiaoaishe_res)
    if func.isexecuted('maozhua') :
        print('maozhua已签到')
    elif maozhua_sign(browser) :
        func.executesql('maozhua',maozhua_res)
    # xiaoaishe_sign(browser)
    # maozhua_sign(browser)
    browser.quit()
