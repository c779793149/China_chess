from socket import *
from tkinter import *
import time
import sys

#界面,待实现
class LoginView:
	def __init__(self):
		self.start()

	def start(self):
		self.create_window()
		self.create_entry1(self.window)
		self.create_button(self.window)
		self.create_label(self.window)

	def create_window(self):
		self.window = Tk()
		self.window.title("盼盼游戏大厅")
		self.window.geometry("400x150")
		self.window.resizable(0,0)

	def create_entry1(self,root):
		self.var1 = StringVar()
		self.var2 = StringVar()
		self.e1 = Entry(root,textvariable=self.var1)
		self.e1.grid(row=0,column=1)
		self.e2 = Entry(root,textvariable=self.var2,show="*")
		self.e2.grid(row=1,column=1)
		self.t1 = Text(root,width=10,height=5)
		self.t1.grid(row=2)

	def button1(self):
		# self.window.destroy()
		# self.start()
		# self.window.mainloop()

		self.t1.insert(1.0,self.var1.get()+"\n")
		self.t1.insert(2.0,self.var2.get()+"\n")

	def button2(self):
		self.window1 = Tk()
		self.window1.title("注册")
		self.create_label(self.window1)
		self.create_entry1(self.window1)
		self.create_button(self.window1)
		self.window1.mainloop()

	def create_button(self,root):
		Button(root,text="登录",command=self.button1).grid(row=2,column=2)
		Button(root,text="注册",command=self.button2).grid(row=2,column=3)

	def create_label(self,root):
		Label(root,text="账户:").grid(row=0)
		Label(root,text="密码:").grid(row=1)


#登录模块
class Login:
	def __init__(self):
		self.connect()

	#连接服务器
	def connect(self):
		self.soc = socket()
		self.soc.connect(ADDR)

	#模块开始接口
	def start(self):
		print("1 登录")
		print("2 注册")
		choice = input("请选择:")
		if choice == "1":
			self.do_login()
		elif choice == "2":
			self.do_regist()
		elif choice == "3":
			return
		else:
			self.start()

	#登录账户
	def do_login(self):
		user = input("请输入账号:")
		password = input("请输入密码:")
		msg = ("L" + " " + user+"##"+password).encode()
		self.soc.send(msg)
		data = self.soc.recv(1024)
		if data == b"OK":
			print("登录成功")
			self.do_chat()
		elif data == b"NG":
			print("账号不存在,请重试!")
		elif data == b"FAIL":
			print("密码输入错误,请重试!")
		self.start()

	#注册账户
	def do_regist(self):
		user = input("请输入账号:")
		password = input("请输入密码:")
		name = input("请输入昵称:")
		email = input("请输入邮箱")
		identity_card = input("请输入身份证号:")
		msg = "R" + " " + "##".join([user,password,name,email,identity_card])
		self.soc.send(msg.encode())
		data = self.soc.recv(1024)
		if data == b"OK":
			print("注册成功")
			self.do_chat()		
		elif data == b"FAIL":
			print("账号已存在,请重试!")
		self.start()

	#登录之后,循环发送接收消息,后续模块需从此接入
	def do_chat(self):
		while True:
			data = input("请输入>>>")
			if not data:break
			data = "C" + " " + data
			self.soc.send(data.encode())
			print(self.soc.recv(1024).decode())

#主函数,注意,sys.argv是从终端读取信息作为参数,格式如下:
#python3 .py文件 host port
# def main():
# 	global ADDR
# 	host = sys.argv[1]
# 	port = sys.argv[2]
# 	ADDR = (host,int(port))
# 	login = Login()
# 	login.start()
# 	# view = LoginView()

if __name__ == "__main__":
	# main()
	v = LoginView()
	v.window.mainloop()
