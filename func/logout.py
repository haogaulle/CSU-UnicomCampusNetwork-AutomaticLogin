import login


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36',
    'Host': '119.39.119.2'
}


if __name__ == '__main__':
    login.logout_(tempHeaders=headers)
    print('注销成功！')
    input("***按回车退出***")
