#! /usr/bin/env python
# -*- coding:utf-8 -*-

#用户行为 上下左右重置 退出用actions表示
#actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
#考虑大写情况
#letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
#关联输入与行为
#actions_dict = dict(zip(letter_codes, actions * 2))
#
#状态机
def main(stdscr):

    def init():
#重置游戏棋盘
    return 'Game'

    def not_game(state):
#画出 Gameover 或者 Win的界面
#读取用户输入得到action，判断是否重启游戏还是结束游戏
    responses = defaultdict(lambda: state)#默认是当前状态，没有行为就会一直在当前界面循环
    responses['Restart0'], response['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
    return responses[action]

    def game():
#画出当前棋盘状态
#读取用户输入得到action
    if action == 'Restart':
        return 'Init'
    if action == 'Exit':
        return 'Exit'
#if 成功移动了一部：
        if gamewin:
            return 'Win'
        if gameover:
            return 'Gameover'
    return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    state = 'Init'

#状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()

#用户输入处理
def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = =keyboard.getch()
    return actions_dict[char]

#矩阵转置与矩阵逆转0

#zuo
def transpose(field):
    return [list(row) for row in zip(*field)]
#you
def invert(field):
    return [row[::-1] for row in field]

#创建棋盘
    class GameField(object):
        def __init__(self, height=4, width=4, win=2048):
            self.height = height
            self.width = width
            self.win_value = 2048
            self.score = 0
            self.highscore = 0
            self.reset()

#棋盘操作
def spawn(self):
    new_element = 4 if randrange(100) > 89 else 2
    (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
    self.field[i][j] = new_element

