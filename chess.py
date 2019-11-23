class Chess:
    def __init__(self,name="空",camp="白",position=None):
        self.name = name
        self.camp = camp
        self.position = position
        self.r = self.position[0]
        self.c = self.position[1]

    def run(self):
        pass

    def eat(self):
        pass

    def __str__(self):
        return self.camp + "-" + self.name

class Rook(Chess):
    def run(self):
        for r in range(self.r-1,-1):
            pass
        for r in range(self.r+1,9)
            pass
        for c in range()

    def eat(self):
        pass

class Knight(Chess):
    pass
class Elephant(Chess):
    pass

class Mandarin(Chess):
    pass

class King(Chess):
    pass

class Cannon(Chess):
    pass

class Pawn(Chess):
    pass


# def main():
#     map = [
#     ["车","马","相","士","帅","士","相","马","车"],
#     ["","","","","","","","","","","","",],
#     ["","炮","","","","","","炮",""],
#     ["卒","","卒","","卒","","卒","","卒"],
#     ["","","","","","","","",""],
#     ["","","","","","","","",""],
#     ["卒","","卒","","卒","","卒","","卒"],
#     ["","炮","","","","","","炮",""],
#     ["","","","","","","","",""],
#     ["车","马","象","士","将","士","象","马","车"]
# ]
#
#     for line in map:
#         for item in line:
#             print(item,end="\t")
#         print()
