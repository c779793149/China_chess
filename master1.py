from chess import *


class Manager:
    def __init__(self):
        self.create_chess()
        self.map = [
            [self.rook1_red,
             self.knight1_red,
             self.ele1phant1_red,
             self.mandarin1_red,
             self.king,
             self.ele1phant2_red,
             self.ele1phant2_red,
             self.knight2_red,
             self.rook2_red
             ],
            [self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess
             ],
            [self.chess,
             self.cannon1_red,
             self.chess,
             self.chess,self.chess,
             self.chess,self.chess,
             self.cannon2_red,
             self.chess
             ],
            [self.pawn1_red,
             self.chess,
             self.pawn2_red,
             self.chess,
             self.pawn3_red,
             self.chess,
             self.pawn4_red,
             self.chess,
             self.pawn5_red
             ],
            [self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess
             ],
            [self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess
             ],
            [self.pawn1_black,
             self.chess,
             self.pawn2_black,
             self.chess,
             self.pawn3_black,
             self.chess,
             self.pawn4_black,
             self.chess,
             self.pawn5_black
             ],
            [self.chess,
             self.cannon1_black,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.cannon2_black,
             self.chess
             ],
            [self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess,
             self.chess
             ],
            [self.rook1_black,
             self.knight1_black,
             self.ele1phant1_black,
             self.mandarin1_black,
             self.general,
             self.mandarin2_black,
             self.ele1phant2_black,
             self.knight2_black,
             self.rook2_black
             ]
        ]

    def create_chess(self):
        self.rook1_red = Rook("车", "红")
        self.rook2_red = Rook("车", "红")
        self.rook1_black = Rook("车", "黑")
        self.rook2_black = Rook("车", "黑")
        self.knight1_red = Knight("马", "红")
        self.knight2_red = Knight("马", "红")
        self.knight1_black = Knight("马", "黑")
        self.knight2_black = Knight("马", "黑")
        self.ele1phant1_red = Elephant("相", "红")
        self.ele1phant2_red = Elephant("相", "红")
        self.ele1phant1_black = Elephant("象", "红")
        self.ele1phant2_black = Elephant("象", "红")
        self.mandarin1_red = Mandarin("士", "红")
        self.mandarin2_red = Mandarin("士", "红")
        self.mandarin1_black = Mandarin("士", "黑")
        self.mandarin2_black = Mandarin("士", "黑")
        self.general = King("帅", "红")
        self.king = King("帅", "黑")
        self.cannon1_red = Cannon("炮", "红")
        self.cannon2_red = Cannon("炮", "红")
        self.cannon1_black = Cannon("炮", "黑")
        self.cannon2_black = Cannon("炮", "黑")
        self.pawn1_red = Pawn("兵", "红")
        self.pawn2_red = Pawn("兵", "红")
        self.pawn3_red = Pawn("兵", "红")
        self.pawn4_red = Pawn("兵", "红")
        self.pawn5_red = Pawn("兵", "红")
        self.pawn1_black = Pawn("卒", "黑")
        self.pawn1_black = Pawn("卒", "黑")
        self.pawn2_black = Pawn("卒", "黑")
        self.pawn3_black = Pawn("卒", "黑")
        self.pawn4_black = Pawn("卒", "黑")
        self.pawn5_black = Pawn("卒", "黑")
        self.chess = Chess()

    def start(self):
        for line in self.map:
            for item in line:
                print(item,end=" ")
            print()

if __name__ == "__main__":
    manager = Manager()
    manager.start()