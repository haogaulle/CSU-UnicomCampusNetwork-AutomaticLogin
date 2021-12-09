import json
fp = open("./func/config.json")
dic = json.load(fp)
# 用户名和密码配置
username = dic['username']
password = dic['password']
fp.close()

# 连通性检测域名
testUrl = "https://www.baidu.com/"

# 登录&注销ip
loginUrl = "http://119.39.119.2/a70.htm"
logoutUrl = "http://119.39.119.2/F.htm"

# 请求配置
data = {
    'DDDDD': username + '@zndx',
    'upass': password,
    'R1': '0',
    'R2': '',
    'R3': '0',
    'R6': '0',
    'para': '00',
    '0MKKey': password,
    'buttonClicked': '',
    'redirect_url': '',
    'err_flag': '',
    'username': '',
    'password': '',
    'user': '',
    'cmd': '',
    'Login': '',
    'v6ip': ''
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36',
    'Host': '119.39.119.2'
}
