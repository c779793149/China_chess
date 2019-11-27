class Chess:  # 棋子类
    """
    吃子:只能吃敌方棋子,只要符合行棋方式.
    """

    def __init__(self, name="空", camp="白", position=(None, None)):
        """
        象棋棋子类
        :param name:棋子名
        :param camp: 棋子阵营
        :param position: 棋子坐标
        """
        self.name = name
        self.camp = camp
        self.position = position
        self.choice = []  # 棋子可选移动坐标,该坐标以二维列表索引为基准.
        # self.nearby = []  # 棋子附近的其他棋子

    def run(self):
        """
        走棋方式:执红先行,以红棋界面为基准
        """
        self.r = self.position[0]
        self.c = self.position[1]
        # print(self.r, self.c)
        self.choice.clear()  # 清空可移动位置列表
        # self.nearby.clear()  # 清空附近棋子列表

    def __str__(self):
        return self.camp + "-" + self.name


BLANK = Chess()  # 空白棋子对象
MAP = [[BLANK for i in range(9)] for j in range(10)]  # 用空白棋子初始化棋盘


class Rook(Chess):  # 车
    "车横冲直撞"

    def run(self):
        super(Rook, self).run()
        self.transverse_move(self.c + 1, 9)  # 筛选右侧可移动位置
        self.transverse_move(self.c - 1, -1, -1)  # 筛选左侧可移动位置
        self.Vertical_move(self.r + 1, 10)  # 筛选下侧可移动位置
        self.Vertical_move(self.r - 1, -1, -1)  # 筛选上侧可移动位置

    # 横移坐标筛选
    def transverse_move(self, begin, end, sep=1):
        for c in range(begin, end, sep):
            if MAP[self.r][c] != BLANK:  # 如果检测到有棋子
                # print("附近:", MAP[self.r][c], ":", MAP[self.r][c].position)
                if MAP[self.r][c].camp != self.camp:  # 如果棋子不是一个阵营
                    self.choice.append((self.r, c))  # 加入可移动位置
                break
            self.choice.append((self.r, c))

    # 竖移坐标筛选
    def Vertical_move(self, begin, end, sep=1):
        for r in range(begin, end, sep):
            if MAP[r][self.c] != BLANK:  # 如果检测到有棋子
                # print("附近:", MAP[r][self.c], ":", MAP[r][self.c].position)
                if MAP[r][self.c].camp != self.camp:  # 如果棋子不是一个阵营
                    self.choice.append((r, self.c))
                break
            self.choice.append((r, self.c))


class Knight(Chess):  # 马
    """
    马走"日"对角,当"日"字中间同侧有棋时,无法移动
    """

    def run(self):
        super(Knight, self).run()
        self.up_choice()
        self.down_choice()
        self.left_choice()
        self.right_choice()

    # 筛选上移位置
    def up_choice(self):
        if self.r - 2 < 0: return
        self.Vertical_move(self.r - 1, self.r - 2)

    # 筛选下移位置
    def down_choice(self):
        if self.r + 2 > 9: return
        self.Vertical_move(self.r + 1, self.r + 2)

    # 竖移坐标筛选
    def Vertical_move(self, a, b):
        if MAP[a][self.c] != BLANK: return
        if self.c - 1 > -1 and MAP[b][self.c - 1].camp != self.camp:
            self.choice.append((b, self.c - 1))
        if self.c + 1 < 9 and MAP[b][self.c + 1].camp != self.camp:
            self.choice.append((b, self.c + 1))

    # 筛选左移位置
    def left_choice(self):
        if self.c - 2 < 0: return
        self.transverse_move(self.c - 1, self.c - 2)

    # 筛选右移位置
    def right_choice(self):
        if self.c + 2 > 8: return
        self.transverse_move(self.c + 1, self.c + 2)

    # 横移坐标筛选
    def transverse_move(self, a, b):
        if MAP[self.r][a] != BLANK: return
        if self.r - 1 > 0 and MAP[self.r - 1][b].camp != self.camp:
            self.choice.append((self.r - 1, b))
        if self.r + 1 < 10 and MAP[self.r + 1][b].camp != self.camp:
            self.choice.append((self.r + 1, b))


class Elephant(Chess):  # 象/像
    """
    象走"田"对角,不能过河,当"田"字中间有棋时不能移动
    """

    def run(self):
        super(Elephant, self).run()
        self.assign_region()  # 需区分阵营,划定行棋区域(相/象不能过河)
        self.do_choice(-1, -1)  # 确认左上角是否可移动
        self.do_choice(1, -1)  # 确认右上角是否可移动
        self.do_choice(-1, 1)  # 确认左下角是否可移动
        self.do_choice(1, 1)  # 确认右下角是否可移动

    def assign_region(self):
        """
        分阵营初始化可移动行边界
        """
        if self.camp == "红":
            self.row_max = 9
            self.row_min = 5
        else:
            self.row_max = 4
            self.row_min = 0

    # 确认是否可移动
    def do_choice(self, abscissa, ordinate):
        """
        综合判断象/象是否可以移动
        :param abscissa: 横坐标,1表示右移,-1表示左移
        :param ordinate: 纵坐标,1表示下移,-1表示上移
        """
        if self.r + ordinate * 2 < self.row_min and ordinate == -1: return  # 判断上移的行
        if self.r + ordinate * 2 > self.row_max and ordinate == 1: return  # 判断下移的行
        if self.c + abscissa * 2 < 0 and abscissa == -1: return  # 判断左移的列
        if self.c + abscissa * 2 > 8 and abscissa == 1: return  # 判断右移的列
        if MAP[self.r + ordinate][self.c + abscissa] == BLANK:
            if MAP[self.r + ordinate * 2][self.c + abscissa * 2].camp != self.camp:
                self.choice.append((self.r + ordinate * 2, self.c + abscissa * 2))


