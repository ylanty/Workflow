import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


driver.get('https://www.baidu.com/')
print(driver.title)
def xiaoaishe_sign():
    # 找到插件的路径，使用它驱动操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    #browser = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
     
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
    browser.quit()
    
def maozhua_sign():
    # 找到插件的路径，使用它驱动操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    #browser = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
     
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
    browser.quit()
 
if __name__ == '__main__':
    xiaoaishe_sign()
    maozhua_sign()
