import requests
import time
from func import settings
from requests.exceptions import ConnectionError


def logout_(tempHeaders):
    try:
        requests.get(url=settings.logoutUrl, headers=tempHeaders, timeout=2)
    except Exception:
        return False
    return True


def login_(tempData, tempHeaders, root):
    time.sleep(1.5)
    if not logout_(tempHeaders=tempHeaders):
        root.event_generate("<<wrongEvent>>")
        return
    response = requests.post(url=settings.loginUrl, data=tempData, headers=tempHeaders)
    flag = True
    if response.status_code == 200:
        try:
            requests.get(url=settings.testUrl, timeout=2)
        except requests.exceptions.ReadTimeout:
            flag = False
            root.event_generate("<<failEvent>>")
            return
        if flag:
            root.event_generate("<<sucEvent>>")
            return


if __name__ == '__main__':
    pass
