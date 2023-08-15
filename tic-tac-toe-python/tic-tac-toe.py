from copy import deepcopy

def main():

    full('o','x')

def draw_board(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    # return board

def row_col(move):
    if (move >=7):
        row = 0
        col = move-7
        return row,col
    elif (move >= 4):
        row = 1
        col = move-4
        return row,col
    elif (move>=1):
        row = 2
        col = move -1
        return row,col


def end_game(board):
    # if count == 9:
    #     return [True,'Draw']
    end = False
    # rows
    for row in range(0,3):
        if (board[row][0] == board[row][1] == board[row][2]):
            end = True
            winner = board[row][0]
            return [True,winner]
    # cols
    for col in range(0,3):
        if (board[0][col] == board[1][col] == board[2][col]):
            end = True
            winner = board[0][col]
            return [True,winner]
    # diags
    if ((board[0][0] == board[1][1] == board[2][2]) or board[0][2] == board[1][1] == board[2][0]):
        return [True,board[1][1]]
    elif len(available_moves(board))==0:
        return [True,'Draw']
    else:
        return [False,None]

def legal_move(board,move):
    row,col = row_col(move)
    if type(board[row][col]) is int:
        return True
    else:
        return False

def make_move(board,move,player):
    row,col = row_col(move)
    board[row][col] = player

def game(board,p1,p2,count):
    # draw_board(board)
    if count %2 == 0:
        player = p1
        print('Player ' + player + ' pick number from board')
        move = int(input())
        row,col = row_col(move)
        if legal_move(board,move):
            make_move(board,move,player)
            # return game(board,p1,p2,count)
            # return 0
        else:
            print('Pick another number : ')
            return game(board,p1,p2,count)
    else:
        player = p2
        move = minimax(board,True)[1]
        # print(move)
        make_move(board,move,player)
        # return 0


def available_moves(board):
    available = []
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != 'o' and board[i][j] != 'x':
                available.append(board[i][j])
    return available


def eval(board):
    winner,outcome = end_game(board)
    if winner and outcome=='x':
        return 1
    if winner and outcome == 'o':
        return -1
    # elif winner and outcome == 'Draw':
        # return 0
    else:
        return 0


def minimax(board,max):
    if end_game(board)[0]:
        return [eval(board),None]
    if max:
        # curr_count = count
        best_value = -1000000
        best_move = None
        available =  available_moves(board)
        for move in available:
            new_board = deepcopy(board)
            make_move(new_board,move,'x')
            hypothetical_value = minimax(new_board,False)[0]
            if hypothetical_value > best_value:
                best_value = hypothetical_value
                best_move = move
        # print('best move+value = ' + str(best_move )+ ' + ' + str(best_value))
        return [best_value,best_move]
    else:
        best_value = 1000000
        best_move = None
        available = available_moves(board)
        for move in available:
            new_board = deepcopy(board)
            make_move(new_board,move,'o')
            hypothetical_value = minimax(new_board,True)[0]
            if hypothetical_value < best_value:
                best_value = hypothetical_value
                best_move = move
                # print(best_move)
        return [best_value,best_move]

def full(p1,p2):
    count = 0
    winner = False
    board = [[7,8,9],[4,5,6],[1,2,3]]
    while count < 10 and not winner:
        draw_board(board)
        game(board,p1,p2,count)
        winner,outcome = end_game(board)
        count +=1
    if winner and outcome!='Draw':
        draw_board(board)
        print('Player '+ outcome + 'Wins')
    elif winner and outcome=='Draw':
        draw_board(board)
        print("It's a Draw")
    # elif count ==10 or not winner:
    #     draw_board(board)
    #     print('Draw')


# def evaluate_board(board):
main()

# print(minimax([['x',8,'x'],[4,5,6],[1,2,3]],True)[1])



