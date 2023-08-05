import random                                                                       #import random to the code

'''
1. If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
2. If N is even, puzzle instance is solvable if 
       -the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of 
         inversions is odd.
       -the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of 
         inversions is even.
3. For all other cases, the puzzle instance is not solvable.
'''

while True:
    print("----------welcome to Marcellus' puzzle----------")                           #print the opening for the puzzle
    while True:
        puzzledimension = input("please enter your dimension in range 3-10:")           #input the dimension level for the puzzle
        try:
            puzzledimension = int(puzzledimension)                                      #convert to integer
            if puzzledimension >= 3 and puzzledimension <= 10:
                break
            print("invalid input!!!\nplease enter between 3-10")
        except:                                                                         #prevention for improper input
            print("invalid input!!!\nplease enter between 3-10")

    def showtable():                                                                    #function for the puzzle's grid
        for i in range(puzzledimension):
            for j in range(puzzledimension):
                if table[i][j]==0:                                                      #convert number 0 in the puzzle to string " " (blank)
                    print(" ", end="\t")            
                else:
                    print(table[i][j], end="\t")
            print(" ")

    table = [None]*puzzledimension                                                      #generate table
    for i in range(puzzledimension):
        table[i] = [None]*puzzledimension
    while True:
        listnumber = random.sample(range(puzzledimension**2), puzzledimension**2)      #randomize the list number in puzzle
        number = 0
        index_x = 1                                                                    #Row
        index_y = 1                                                                    #Column
        for i in range(puzzledimension):
            for j in range(puzzledimension):
                table[i][j] = listnumber[number]                                      #generate puzzle
                if table[i][j] == 0:
                    index_x = i
                    index_y = j
                number += 1

        clone_list_number = listnumber[:]                                           #list for inversion
        clone_list_number.remove(0)
        invers_cnt = 0                                                              #inversion count
        for i in range(len(clone_list_number)):
            for j in range(i + 1, len(clone_list_number)):
                if clone_list_number[i] > clone_list_number[j]:
                    invers_cnt += 1
                else:
                    invers_cnt = invers_cnt

        if puzzledimension % 2 == 1 and invers_cnt % 2 == 0:                     #inversion is even and dimension odd           
            break
        elif puzzledimension % 2 == 0:                                           #inversion for even
            even_list = list(range(0, puzzledimension, 2))                       
            odd_list = list(range(1, puzzledimension, 2))
            if index_x in even_list and invers_cnt % 2 == 1:                    #the inversion is odd and blank in even
                break
            elif index_x in odd_list and invers_cnt % 2 == 0:                    #the inversion is even and blank in odd
                break
            else:                                                              #if unsolvable it will generate new puzzle
                continue
        else:
            continue
        break

    def left():                                                           #define left movement function
        global index_x, index_y
        if index_y==puzzledimension-1:
            return
        table[index_x][index_y], table[index_x][index_y+1] = table[index_x][index_y+1], table[index_x][index_y]
        index_y=index_y+1  

    def right():                                                         #define right movement function
        global index_x, index_y
        if index_y==0:
            return
        table[index_x][index_y], table[index_x][index_y-1] = table[index_x][index_y-1], table[index_x][index_y]
        index_y=index_y-1

    def down():                                                           #define down movement function
        global index_x, index_y
        if index_x==0:
            return
        table[index_x][index_y], table[index_x-1][index_y] = table[index_x-1][index_y], table[index_x][index_y]
        index_x=index_x-1

    def up():                                                             #define up movement function
        global index_x, index_y
        if index_x==puzzledimension-1:
            return
        table[index_x][index_y], table[index_x+1][index_y] = table[index_x+1][index_y], table[index_x][index_y]
        index_x=index_x+1

    l = input("Enter your keybind for left:")                            #input keybind for movement
    r = input("Enter your keybind for right:")
    d = input("Enter your keybind for down:")
    u = input("Enter your keybind for up:")

    keybind_dict = {l: left, r: right, d: down, u: up}                  #dictionary for keybind

    def check_table():                                                  #function to check if the puzzle is done
        check = 1
        for i in range(puzzledimension):
            for j in range(puzzledimension):
                if i == puzzledimension-1 and j == puzzledimension-1:
                    if table[i][j] == 0:
                        return True
                if table[i][j] != check:
                    return False
                check += 1

    movecount = 0   
    play_again = False             
    while True:
        showtable()
        move = input("Enter your movement:")
        if move in [l, r, d, u]:                                      #count movement
            keybind_dict[move]()
            movecount += 1
        elif move not in [l, r, d, u]:
            movecount == movecount
        else:
            print('Wrong key!!!')                                    #prevention for improper input
        if check_table():
            showtable()
            print("congratzzz!!! you just made it in " + str(movecount) +" move.\nFeel smart yet?")  #if the user complete the puzzle  
            while True:
                play_again = str(input('Do you want to play again?\npress p to play again or n to stop: '))  #ask the user if they want to play again
                if play_again == "p":                               #keyword to play again
                    play_again = True
                    break
                elif play_again == "n":                             #keyword to stop
                    play_again = False
                    break
                else:                                                #prevention for invalid input
                    print('Invalid input!!!')
            break
    if play_again == True:                                    #play the puzzle again
        continue
    elif play_again == False:                                    #stop the puzzle
        while True:
            feedback = str(input('Is it difficult?(yes/no) '))       #ask user feedback
            if feedback == 'no':                                 #if the user feel easy
                print("Great!!!!!")
                break
            elif feedback == 'yes':                              #if the user feel difficult
                print('You need more practice bro')
                break
            else:
                print('Invalid input!!!')                        #prevention for improper input
        break
    break
       
