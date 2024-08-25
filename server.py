import socket
import tkinter as tk
from tkinter import *


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print(f"伺服器的IP地址為{ip}")
port = 9999

s.bind((ip,port))
s.listen(1)
print('等待客戶端連接...')
# 接受客戶端連接
client_socket, client_address = s.accept()
print('已連接：', client_address)

windows = Tk()
windows.title("server")
windows.geometry('500x400')

tk.Label(windows, text ="Welcome", bg = "lightblue").pack()
ip = "服務端" + str(client_address)
tk.Label(windows, text = ip, bg = "white").pack()
tk.Label(windows, text="輸入訊息").pack()
entry_1 = tk.Entry(windows)
entry_1.pack()
def sendms():
    message = entry_1.get()
    client_socket.send(message.encode())
tk.Button(windows, text="send",command=sendms).pack()

tk.Label(windows, text = "發送訊息方塊").pack()
entry_2 = tk.Entry(windows)
entry_2.pack()
def textbox():
    message = "textbox(" + entry_2.get() + ")"
    client_socket.send(message.encode())
tk.Button(windows, text = "send", command = textbox).pack()

tk.Label(windows,text = "開啟網站").pack()
entry_3 = tk.Entry(windows)
entry_3.pack()
def opwb():
    message = "open(" + entry_3.get() + ")"
    client_socket.send(message.encode())
tk.Button(windows, text = "send",command=opwb).pack()

tk.Label(windows,text = "傳送指令").pack()
entry_4 = tk.Entry(windows)
entry_4.pack()
def runcd():
    message = "cmd(" + entry_4.get() + ")"
    client_socket.send(message.encode())
tk.Button(windows,text = "send",command=runcd).pack()

def quit():
    client_socket.send("quit".encode())
    client_socket.close()
    s.close()
    windows.quit()
    
tk.Button(windows, text = "結束連接", command=quit).pack()


windows.mainloop()
s.close()


    
    
    



