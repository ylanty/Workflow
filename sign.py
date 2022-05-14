import requests
import os

session = requests.session()
#获取token
url = 'https://xiaoaishe.com/wp-json/b2/v1/getRecaptcha'
data = {'number': '4','width': '186','height': '50'}
token = session.post(url = url,data=data).json()['token']
#print(token)
#登录
url = 'https://xiaoaishe.com/wp-json/jwt-auth/v1/token'
data = {'username': os.environ['xiaoaishe_username'],'password': os.environ['xiaoaishe_password'],'token': token}
login_cookies = session.post(url = url,data=data).cookies.get_dict()
#签到
url = 'https://xiaoaishe.com/wp-json/b2/v1/userMission'
#cookies = dict(b2_back_url='https://xiaoaishe.com/vips',b2_token=b2_token,PHPSESSID=PHPSESSID)
#requests.utils.add_dict_to_cookiejar(session.cookies, login_cookies)
data = {}
headers = {'authorization': 'Bearer '+login_cookies['b2_token']}
jg = session.post(url=url, data=data, headers=headers)
print(jg.text)

session = requests.session()
#登录
url = 'https://maozhua.org/wp-json/jwt-auth/v1/token'
data = {'username': os.environ['maozhua_username'],'password': os.environ['maozhua_password']}
login_cookies = session.post(url = url,data=data).cookies.get_dict()
#print(login_cookies)
#获取PHPSESSID
url = 'https://maozhua.org/wp-json/b2/v1/tjuser'
data = {}
headers = {'authorization': 'Bearer '+login_cookies['b2_token']}
cookies = session.post(url = url,data=data, headers=headers).cookies.get_dict()
#print(cookies['PHPSESSID'])
#maozhua签到
url = 'https://maozhua.org/wp-json/b2/v1/userMission'
data = {}
headers = {'authorization': 'Bearer '+b2_token}
jg = session.post(url=url, data=data, headers=headers)
print(jg.text)
