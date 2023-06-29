print('Welcome to Tic-Tac-Toe, Type X or O for your command followed with the location in the grid in the following \n'
      'manner. The Rows are arranged in A,B,C and columns in 1,2,3. So if you want to play in the first row and second'
      '\ncolumn, be sure to type B2!\n')

Row1 = ['A1', 'A2', 'A3']
Row2 = ['B1', 'B2', 'B3']
Row3 = ['C1', 'C2', 'C3']
usedGrid = []
prevIn = ''
counter = 0
acceptableVal = ['X', 'O']


def Display():
    print(Row1[0], '|', Row1[1], '|', Row1[2], )
    print(Row2[0], '|', Row2[1], '|', Row2[2], )
    print(Row3[0], '|', Row3[1], '|', Row3[2], )


def playerInput():
    ival = input('Enter your Symbol: ').upper()
    if ival not in acceptableVal:
        return 'Invalid'
    return ival


def gridInput():
    gval = input('Enter grid position: ').upper()
    print(gval)
    if gval in usedGrid:
        return 'Fail'
    usedGrid.append(gval)
    return gval


def ARow(RC):
    for val in range(3):
        if Row1[val] == gridval:
            Row1[val] = pval
            break


def BRow(RC):
    for val in range(3):
        if Row2[val] == gridval:
            Row2[val] = pval
            break


def CRow(RC):
    for val in range(3):
        if Row3[val] == gridval:
            Row3[val] = pval
            break


def WinningCheck():
    if Row1[0] == Row1[1] == Row1[2]:
        return 'W'
    if Row2[0] == Row2[1] == Row3[2]:
        return 'W'
    if Row3[0] == Row3[1] == Row3[2]:
        return 'W'
    if Row1[0] == Row2[0] == Row3[0]:
        return 'W'
    if Row1[1] == Row2[1] == Row3[1]:
        return 'W'
    if Row1[2] == Row2[2] == Row3[2]:
        return 'W'
    if Row1[0] == Row2[1] == Row3[2]:
        return 'W'
    if Row1[2] == Row2[1] == Row3[0]:
        return 'W'
    return 'GC'


while True:
    if counter == 9:
        Display()
        print(prevIn,'wins')
        break
    Display()

    pval = playerInput()

    if pval == prevIn:
        print('The same player cannot go Twice')
        continue

    if pval == 'Invalid':
        print('Enter either X or O')
        continue

    prevIn = pval

    gridval = gridInput()
    if gridval == 'Fail':
        print('Position in use. Go again')
        continue

    if gridval.startswith('A'):
        ARow(gridval)

    if gridval.startswith('B'):
        BRow(gridval)

    if gridval.startswith('C'):
        CRow(gridval)

    status = WinningCheck()
    counter += 1
    if status == 'W':
        print(prevIn,'Wins!')
        break
    print("Next player's turn")
