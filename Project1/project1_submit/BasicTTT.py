
# coding: utf-8

from __future__ import print_function
import string
import time
import sys


class gameTTT:
    def __init__(self):
        self.board = [" " for i in range(9)]

    def move(self, number, player):
        self.board[number] = player

        # check whether any player wins the game
    def win(self):
        state = self.board
        # check rows
        for i in range(3):
            if state[i * 3] == state[i * 3 + 1] and state[i * 3 + 1] == state[i * 3 + 2] and state[i * 3] != " ":
                if state[i * 3] == human:
                    return 1  # computer loses
                else:
                    return 3  # computer wins
        # check columns
        for i in range(3):
            if state[i] == state[i + 3] and state[i + 3] == state[i + 6] and state[i] != " ":
                if state[i] == human:
                    return 1  # computer loses
                else:
                    return 3  # computer wins
        # check diagonal lines
        if state[0] == state[4] and state[4] == state[8] and state[0] != " ":
            if state[0] == human:
                return 1  # computer loses
            else:
                return 3  # computer wins
        if state[2] == state[4] and state[4] == state[6] and state[2] != " ":
            if state[2] == human:
                return 1  # computer loses
            else:
                return 3  # computer wins
        return False

    # check whether the game ends in draw
    def draw(self):
        for i in range(9):
            if self.board[i] == " ":
                return False
        return 2

    def terminal_test(self):
        if self.win():
            return self.win()
        elif self.draw():
            return self.draw()
        else:
            return False


def boarddisplay(state):
    for i in range(3):
        print(" %s | %s | %s " % (state[i * 3], state[i * 3 + 1], state[i * 3 + 2]), file=sys.stderr)
        if i < 2:
            print("-----------", file=sys.stderr)
    print("\n", file=sys.stderr)


def initialgame():
    print("Let me know your choice: X(go first) or O(go second): ", file=sys.stderr)
    readin = sys.stdin
    readinline = readin.readline()
    human = readinline[0]
    human = human.upper()
    return human

def minimax_decision(gamemodel):
    def max_value(gamemodel):
        if gamemodel.terminal_test():
            return gamemodel.terminal_test()
        # find possible moves
        actions = []
        for i in range(9):
            if gamemodel.board[i] == " ":
                actions.append(i)
        v = -1000
        move = -1
        for i in range(len(actions)):
            gamemodel.board[actions[i]] = computer
            temp = min_value(gamemodel)
            if v < temp:
                v = temp
                move = actions[i]
            gamemodel.board[actions[i]] = " "
        steps.append(move)
        return v

    def min_value(gamemodel):
        if gamemodel.terminal_test():
            return gamemodel.terminal_test()
        actions = []
        for i in range(9):
            if gamemodel.board[i] == " ":
                actions.append(i)
        v = 1000
        for i in range(len(actions)):
            gamemodel.board[actions[i]] = human
            temp = max_value(gamemodel)
            if v > temp:
                v = temp
            gamemodel.board[actions[i]] = " "
        return v

    steps = []
    max_value(gamemodel)
    return steps.pop()


play = True
while play:
    human = initialgame()
    game = gameTTT()
    if human == "X":
        computer = "O"
        boarddisplay(game.board)
        while not game.terminal_test():
            #boarddisplay(game.board)
            print("Please type a number in 1-9: ", file=sys.stderr)
            readin = sys.stdin
            readinline = readin.readline()
            h_move = int(readinline[0]) - 1


            if h_move < 0 or h_move > 9:
                print("Invalid Input, Please type a new number in 1-9: ", file=sys.stderr)
                readin = sys.stdin
                readinline = readin.readline()
                h_move = int(readinline[0]) - 1


            while game.board[h_move] != " ":
                print("Invalid Input, Please type a new number in 1-9: ", file=sys.stderr)
                readin = sys.stdin
                readinline = readin.readline()
                h_move = int(readinline[0]) - 1
            game.move(h_move, human)
            boarddisplay(game.board)
            if game.terminal_test():
                break
            # use MINIMAX function to get AI's move (calculate the performance at the same time)
            starttime = time.time()
            c_move = minimax_decision(game)
            endtime = time.time()
            game.move(c_move, computer)
            print(c_move + 1, file=sys.stdout)
            print("time cost:%.2f" % (endtime - starttime), file=sys.stderr)
            boarddisplay(game.board)
            if game.terminal_test():
                break
    else:
        computer = "X"
        while not game.terminal_test():
            starttime = time.time()
            c_move = minimax_decision(game)
            endtime = time.time()
            game.move(c_move, computer)
            print(c_move + 1, file=sys.stdout)
            print("time cost:%.2f" % (endtime - starttime), file=sys.stderr)
            boarddisplay(game.board)
            if game.terminal_test():
                break
            #boarddisplay(game.board)
            print("Please type a number in 1-9: ", file=sys.stderr)
            readin = sys.stdin
            readinline = readin.readline()
            h_move = int(readinline[0]) - 1
            while game.board[h_move] != " ":
                print("Invalid Input, Please type a new number in 1-9: ", file=sys.stderr)
                readin = sys.stdin
                readinline = readin.readline()
                h_move = int(readinline[0]) - 1
            game.move(h_move, human)
            boarddisplay(game.board)
            if game.terminal_test():
                break

    if game.terminal_test() == 1:
        print("You win", file=sys.stderr)
    elif game.terminal_test() == 2:
        print("Draw", file=sys.stderr)
    elif game.terminal_test() == 3:
        print("Computer wins", file=sys.stderr)