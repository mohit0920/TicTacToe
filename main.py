def displayBoard(inList):
    '''It  display board every time after input in represntation.'''
    type1Str = '   |   |   '
    type2Str = '---+---+---'
    type3Str = ' |'
    space = ' '
    print("\n\n")
    for i  in range(1,10):
       # print(type1Str)
        if i == 1 or i == 4 or i ==7 :
            print(type1Str)
            print(f'{space}{inList[i]}',end = type3Str)
        elif i == 2 or i == 5 or i == 8 :
            print(f'{space}{inList[i]}', end = space)
        else :
            print(type3Str[::-1], inList[i])
            print(type1Str)
            if i != 9 :
                print(type2Str)
    print("\n\n")

def play():
    '''Main leading Function where execution starts it includes  all global variable declaration and Introduction of game.'''
    global inputList 
    global flag
    flag = False
    inputList = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('Welcome To Tic Tac Toe Game :')
    print("You have to give  input using number from 1 to 9 & positions for these numbers on board is as shown :-")
    demoList = ['#',1,2,3,4,5,6,7,8,9]
    displayBoard(demoList)
    print("Player 1 :- ")
    choicePlayer1 = input("Would you like to play with X or with O. Enter your Choice :- \n")
    if choicePlayer1.upper() == 'X':
        print("You Have Chosen X. So You Will go first.")
        playerInput(1,'X')
    elif choicePlayer1.upper() == 'O':
        print("You Have Chosen O. So player 2 Will Go First.")
        playerInput(2,'X')
    else :
        print("Invalid Choice. Enter A Valid Choice :-")
        play()

def playerInput(playerNumber,choice):
    '''function used to take inputs from player '''
    global flag
    print(f"Player {playerNumber} :-")
    pos = int(input("Enter You choice from numpad[1-9] according to position shown before :- \n"))
    if pos <1 or pos > 9:
        print("invalid position!")
        playerInput(playerNumber,choice)
    elif inputList[pos] != ' ':
        print("Already A Symbol Here!")
        playerInput(playerNumber,choice)
    else :
        inputList[pos] = choice
        displayBoard(inputList)
        winCheck(playerNumber,choice)
        if flag :
            replay = input("Would You like to Replay ! \n Enter Y if you like to replay, or hit Enter to exit :- ")
            if replay.upper() == 'Y':
                play()
                flag = False
           # if replay == '' :
            print("Good Bye!!!")
            exit()
            
def winCheck(playerNumber,choice):
    '''function used to check if any user wins ot it's a tie'''
    possibleWins = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    global flag
    global inputList
    for item in possibleWins :
        if (inputList[item[0]] == inputList[item[1]]) and (inputList[item[1]] == inputList[item[2]]) and ( inputList[item[2]] != ' ' ) :
            print(f"\n\n\n*** Player {playerNumber} wins !. *** \n With choice {choice} look at positions {item[0]}, {item[1]}, {item[2]} on Board. ")
            flag = True
    if not ' ' in inputList :
        displayBoard(inputList)
        print("\n\n\n *** It's a tie ! *** \n No space left")
        flag = True
        replay = input("Would You like to Replay ! \n Enter Y if you like to replay, or hit Enter to exit :- ")
        if replay.upper() == 'Y':
            play()
            flag = False
        print("Good Bye!!!")
        exit()
    if not flag :
        if choice == 'X':
            newChoice = 'O'
        else :
            newChoice = 'X'
        if playerNumber == 1:
            newPlayer = 2
        else :
            newPlayer = 1
        playerInput(newPlayer, newChoice)

play() #Calls the main play function to start execution 

