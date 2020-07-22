import random,sys
board=[[1,2,3],
       [4,"X",6],
       [7,8,9]]
l=[]
counter=0
def EnterMove(board):
    dict={}
    move=eval(input("Enter your move: "))
    if type(move)!=type(1) or move not in range(1,10):
        print("Move Invalid")
        return
    lf=[]
    for f in l:
        lf.append((board[f[0] - 1][f[1] - 1]))
    if move not in lf:
        print("Place already occupied")
        return
    for x in range(len(l)):
        dict[lf[x]]=l[x]
    board[dict[move][0]-1][dict[move][1]-1]="O"
    global counter
    counter += 1
    DisplayBoard(board)

def DrawMove(board):
    dict={}
    lf = []
    for f in l:
        lf.append((board[f[0] - 1][f[1] - 1]))
    for x in range(len(l)):
        dict[lf[x]]=l[x]
    move=random.choice(lf)
    board[dict[move][0] - 1][dict[move][1] - 1] = "X"
    global counter
    counter+=1
    DisplayBoard(board)
def MakeListOfFreeFields(board):
    l.clear()
    for x in range(3):
        for y in range(3):

            if type(board[x][y]) == type(1):
                l.append((x + 1, y + 1))
    if counter==8:
        print("It is a tie")
        sys.exit()
    if counter in [0,2,4,6]:
        EnterMove(board)
    else:
        DrawMove(board)

def VictoryFor(board):
    # row surfing
    for x in board:
        X,O = 0,0
        for y in x:
            if y == "X":
                X += 1
            if y == "O":
                O += 1
        if X == 3 or O == 3:
            if X==3:
                return "Computer has won"
            else:
                return "You have won"
# column surfing
    for y in range(3):
        X,O = 0,0
        for x in range(3):
            if board[x][y] == "X":
                X += 1
            if board[x][y] == "O":
                O += 1
        if X == 3 or O == 3:
            if X==3:
                return "Computer has won"
            else:
                return "You have won"

# diagnol surfing(l-r)
    X,O = 0,0
    for x, y in (0, 0), (1, 1), (2, 2):
        if board[x][y] == "X":
            X += 1
        if board[x][y] == "O":
            O += 1
        if X == 3 or O == 3:
            if X==3:
                return "Computer has won"
            else:
                return "You have won"
# diagnol surfing(r-l)
    X,O = 0,0
    for x, y in (2, 0), (1, 1), (0, 2):
        if board[x][y] == "X":
            X += 1
        if board[x][y] == "O":
            O += 1
        if X == 3 or O == 3:
            if X == 3:
                return "Computer has won"
            else:
                return "You have won"

def DisplayBoard(board):
    (a, b, c), (d, e, f), (g, h, i) = board[0], board[1], board[2]
    for y in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        if y == 0:
            print("|   {}   |   {}   |   {}   |".format(a, b, c))
        elif y == 1:
            print("|   {}   |   {}   |   {}   |".format(d, e, f))
        else:
            print("|   {}   |   {}   |   {}   |".format(g, h, i))
        print("|       |       |       |")
    print("+-------+-------+-------+")
    statement=VictoryFor(board)
    if statement!=None:
        print(statement)
        sys.exit()
    MakeListOfFreeFields(board)

DisplayBoard(board)




