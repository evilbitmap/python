import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
board = ['.' for i in range(9)]
poziceHrace = {'X':[], 'O':[]}
turn = 'O'
count = 9

def printboard(board):

    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print(" {} | {} | {}".format(board[0], board[1], board[2]))

def game(turn):
    while True:
        #printe board a vypíše kdo hraje
        printboard(board)
        print(f"turn: {turn}")
        if ZkontrolujVyhru(poziceHrace, turn):
            winner()

        #user input
        move = int(input())
        #vymaže konzoli
        clearConsole()
        #pokud je políčko volné tak zadej do políčka kdo hraje a pokud tam něco je tak zabrané
        if board[move-1] == '.':
            board[move-1] = turn
            #updatuje pozice hrace
            poziceHrace[turn].append(move)
            #při každém tahu hraje další
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            print("spot taken")

def winner():
    clearConsole()
    printboard(board)
    print(f"{turn}: vyhrál")

def ZkontrolujVyhru(poziceHrace, turn):
    poziceProVyhru = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for x in poziceProVyhru:
        if all(y in poziceHrace[turn] for y in x):
            return True
    return False
    



def main():
    game(turn)

if __name__ == "__main__":
    main()
