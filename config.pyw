import os
import sys
import json
import tkinter
import tkinter.messagebox as mbox


c_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(c_dir)


class Window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.init_window()

        self.label_0 = tkinter.Label(self.window, text="设  置", font=("", 25))
        self.label_0.place(x=197, y=20)
        self.label_1 = tkinter.Label(self.window, text="账号", font=("", 14))
        self.label_1.place(x=111, y=80)
        self.username_bar = tkinter.Entry(self.window, font=("", 16))
        self.username_bar.place(x=165, y=80)
        self.label_2 = tkinter.Label(self.window, text="密码", font=("", 14))
        self.label_2.place(x=111, y=150)
        self.password_bar = tkinter.Entry(self.window, font=("", 16))
        self.password_bar.place(x=165, y=150)
        self.btn = tkinter.Button(self.window, text="保存", width=10, height=1, font=("", 14), command=self.save)
        self.btn.place(x=195, y=200)
        # self.window.update()

        self.getval()

    def init_window(self):
        self.window.title("设置")
        self.window.geometry("500x300")
        self.window.resizable(False, False)

    def save(self):
        fp = open("./func/config.json")
        pre_dic = json.load(fp)
        fp.close()
        username = self.username_bar.get()
        password = self.password_bar.get()
        if pre_dic['username'] != username:
            dic = None
            with open("./func/config.json", 'r') as fp:
                dic = json.load(fp)
                dic['username'] = username
            with open("./func/config.json", 'w') as fp:
                json.dump(dic, fp, indent=1)
        if pre_dic['password'] != password:
            dic = None
            with open("./func/config.json", 'r') as fp:
                dic = json.load(fp)
                dic['password'] = password
            with open("./func/config.json", 'w') as fp:
                json.dump(dic, fp, indent=1)
        mbox.showinfo(title="提示", message="保存成功！")

    def getval(self):
        fp = open("./func/config.json")
        pre_dic = json.load(fp)
        fp.close()
        self.username_bar.insert(0, pre_dic['username'])
        self.password_bar.insert(0, pre_dic['password'])

    def show(self):
        self.window.mainloop()


if __name__ == '__main__':
    top = Window()
    # print(top.username_bar.winfo_width()) 224
    # print(top.username_bar.winfo_height()) 25
    # print(top.label_1.winfo_width()) 44
    # print(top.label_1.winfo_height()) 25
    # print(top.label_0.winfo_width()) 106
    # print(top.label_0.winfo_height()) 39
    # print(top.btn.winfo_width()) 110
    # print(top.btn.winfo_height()) 33
    top.show()
