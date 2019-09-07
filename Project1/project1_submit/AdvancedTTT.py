# coding: utf-8
from __future__ import print_function
import string
import random
import time
import sys

class gameTTT:
    def __init__(self):
        self.board = [[" " for i in range(9)] for i in range(9)]
        
    def move(self,playx,playy,player):
        self.board[playx][playy]=player
    
    # test whether the board has a winner
    def game_win(self):
        for k in range(9):
            state = self.board[k]
            # check each row 
            for i in range(3):
                if [state[i*3],state[i*3+1],state[i*3+2]] in com_wins:
                    return 1000
                elif [state[i*3],state[i*3+1],state[i*3+2]] in hum_wins:
                    return -1000
            # check each column
            for i in range(3):
                if [state[i],state[i+3],state[i+6]] in com_wins:
                    return 1000
                elif [state[i],state[i+3],state[i+6]] in hum_wins:
                    return -1000
            # check diagonal line
            if [state[0],state[4],state[8]] in com_wins:
                return 1000
            elif [state[0],state[4],state[8]] in hum_wins:
                return -1000
            
            if [state[2],state[4],state[6]] in com_wins:
                return 1000
            elif [state[2],state[4],state[6]] in hum_wins:
                return -1000

        return False   
        
    def game_draw(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j]==" ":
                    return False
        # if the game ends in draw, return 1(differentiate it from 0, which will be regarded as False)
        return 1
        
    def terminal_state_test(self):
        if self.game_win():
            return self.game_win()
        elif self.game_draw():
            return self.game_draw()
        else:
            return False

def boarddisplay(state):
    for i in range(3):
        print("             |             |           ",file=sys.stderr)
        for j in range(3):
            print("  %s | %s | %s  |  %s | %s | %s  |  "
                  "%s | %s | %s  "%(state[i*3][j*3],state[i*3][j*3+1],state[i*3][j*3+2],
                                    state[i*3+1][j*3],state[i*3+1][j*3+1],state[i*3+1][j*3+2],
                                    state[i*3+2][j*3],state[i*3+2][j*3+1],state[i*3+2][j*3+2]),file=sys.stderr)
            if j < 2:
                print("-----------------------------------------",file=sys.stderr)
        print("             |             |           ",file=sys.stderr)
        if i < 2:
            print("-----------------------------------------",file=sys.stderr)


def initialgame():
    print("Let me know your choice: X(go first) or O(go second): ",file=sys.stderr)
    readin = sys.stdin
    readinline = readin.readline()
    human = readinline[0]
    human = human.upper()
    return human


def evaluation(gamemodel):
    # calculate each player's score
    computerscore = 0
    humanscore = 0
    for i in range(9):
        state = gamemodel.board[i]
            
        # check each row
        for j in range(3):
            if [state[j*3],state[j*3+1],state[j*3+2]] in com_2win:
                computerscore += 2
            elif [state[j*3],state[j*3+1],state[j*3+2]] in hum_2wins:
                humanscore += 2
            
        # check each column
        for j in range(3):
            if [state[j],state[j+3],state[j+6]] in com_2win:
                computerscore += 2
            elif [state[j],state[j+3],state[j+6]] in hum_2wins:
                humanscore += 2
            
        # check diagonal lines
        if [state[0],state[4],state[8]] in com_2win:
             computerscore += 2
        elif [state[0],state[4],state[8]] in hum_2wins:
            humanscore += 2
            
        if [state[2],state[4],state[6]] in com_2win:
             computerscore += 2
        elif [state[2],state[4],state[6]] in hum_2wins:
             humanscore += 2
    
    if (computerscore-humanscore)==0:
        return 1
    else:
        return (computerscore-humanscore)

def find_new_position(gamemodel):
    actions = []
    blanknumber = 0
    for i in range(9):
        for j in range(9):
            if gamemodel.board[i][j]==" ":
                blanknumber += 1
    while len(actions) < min(blanknumber,9):
        playx = random.choice(range(9))
        playy = random.choice(range(9))
        if gamemodel.board[playx][playy]==" ":
            actions.append([playx,playy])
            
    return actions

