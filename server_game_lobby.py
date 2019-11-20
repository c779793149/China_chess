from socket import *
from tkinter import *
from select import select
from threading import Thread
from time import time,sleep
import sys,os,pymysql


class LoginManager:
	def __init__(self):
		self.create_soc()
		self.create_select()
		self.connect_mysql()

	#创建套接字
	def create_soc(self):
		addr = ("0.0.0.0",10086)
		self.soc = socket()
		self.soc.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		self.soc.bind(addr)
		self.soc.listen(3)

	#IO多路复用,创建select监听列表
	def create_select(self):
		self.rlist = [self.soc] #读IO,一般只用这个
		self.wlist = []
		self.xlist = []
	
	#连接数据库,设置通用sql语句
	def connect_mysql(self):
		self.db = pymysql.connect("localhost","root","123456","game_lobby",charset="utf8")
		self.cur = self.db.cursor()
		self.sql1 = "select user,password from user where user=%s;"
		self.sql2 = "select user from user where user=%s and name=%s;"
		self.sql3 = "insert into user (user,password,name,email,identity_card) values (%s,%s,%s,%s,%s);"

	#开始接口,循环监听客户端请求
	def start(self):
		while True:
			self.rs,self.ws,self.xs = select(self.rlist,self.wlist,self.xlist)
			for r in self.rs:
				if r == self.soc:
					self.do_connect()
				else:
					self.do_request(r)

	#连接客户端
	def do_connect(self):
		soc,addr = self.soc.accept()
		self.rlist.append(soc)
		
	#处理请求
	def do_request(self,soc):
		msg = soc.recv(1024).decode()
		if not msg:
			self.rlist.remove(soc)
			soc.close()
			return
		action,data = msg.split(" ",1)
		if action == "L":
			self.do_verify(soc,data)
		elif action == "R":
			self.do_regist(soc,data)
		else:
			self.do_chat(soc,data)

	#验证账户密码
	def do_verify(self,*args):
		data = tuple(args[1].split("##"))
		print(data)
		self.cur.execute(self.sql1,data[0])
		info = self.cur.fetchone()
		print(info)
		if not info:
			args[0].send(b"NG")
		elif info ==data:
			args[0].send(b"OK")
		else:
			args[0].send(b"FAIL")

	#注册用户
	def do_regist(self,*args):
		data = args[1].split("##")
		print(data)
		self.cur.execute(self.sql2,data[:2])
		info = self.cur.fetchone()
		if not info:
			try:
				self.cur.execute(self.sql3,data)
				self.db.commit()
			except:
				args[0].send(b"FAIL")
			else:
				args[0].send(b"OK")
		else:
			args[0].send(b"FAIL")

	#登录完毕后,处理消息,待完善
	def do_chat(self,soc,data):
		print(data)
		soc.send(b"***")

def main():
	manager = LoginManager()
	manager.start()

if __name__ == "__main__":
	main()
