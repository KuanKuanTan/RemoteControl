# RemoteControl
Server端可用GUI介面對Client(服務端)進行傳送訊息、傳送訊息方塊、控制開啟網站、傳送指令功能
#所需模組(基本上都已有內建，不須安裝):
  1.tkinter
  2.os
  3.webbrowser
  4.socket
#使用說明:
##檔案說明:
`server.py`:伺服器控制端
`client.py`:服務接收端
##使用說明:
先在server端執行server.py，終端機會顯示server的IP地址，請記下。然後在client端執行client.py，並在終端機中輸入server的IP地址，成功連線上後server端會自動開啟GUI介面。
##功能說明:
  1.傳送訊息:在輸入框中寫入訊息後，按下send，訊息就會顯示在client端的終端機上
  2.發送訊息方塊:在輸入框中寫入訊息後，按下send，訊息框就會顯示在client端的螢幕上
  3.開啟網站:在輸入框中輸入網址後，按下send，client端就會在預設瀏覽器中開啟網站
  4.傳送指令:在輸入框中輸入指令代碼後(如:shutdown -s -t 1)，client端就會直接執行指令
  5.結束連線:按下後會關閉server端和client端的socket連線，關閉GUI介面，和停止程式
  
  
