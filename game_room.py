from master import *
from threading import Thread
from select import select

class Gamemanager:
    def __init__(self,soc,que):
        self.soc = soc
        self.que = que
        self.rlist = []
        self.user_dict = {} #用户名为值,连接套接字为键,方便查找用户
        self.play_user = {} #对局用户,键值均为套接字
        self.table = [[] for i in range(10)]

    #模块入口,循环接收客户端请求
    def server_forver(self):
        t1 = Thread(target=self.add_user)
        t2 = Thread(target=self.do_request)
        t1.start()
        t2.start()


    def do_request(self):
        self.ws = []
        self.xs = []
        while True:
            if self.rlist:
                # print(self.rlist)
                rs, ws, xs = select(self.rlist, self.ws, self.xs,1)
            else:
                continue
            # print("select已执行")
            for r in rs:
                msg = r.recv(1024).decode()
                if not msg:
                    self.do_quit()
                else:
                    print(msg)
                    action,data = msg.split(" ",1)
                    if action == "T":
                        self.get_ready(r,data)
                    elif action == "G":
                        print(data)
                        self.play_game(r,data)

    #进入房间入座
    def get_ready(self,r,msg):
        n,data = msg.split("##",1)
        n = int(n)
        if data == "IN": #表示玩家要加入某一桌游戏
            self.verify_table(n,r)
        elif data == "OK": #表示玩家已准备
            r.send(b"OK")
            self.start_game(n,r)
        elif data == "LOOK": #观战,暂缓
            pass

    def verify_table(self,n,r):
        if len(self.table[n-1]) < 2:
            self.table[n-1].append(r)
            print(self.table)
            r.send(b"OK")
        else:
            r.send(b"NG")

    #注意,玩家准备之后进入收发同步阶段
    def start_game(self,n,r):
        if len(self.table[n-1]) == 2:
            # 把对局玩家加入字典,可以快速处理对局信息
            self.play_user[r] = self.table[n-1][0]
            self.play_user[self.table[n-1][0]] = r
            r.send("START 红".encode())
            self.table[n-1][0].send("START 黑".encode())

    #发送对局信息给对方
    def play_game(self,r,data):
        self.play_user[r].send(data.encode())

    def add_user(self):
        while True:
            soc = self.que.get()
            print("添加用户",soc)
            self.rlist.append(soc)

    def do_quit(self):
        pass

# class User:
#     def __init__(self,soc,user,table=None):
#         self.soc = soc
#         self.user = user
#         self.table = table




