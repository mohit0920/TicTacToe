def displayBoard(inputList):
    type1Str = '   |   |   '
    type2Str = '---+---+---'
    type3Str = ' |'
    space = ' '
    for i  in range(1,10):
       # print(type1Str)
        if i == 1 or i == 4 or i ==7 :
            print(type1Str)
            print(f'{space}{inputList[i]}',end = type3Str)
        elif i == 2 or i == 5 or i == 8 :
            print(f'{space}{inputList[i]}', end = space)
        else :
            print(type3Str[::-1], inputList[i])
            print(type1Str)
            if i != 9 :
                print(type2Str)
