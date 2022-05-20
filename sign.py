import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def xiaoaishe_sign(browser):
    try:
        # 选择需要打卡的网址，填入你的签到网页
        browser.get('https://xiaoaishe.com/mission/today')
        browser.find_element_by_xpath('//div[@class="modal-content b2-radius"]//span[@class="close-button"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//button[@class="empty mobile-hidden"]').click()
        time.sleep(2)
        # 找到邮件和密码输入框的xpath,并在对应的位置送入账号密码
        browser.find_element_by_xpath('//label[@class="login-form-item"]//input[@name="username"]').send_keys(os.environ["xiaoaishe_username"])
        browser.find_element_by_xpath('//label[@class="login-form-item"]//input[@name="password"]').send_keys(os.environ["xiaoaishe_password"])
        # 找到登录按钮的xpath，模拟点击
        browser.find_element_by_xpath('//div[@class="login-box-in"]//div[@class="login-bottom"]//button').click()
        time.sleep(2)
        # 找到签到按钮的xpath，模拟签到
        browser.find_element_by_xpath('//div[@class="bar-item bar-mission"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//div[@class="bar-user-info-row bar-mission-action"]').click()
    except Exception as e:
        print("有错误:", e)
    
def maozhua_sign(browser):
    try:
        # 选择需要打卡的网址，填入你的签到网页
        browser.get('https://maozhua.org/mission/today')
        browser.find_element_by_xpath('//button[@class="empty mobile-hidden"]').click()
        time.sleep(2)
        # 找到邮件和密码输入框的xpath,并在对应的位置送入账号密码
        browser.find_element_by_xpath('//label[@class="login-form-item"]//input[@name="username"]').send_keys(os.environ["maozhua_username"])
        browser.find_element_by_xpath('//label[@class="login-form-item"]//input[@name="password"]').send_keys(os.environ["maozhua_password"])
        # 找到登录按钮的xpath，模拟点击
        browser.find_element_by_xpath('//div[@class="login-box-in"]//div[@class="login-bottom"]//button').click()
        time.sleep(2)
        # 找到签到按钮的xpath，模拟签到
        browser.find_element_by_xpath('//div[@class="bar-item bar-mission"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//div[@class="bar-user-info-row bar-mission-action"]').click()
    except Exception as e:
        print("有错误:", e)
 
def sdai_sign(browser):
    try:
        # 选择需要打卡的网址，填入你的签到网页
        browser.get('https://www.sdai.me/')
        # 找到邮件和密码输入框的xpath,并在对应的位置送入账号密码
        browser.find_element_by_xpath('//input[@id="user_login"]').send_keys(os.environ["sdai_username"])
        browser.find_element_by_xpath('//input[@id="user_pass"]').send_keys(os.environ["sdai_password"])  
        # 找到登录按钮的xpath，模拟点击
        browser.find_element_by_xpath('//input[@id="wp-submit"]').click()
        time.sleep(2)
        # 找到签到按钮的xpath，模拟签到
        browser.find_element_by_xpath('//a[@class="poi-tooltip is-bottom inn-nav__point-sign-daily__btn"]').click()
    except Exception as e:
        print("有错误:", e)
    
if __name__ == '__main__':
    # 找到插件的路径，使用它驱动操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    xiaoaishe_sign(browser)
    maozhua_sign(browser)
    sdai_sign(browser)
    browser.quit()
