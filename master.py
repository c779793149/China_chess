from chess import *


class Manager:
    def __init__(self):
        self.create_chess()
        self.map = [[self.blank for i in range(9)] for j in range(10)]
        self.chess = [
            self.rook1_red,
            self.knight1_red,
            self.ele1phant1_red,
            self.mandarin1_red,
            self.king,
            self.ele1phant2_red,
            self.ele1phant2_red,
            self.knight2_red,
            self.rook2_red,
            self.cannon1_red,
            self.cannon2_red,
            self.pawn1_red,
            self.pawn2_red,
            self.pawn3_red,
            self.pawn4_red,
            self.pawn5_red,
            self.pawn1_black,
            self.pawn2_black,
            self.pawn3_black,
            self.pawn4_black,
            self.pawn5_black,
            self.cannon1_black,
            self.cannon2_black,
            self.rook1_black,
            self.knight1_black,
            self.ele1phant1_black,
            self.mandarin1_black,
            self.general,
            self.mandarin2_black,
            self.ele1phant2_black,
            self.knight2_black,
            self.rook2_black
        ]

    def create_chess(self):
        self.rook1_red = Rook("车", "红",(9,0))
        self.rook2_red = Rook("车", "红",(9,8))
        self.rook1_black = Rook("车", "黑",(0,0))
        self.rook2_black = Rook("车", "黑",(0,8))
        self.knight1_red = Knight("马", "红",(9,1))
        self.knight2_red = Knight("马", "红",(9,7))
        self.knight1_black = Knight("马", "黑",(0,1))
        self.knight2_black = Knight("马", "黑",(0,7))
        self.ele1phant1_red = Elephant("相", "红",(9,2))
        self.ele1phant2_red = Elephant("相", "红",(9,6))
        self.ele1phant1_black = Elephant("象", "黑",(0,2))
        self.ele1phant2_black = Elephant("象", "黑",(0,6))
        self.mandarin1_red = Mandarin("士", "红",(9,3))
        self.mandarin2_red = Mandarin("士", "红",(9,5))
        self.mandarin1_black = Mandarin("士", "黑",(0,3))
        self.mandarin2_black = Mandarin("士", "黑",(0,5))
        self.general = King("帅", "红",(9,4))
        self.king = King("帅", "黑",(0,4))
        self.cannon1_red = Cannon("炮", "红",(7,1))
        self.cannon2_red = Cannon("炮", "红",(7,7))
        self.cannon1_black = Cannon("炮", "黑",(2,1))
        self.cannon2_black = Cannon("炮", "黑",(2,7))
        self.pawn1_red = Pawn("兵", "红",(6,0))
        self.pawn2_red = Pawn("兵", "红",(6,2))
        self.pawn3_red = Pawn("兵", "红",(6,4))
        self.pawn4_red = Pawn("兵", "红",(6,6))
        self.pawn5_red = Pawn("兵", "红",(6,8))
        self.pawn1_black = Pawn("卒", "黑",(3,0))
        self.pawn2_black = Pawn("卒", "黑",(3,2))
        self.pawn3_black = Pawn("卒", "黑",(3,4))
        self.pawn4_black = Pawn("卒", "黑",(3,6))
        self.pawn5_black = Pawn("卒", "黑",(3,8))
        self.blank = Chess()

    def output_map_black(self):
        for chess in self.chess:
            r = chess.position[0]
            c = chess.position[1]
            self.map[r][c]=chess
        self.map_Matrix_transposition()
        for row in self.map:
            for chess in row:
                print(chess,end=" ")
            print()
        self.map_Matrix_transposition()

    def output_map_red(self):
        for chess in self.chess:
            r = chess.position[0]
            c = chess.position[1]
            self.map[r][c]=chess
        for row in self.map:
            for chess in row:
                print(chess,end=" ")
            print()

    def start(self):
        while True:
            p = input("请输入阵营(r/b):").upper()
            if p == "R":
                self.output_map_red()
            elif p.upper() == "B":
                self.output_map_black()
            else:
                continue
            data = input("请输入操作(输入坐标即可):")
            p0,p1=data.split(" ")
            p0 = self.str_to_tuple(p0)
            p1 = self.str_to_tuple(p1)
            if not data:
                continue
            else:
                if p == "B":
                    p0 = (8-p0[0],8-p0[1])
                    p1 = (8-p1[0],8-p1[1])
                    print(p0,p1)
                self.map[p0[0]][p0[1]].position = p1
                self.map[p0[0]][p0[1]] = self.blank

    #将输入的字符串形式元组转化为元组
    def str_to_tuple(self,data):
        try:
            return tuple(map(int,data[1:-1].split(",")))
        except:
            return ()

    def map_Matrix_transposition(self):
        for line in self.map:
            line.reverse()
        self.map.reverse()


if __name__ == "__main__":
    manager = Manager()
    manager.start()