def minimax_decision(gamemodel,humanx,humany):
    
    def max_value(depth,gamemodel,playx,playy,alpha,beta):
        if gamemodel.terminal_state_test():
            return gamemodel.terminal_state_test()
        if depth > 6:
            return evaluation(gamemodel)      
        # find legal actions
        actions = []
        for i in range(9):
            if gamemodel.board[playy][i]==" ":
                actions.append([playy,i])
        if len(actions) == 0:
            actions = find_new_position(gamemodel) 
        move = [-1,-1]
        for i in range(len(actions)):
            gamemodel.board[actions[i][0]][actions[i][1]]=computer
            temp = min_value(depth+1,gamemodel,actions[i][0],actions[i][1],alpha,beta)
            if alpha < temp:
                alpha = temp
                move = [actions[i][0],actions[i][1]]
            if alpha >= beta:
                gamemodel.board[actions[i][0]][actions[i][1]]=" "
                return alpha
            gamemodel.board[actions[i][0]][actions[i][1]]=" "
        steps.append(move)
        return alpha
            
    def min_value(depth,gamemodel,playx,playy,alpha,beta):
        if gamemodel.terminal_state_test():
            return gamemodel.terminal_state_test()        
        if depth > 6:
            return evaluation(gamemodel)
        actions = []
        for i in range(9):
            if gamemodel.board[playy][i]==" ":
                actions.append([playy,i])
        if len(actions) == 0:
            actions = find_new_position(gamemodel)  
        for i in range(len(actions)):
            gamemodel.board[actions[i][0]][actions[i][1]]=human
            temp = max_value(depth+1,gamemodel,actions[i][0],actions[i][1],alpha,beta)
            if beta > temp:
                beta = temp
            if beta <= alpha:
                gamemodel.board[actions[i][0]][actions[i][1]]=" "
                return beta
            gamemodel.board[actions[i][0]][actions[i][1]]=" "
        return beta
    
    steps = []
    # if AI plays first, its first move is the center of the board
    if (humanx == -1):
        return [4,4]
    else:
        max_value(0,gamemodel,humanx,humany,-2000,2000)
        return steps.pop()


play = True
while play:
    human = initialgame()
    game = gameTTT()
    com_move=[-1,-1]
    first_step = -1
    sec_step = -1
    if human == "X":
        computer = "O"
        com_2win = [[computer,computer," "],[computer," ",computer],[" ",computer,computer]]
        hum_2wins = [[human,human," "],[human," ",human],[" ",human,human]]  
        com_wins = [[computer,computer,computer]]
        hum_wins = [[human,human,human]]
        boarddisplay(game.board)
        while not game.terminal_state_test():
            #boarddisplay(game.board)
            print("Please type two numbers in 1-9 to indicate the position you want to play: ",file=sys.stderr)
            readin = sys.stdin
            humanline = readin.readline().split(" ")
            first_step = int(humanline[0])
            sec_step = int(humanline[1])
            first_step -= 1
            sec_step -= 1

            # check whether the input is valid 
            if com_move[1]!= -1:
                while (first_step != com_move[1]) or (game.board[first_step][sec_step]!=" "):
                    print("The input is invalid, please type two new numbers in 1-9 to indicate the position you want to play: ",file=sys.stderr)
                    readin = sys.stdin
                    humanline = readin.readline().split(" ")
                    first_step = int(humanline[0])
                    sec_step = int(humanline[1])
                    first_step -= 1
                    sec_step -= 1
            
            game.move(first_step,sec_step,human)
            boarddisplay(game.board)
            if game.terminal_state_test():
                break
            
            # use H-MINIMAX function to get AI's move (calculate the performance at the same time)
            starttime = time.time()
            com_move = minimax_decision(game,first_step,sec_step)
            endtime = time.time()
            game.move(com_move[0],com_move[1],computer)
            print(com_move[0]+1,com_move[1]+1,file=sys.stdout)
            print("time cost:%.2f"%(endtime-starttime),file=sys.stderr)
            boarddisplay(game.board)
            if game.terminal_state_test():
                break
    else:
        computer = "X"
        com_2win = [[computer,computer," "],[computer," ",computer],[" ",computer,computer]]
        hum_2wins = [[human,human," "],[human," ",human],[" ",human,human]]  
        com_wins = [[computer,computer,computer]]
        hum_wins = [[human,human,human]]    
        while not game.terminal_state_test(): 
            starttime = time.time()
            com_move = minimax_decision(game,first_step,sec_step)
            endtime = time.time()
            game.move(com_move[0],com_move[1],computer)
            print(com_move[0]+1,com_move[1]+1,file=sys.stdout)
            print("time cost:%.2f"%(endtime-starttime),file=sys.stderr)
            #boarddisplay(game.board)
            if game.terminal_state_test():
                break
            
            boarddisplay(game.board)
            print("Please type two numbers in 1-9 to indicate the position you want to play: ",file=sys.stderr)
            readin = sys.stdin
            humanline = readin.readline().split(" ")
            first_step = int(humanline[0])
            sec_step = int(humanline[1])
            first_step -= 1
            sec_step -= 1
            
            # check whether the input is valid 
            if com_move[1]!= -1:
                while (first_step != com_move[1]) or (game.board[first_step][sec_step]!=" "):
                    print("The input is invalid, please type two new numbers in 1-9 to indicate the position you want to play: ",file=sys.stderr)
                    readin = sys.stdin
                    humanline = readin.readline().split(" ")
                    first_step = int(humanline[0])
                    sec_step = int(humanline[1])
                    first_step -= 1
                    sec_step -= 1

            game.move(first_step,sec_step,human)
            boarddisplay(game.board)
            if game.terminal_state_test():
                break

    if game.terminal_state_test() == -1000:
        print("You win",file=sys.stderr)
    elif game.terminal_state_test() == 1:
        print("Draw",file=sys.stderr)
    elif game.terminal_state_test() == 1000:
        print("Computer wins",file=sys.stderr)
