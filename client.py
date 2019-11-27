from socket import *
from tkinter import *
from config import *
from master import *
import time
import sys

#界面,待实现
class LoginView:
	def __init__(self):
		self.create_window()
		# self.create_entry()

	def create_window(self):
		self.window = Tk()
		self.window.title = "盼盼游戏大厅"
		self.window.geometry("400x200")
		self.window.resizable(width=False,height=False)
		self.create_entry()
		self.create_button()
		self.window.mainloop()

	def create_entry(self):
		e1 = Entry()
		self.t1 = Text(self.window,width=100,height=5)
		e1.pack()
		self.t1.pack()


	def create_button(self):
		Button(self.window,text="aaa",command=self.button1).pack(side=TOP)

	def button1(self):
		# self.window.quit()
		self.t1.insert(0.0,"Hello,Newin\n")
		self.window.destroy() #关闭窗口,打开新窗口
		self.create_window()

	# def create_newindow(self):
	# 	self.window = Tk()
	# 	self.create_button(self.w1)
	# 	self.create_entry(self.w1)
	# 	self.w1.mainloop()


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
			print("1 进入游戏!")
			print("2 退出大厅!")
			data = input("请选择:")
			if data == "1":
				self.play_game1()
			elif data == "2":
				pass
			else:
				pass

	def play_game1(self):
		while True:
			self.soc.send(b"C OK")
			data = self.soc.recv(1024)
			print(data)
			if data == b"OK":
				self.soc.send(b"T 1##IN")
				data = self.soc.recv(1024)
				print(data)
				if data == b"OK":
					self.soc.send(b"T 1##OK")
					data = self.soc.recv(1024).decode()
					print(data)
					data = self.soc.recv(1024).decode()
					print(data)
					camp = data[1]
					return self.play_game2(camp)

	def play_game2(self,camp):
		manager = Manager(camp,self.soc)
		print("start")
		manager.start()

#主函数,注意,sys.argv是从终端读取信息作为参数,格式如下:
#python3 .py文件 host port
def main():
	global ADDR
	ADDR = (HOST,PORT)
	login = Login()
	login.start()
	# view = LoginView()

if __name__ == "__main__":
	main()
	# v =LoginView()