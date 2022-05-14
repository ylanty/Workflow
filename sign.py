import requests
import os

xiaoaishe_session = requests.session()
#获取token
xiaoaishe_url = 'https://xiaoaishe.com/wp-json/b2/v1/getRecaptcha'
xiaoaishe_data = {'number': '4','width': '186','height': '50'}
xiaoaishe_token = xiaoaishe_session.post(url = xiaoaishe_url,data=xiaoaishe_data).json()['token']
#print(token)
#登录
xiaoaishe_url = 'https://xiaoaishe.com/wp-json/jwt-auth/v1/token'
xiaoaishe_data = {'username': os.environ['xiaoaishe_username'],'password': os.environ['xiaoaishe_password'],'token': xiaoaishe_token}
xiaoaishe_login_cookies = xiaoaishe_session.post(url = xiaoaishe_url,data=xiaoaishe_data).cookies.get_dict()
#签到
xiaoaishe_url = 'https://xiaoaishe.com/wp-json/b2/v1/userMission'
#cookies = dict(b2_back_url='https://xiaoaishe.com/vips',b2_token=b2_token,PHPSESSID=PHPSESSID)
#requests.utils.add_dict_to_cookiejar(session.cookies, login_cookies)
xiaoaishe_data = {}
xiaoaishe_headers = {'authorization': 'Bearer '+xiaoaishe_login_cookies['b2_token']}
xiaoaishe_res = xiaoaishe_session.post(url=xiaoaishe_url, data=xiaoaishe_data, headers=xiaoaishe_headers)
print(xiaoaishe_res.text)

maozhua_session = requests.session()
#登录
maozhua_url = 'https://maozhua.org/wp-json/jwt-auth/v1/token'
maozhua_data = {'username': os.environ['maozhua_username'],'password': os.environ['maozhua_password']}
maozhua_login_cookies = maozhua_session.post(url = maozhua_url,data=maozhua_data).cookies.get_dict()
#print(login_cookies)
#获取PHPSESSID
maozhua_url = 'https://maozhua.org/wp-json/b2/v1/tjuser'
maozhua_data = {}
maozhua_headers = {'authorization': 'Bearer '+maozhua_login_cookies['b2_token']}
maozhua_cookies = maozhua_session.post(url = maozhua_url,data=maozhua_data, headers=maozhua_headers).cookies.get_dict()
#print(cookies['PHPSESSID'])
#maozhua签到
maozhua_url = 'https://maozhua.org/wp-json/b2/v1/userMission'
maozhua_data = {}
maozhua_headers = {'authorization': 'Bearer '+maozhua_login_cookies['b2_token']}
maozhua_res = maozhua_session.post(url=maozhua_url, data=maozhua_data, headers=maozhua_headers)
print(maozhua_res.text)