class Mandarin(Chess):  # 士
    """
    士只能在九宫格的四角及中间以"口"字对角行棋
    """

    def run(self):
        super(Mandarin, self).run()
        self.assign_region()
        self.do_choice()

    def assign_region(self):
        """
        分阵营初步指定可选坐标
        """
        if self.camp == "红":
            self.choice[:] = [(8, 4), (9, 3), (9, 5), (7, 3), (7, 5)]
        else:
            self.choice[:] = [(1, 4), (0, 3), (0, 5), (2, 3), (2, 5)]

    def do_choice(self):
        # 如果当前位置不在九宫中心,那么可移动位置只能是九宫中心
        # 反之,除了同阵营占有,都可以移动
        if self.position != self.choice[0]:
            self.choice[:] = self.choice[0:1]
        for i in range(len(self.choice) - 1, -1, -1):
            if MAP[self.choice[i][0]][self.choice[i][1]].camp == self.camp:
                del self.choice[i]  # 如果阵营相同则不能移动


class Cannon(Chess):  # 炮
    """
    炮横冲直撞,隔山打牛.
    """

    def run(self):
        super(Cannon, self).run()
        self.transverse_move(self.c + 1, 9)  # 筛选右侧可移动位置
        self.transverse_move(self.c - 1, -1, -1)  # 筛选左侧可移动位置
        self.Vertical_move(self.r + 1, 10)  # 筛选下侧可移动位置
        self.Vertical_move(self.r - 1, -1, -1)  # 筛选上侧可移动位置

    # 左移或右移坐标筛选
    def transverse_move(self, begin, end, sep=1):
        for c in range(begin, end, sep):
            if MAP[self.r][c] != BLANK:  # 如果检测到有棋子
                for cc in range(c + sep, end, sep):
                    if MAP[self.r][cc] != BLANK:
                        if MAP[self.r][c].camp != self.camp:  # 如果棋子不是一个阵营
                            self.choice.append((self.r, cc))  # 加入可移动位置
                        break
                break
            self.choice.append((self.r, c))

    def Vertical_move(self, begin, end, sep=1):
        for r in range(begin, end, sep):
            if MAP[r][self.c] != BLANK:  # 如果检测到有棋子
                for rr in range(r + sep, end, sep):
                    if MAP[rr][self.c] != BLANK:
                        if MAP[rr][self.c].camp != self.camp:  # 如果棋子不是一个阵营
                            self.choice.append((rr, self.c))  # 加入可移动位置
                        break
                break
            self.choice.append((r, self.c))


class Pawn(Chess):  # 兵卒
    """
    兵卒死战不退,不入敌阵不横移
    """

    def run(self):
        super(Pawn, self).run()
        if self.camp == "红":
            self.red_choice()
        else:
            self.black_choice()

    # 红棋移动坐标筛选
    def red_choice(self):
        if self.r > 0:
            if MAP[self.r - 1][self.c].camp != self.camp:
                self.choice.append((self.r - 1, self.c))
        if self.r < 5:
            self.transverse_move()

    # 黑棋移动坐标筛选
    def black_choice(self):
        if self.r < 9:
            if MAP[self.r + 1][self.c].camp != self.camp:
                self.choice.append((self.r + 1, self.c))
        if self.r > 4:
            self.transverse_move()

    # 平移坐标筛选
    def transverse_move(self):
        if self.c > 0:
            if MAP[self.r][self.c - 1].camp != self.camp:
                self.choice.append((self.r, self.c - 1))
        if self.c < 8:
            if MAP[self.r][self.c + 1].camp != self.camp:
                self.choice.append((self.r, self.c + 1))


class King(Chess):  # 将/帅
    """
    输赢待定,先确认走棋方式
    将帅只能在九宫格内走直线,一次只能移动一格
    """

    def run(self):
        super(King, self).run()
        self.assign_region()
        self.do_choice()

    def assign_region(self):
        """
        分阵营初步指定可选坐标
        """
        if self.camp == "红":
            self.choice[:] = [
                (9, 3), (9, 4), (9, 5),
                (8, 3), (8, 4), (8, 5),
                (7, 3), (7, 4), (7, 5)
            ]
        else:
            self.choice[:] = [
                (0, 3), (0, 4), (0, 5),
                (1, 3), (1, 4), (1, 5),
                (2, 3), (2, 4), (2, 5)
            ]

    def do_choice(self):
        """
        删除九宫格内同意阵营棋子
        删除不在一条直线上的棋子
        删除距离二格的棋子
        """
        for i in range(len(self.choice) - 1, -1, -1):
            if MAP[self.choice[i][0]][self.choice[i][1]].camp == self.camp:
                del self.choice[i]
            elif self.choice[i][0] != self.r and self.choice[i][1] != self.c:
                del self.choice[i]
            elif self.choice[i][0] - self.r not in (1, -1) and \
                    self.choice[i][1] - self.c not in (1, -1):
                del self.choice[i]
