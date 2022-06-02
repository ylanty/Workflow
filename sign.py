import pymysql
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
        browser.get('https://xiaoai996.com/mission/today')
        time.sleep(2)
        browser.find_element(By.XPATH,'//div[@class="modal-content b2-radius"]//span[@class="close-button"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH,'//button[@class="empty mobile-hidden"]').click()
        time.sleep(2)
        # 找到邮件和密码输入框的xpath,并在对应的位置送入账号密码
        browser.find_element(By.XPATH,'//label[@class="login-form-item"]//input[@name="username"]').send_keys(os.environ["xiaoaishe_username"])
        browser.find_element(By.XPATH,'//label[@class="login-form-item"]//input[@name="password"]').send_keys(os.environ["xiaoaishe_password"])
        # 找到登录按钮的xpath，模拟点击
        browser.find_element(By.XPATH,'//div[@class="login-box-in"]//div[@class="login-bottom"]//button').click()
        time.sleep(2)
        # 找到签到按钮的xpath，模拟签到
        browser.find_element(By.XPATH,'//div[@class="bar-item bar-mission"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH,'//div[@class="bar-user-info-row bar-mission-action"]').click()
        time.sleep(2)
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
        time.sleep(2)
        browser.find_element(By.XPATH,'//button[@class="empty mobile-hidden"]').click()
        time.sleep(2)
        # 找到邮件和密码输入框的xpath,并在对应的位置送入账号密码
        browser.find_element(By.XPATH,'//label[@class="login-form-item"]//input[@name="username"]').send_keys(os.environ["maozhua_username"])
        browser.find_element(By.XPATH,'//label[@class="login-form-item"]//input[@name="password"]').send_keys(os.environ["maozhua_password"])
        # 找到登录按钮的xpath，模拟点击
        browser.find_element(By.XPATH,'//div[@class="login-box-in"]//div[@class="login-bottom"]//button').click()
        time.sleep(2)
        # 找到签到按钮的xpath，模拟签到
        browser.find_element(By.XPATH,'//div[@class="bar-item bar-mission"]').click()
        time.sleep(2)
        browser.find_element(By.XPATH,'//div[@class="bar-user-info-row bar-mission-action"]').click()
        time.sleep(2)
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
 
def sdai_sign(browser):
    try:
        # 选择需要打卡的网址，填入你的签到网页
        browser.get('https://www.sdai.me/')
        time.sleep(2)
        # 找到邮件和密码输入框的xpath,并在对应的位置送入账号密码
        browser.find_element(By.XPATH,'//input[@id="user_login"]').send_keys(os.environ["sdai_username"])
        browser.find_element(By.XPATH,'//input[@id="user_pass"]').send_keys(os.environ["sdai_password"])  
        # 找到登录按钮的xpath，模拟点击
        browser.find_element(By.XPATH,'//input[@id="wp-submit"]').click()
        time.sleep(2)
        # 找到签到按钮的xpath，模拟签到
        try:
            browser.find_element(By.XPATH,'//a[@class="poi-tooltip is-bottom inn-nav__point-sign-daily__btn"]').click()
            time.sleep(2)
        except Exception as e:
            print("sdai签到有错误:", e)
        browser.get('https://www.sdai.me/')
        time.sleep(2)
        browser.find_element(By.XPATH,'//div[@id="inn-user-menu__container"]').click()
        time.sleep(2)
        func.daylylog(browser.find_element(By.XPATH,'//fieldset/div[4]').text)
    except Exception as e:
        print("sdai有错误:", e)

def executesql(web_name,result):
    # 打开数据库连接
    db = pymysql.connect(host='os.environ["mysql_host"]',
                         user='os.environ["mysql_username"]',
                         password='os.environ["mysql_password"]',
                         database='os.environ["mysql_database"]')
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 语句
    sql = "INSERT INTO `daylylog`(`web_name`, `day_time`, `result`, `sys_time`) VALUES ('%s', utc_date(), '%s',sysdate())" %(web_name,result)
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 执行sql语句
       db.commit()
    except:
       # 发生错误时回滚
       db.rollback()
    finally:
        # 关闭数据库连接
        cursor.close()
        db.close()

def isexecuted(web_name):
    # 打开数据库连接
    db = pymysql.connect(host='os.environ["mysql_host"]',
                         user='os.environ["mysql_username"]',
                         password='os.environ["mysql_password"]',
                         database='os.environ["mysql_database"]')
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 语句
    sql = "SELECT * FROM `daylylog` WHERE `web_name` = '%s' and `day_time` = utc_date() " %web_name
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       if len(results)>0:
           return True
       else:
           return False
    except:
       # 发生错误
       print ("Error: unable to fetch data")
       return False
    finally:
        # 关闭数据库连接
        cursor.close()
        db.close()

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('ignore-certificate-errors')
    browser = webdriver.Chrome(options=chrome_options)
    # 找到插件的路径，使用它驱动操作
    if isexecuted('xiaoaishe') :
        print('xiaoaishe已签到')
    elif xiaoaishe_sign(browser) :
        executesql('xiaoaishe',xiaoaishe_res)
    if isexecuted('maozhua') :
        print('maozhua已签到')
    elif maozhua_sign(browser) :
        executesql('maozhua',maozhua_res)
    # xiaoaishe_sign(browser)
    # maozhua_sign(browser)
    # sdai_sign(browser)
    browser.quit()
