import os
import sys
import tkinter
import tkinter.messagebox as mbox
from threading import Thread

c_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(c_dir)

from func.login import login_
from func import settings

window = None


def check_status_200(event):
    mbox.showinfo(title='提示', message='网络连接成功！')
    sys.exit()


def check_status_404(event):
    res = mbox.askretrycancel(title='错误', message='请检查wifi或网线连接！')
    if res:
        global window
        connect_web(window)
    else:
        sys.exit()


def check_status_500(event):
    res = mbox.askretrycancel(title='提示', message='网络连接失败，请重试')
    if res:
        global window
        connect_web(window)
    else:
        sys.exit()


def create_window():
    top = tkinter.Tk()
    top.title("校园网登录")
    top.geometry("600x200")
    top.resizable(False, False)
    label_1 = tkinter.Label(top, text="正在尝试连接到校园网", font=("Microsoft YaHei", 20))
    label_2 = tkinter.Label(top, text="made by HaoGaulle 2090029747@qq.com", font=("", 10))
    label_1.place(x=162, y=50)
    label_2.place(x=175, y=120)

    top.bind("<<sucEvent>>", check_status_200)
    top.bind("<<failEvent>>", check_status_500)
    top.bind("<<wrongEvent>>", check_status_404)

    return top


def connect_web(root):
    thread = Thread(target=login_, args=(settings.data, settings.headers, root))
    thread.start()


if __name__ == '__main__':
    window = create_window()
    connect_web(window)
    window.mainloop()
