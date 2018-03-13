'''
Created on Nov 5, 2017

@author: bill
'''

# Initialize Board

board = [[0,0,0],[0,0,0],[0,0,0]]
win = False

def gen_board ():
    """
    Requires no arg.
    Output is to Consol for a 3 x 3 matrix used in Tic-Tac-Toe
    """
    for r in board:
        print(r[0], '  ',r[1], '  ', r[2])
 
def move (x,y,player):
    """
    Requires arg1 for selected row, arg2 for selected column and arg3 for player ID
    places player ID on row/column for turn
    Null return
    """
    board[x-1][y-1] = player
    return

def check_err(x,y):
    """
    Requires arg1 for selected row and arg2 for selected column
    Checks whether selected move is to a location that has already been selected in a prior turn.
    Returns "False" for element is blank; "True" if element is used in prior turn.
    """
    if board[x-1][y-1] == 0:
        return False
    else:
        return True

def check_win():
    """
    Requires no arg.
    Checks for status of matrix and sets variable win = True if there is a winning array configuration for Tic-Tac-Toe
    Returns Null
    """
    global win
    for r in board:
        if r == ['X','X','X'] or r == ['O','O','O']: #checking horizontal win
            win = True
            gen_board()
            print('WE HAVE A WINNER!!!')
            break
        elif (board[0][0] and board[1][1] and board [2][2]) == ("X" or "O"): #checking diagonal win
            win = True
            gen_board()
            print('WE HAVE A WINNER!!!')
            break
        elif (board[0][2] and board[1][1] and board [2][0]) == ("X" or "O"): #checking diagonal win
            win = True
            gen_board()
            print('WE HAVE A WINNER!!!')
            break
        elif ((board[0][0] and board[1][0] and board [2][0]) == ("X" or "O")) or ((board[0][1] and board[1][1] and board [2][1]) == ("X" or "O")) or ((board[0][2] and board[1][2] and board [2][2]) == ("X" or "O")): #checkign vertical win
                    win = True
                    gen_board()
                    print('WE HAVE A WINNER!!!')
        else:
            for i in range(3):
                for j in range (3):
                    if board[i][j] == 0:
                        open_spot = True
                    else:
                        open_spot = False
            if open_spot == False:
                win = True
                gen_board()
                print('Nobody Won... :-(')
 
while win == False:
    gen_board()
    player = 'D'
    x = 10
    y = 10
    while player not in {'X', 'O'}:
        player = (input("Please indicate X or O: ").upper())
    while x not in {1,2,3}:
        x = int(input("Please indicate row: "))
    while y not in {1,2,3}:
        y = int(input("Please indicate column: "))
    if check_err(x,y):
        print("You may only place an 'X' or an 'O' in an empty (0) space!")
    else:
        move(x,y,player)
        check_win()
        
