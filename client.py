from socket import *
from tkinter import *
import time
import sys

#界面,待实现
class LoginView:
	def __init__(self):
		self.create_window()
		self.create_entry()

	def create_window(self):
		self.window = Tk()
		self.window.title = "盼盼游戏大厅"
		self.window.geometry("150x400")

	def create_entry(self):
		var = StringVar()
		e1 = Entry(self.window,)

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
			data = input(">>>")
			if not data:break
			data = "C" + " " + data
			self.soc.send(data.encode())
			print(self.soc.recv(1024).decode())

#主函数,注意,sys.argv是从终端读取信息作为参数,格式如下:
#python3 .py文件 host port
def main():
	global ADDR
	host = sys.argv[1]
	port = sys.argv[2]
	ADDR = (host,int(port))
	login = Login()
	login.start()
	# view = LoginView()

if __name__ == "__main__":
	# main()
	v = LoginView()
