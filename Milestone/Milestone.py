# player1 = input("Please pick a marker 'X' or 'O'")
# player1 = int(input('Please enter a number:'))
# print(player1)
def WinnerScreen(board):
        print("\n" * 10)
        print(board[1] + "|" + board[2] + "|" + board[3])
        print(board[4] + "|" + board[5] + "|" + board[6])
        print(board[7] + "|" + board[8] + "|" + board[9])
        print("YOU WIN")
        exit()

def TieGame(board):
        print(board[1] + "|" + board[2] + "|" + board[3])
        print(board[4] + "|" + board[5] + "|" + board[6])
        print(board[7] + "|" + board[8] + "|" + board[9])
        print("IT A TIE")
        exit()

def display_board(board, player1, player2, player1Turn):
    player1Turn
    WIN = 0
    if player1Turn == 1:
        player1GoFlag = 1
    else:
        player1GoFlag = 0
    boardPlacement = 0
    board[0] = "W"
    while (WIN == 0):
        print(board[1] + "|" + board[2] + "|" + board[3])
        print(board[4] + "|" + board[5] + "|" + board[6])
        print(board[7] + "|" + board[8] + "|" + board[9])
        while boardPlacement not in range(1, 10):
            boardPlacement = int(input("Pick from 1 to 9:"))
            print(boardPlacement)
            print(type(boardPlacement))
        if player1GoFlag == 1:
            if not board[boardPlacement] != " ":
                board[int(boardPlacement)] = player1
                player1GoFlag = 0
            else:
                print(board[int(boardPlacement)])
                print("Already in use")
        else:
            if not board[boardPlacement] != " ":
                board[int(boardPlacement)] = player2
                player1GoFlag = 1
            else:
                print(board[int(boardPlacement)])
                print("Already in use")
        print("\n" * 10)
        boardPlacement = 0
        if board[1] == board[2] == board[3] != " ":
            WinnerScreen(board)
        elif board[4] == board[5] == board[6] != " ":
            WinnerScreen(board)
        elif board[7] == board[8] == board[9] != " ":
            WinnerScreen(board)
        elif board[1] == board[4] == board[7] != " ":
            WinnerScreen(board)
        elif board[2] == board[5] == board[8] != " ":
            WinnerScreen(board)
        elif board[3] == board[6] == board[9] != " ":
            WinnerScreen(board)
        elif board[1] == board[5] == board[9] != " ":
            WinnerScreen(board)
        elif board[3] == board[5] == board[7] != " ":
            WinnerScreen(board)
        elif " " not in board:
                TieGame(board)
        #print(board)

# test_board = ['#','X','O','X','O','X','O','X','O','X']
test_board = [" "] * 10
player1 = "X"
player2 = "Y"
player1Turn = 1
#display_board(test_board, player1, player2, player1Turn)

def playerPick():
        player1 = ""
        player2 = ""
        player1pos = 0
        player2pos = 0
        pos = 0
        while player1 not in ["x","o"]:
                player1 = input("Please pick a marker 'X' or 'O': ")
                if player1 == "x":
                        player1 = "X"
                        player2 = "O"
                else:
                        player1 = "O"
                        player2 = "X"
                        print("Player 1 = " + player1 )
                        print("Player 2 = " + player2)
                #while pos != 1 and pos != 2:
                while pos not in [1,2]:
                        pos = int(input('Please enter 1 or 2:'))
                        player1pos = pos
                if player1pos == 1:
                        player2pos = 2
                        print("Player 1 will go first")
                        print("Player 2 will go second")
                else:
                        player2pos = 1
                        print("Player 2 will go first")
                        print("Player 1 will go second")
                display_board(test_board, player1, player2, player1pos)

playerPick()