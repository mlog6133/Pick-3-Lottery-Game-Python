'''
NAME : Marquis Logan


DATE : November 14, 2022


DESC : This python module shall receive user input and the computer will select a random integer that shall be compared
between the two. If the numbers are similar then the user will receive a prize contingent upon how many correct numbers

'''
#defined function the runs the whole game
def pay():
    # computer random integer choice 
    import random
    comp1 = str(random.randint(0,9))
    comp2 = str(random.randint(0,9))
    comp3 = str(random.randint(0,9))
    m = comp1 + comp2 + comp3
    
    # Lottery Menu
    print()
    print('-------------------------------------------------')
    print("--- Virginia State University's Lottery Menu! ---")
    print('-------------------------------------------------')
    print('')
    ch = input("Please select ANY 3 digit number for your Pick 3 Lottery selection! (Enter 4 to quit program): ")
    
    # Quit option
    if ch == '4':
        print("You've quit :////")
        print('Thanks for playing!')
        
        return False
    
    #Pick 3 Lottery Game
    list(m)
    list(ch)
    a = list(set(m) & set(ch))
    if len(a) == 1:
        print(f" You've won $1, Computer selected {m} and you selected {ch}")
    elif len(a) == 2:
        print(f" You've won $50, Computer selected {m} and you selected {ch}")
    elif len(a) == 3:
        print(f"You've won $100, Computer selected {m} and you selected {ch}")
    elif ch[0:3] == m[0:3]:
        print(f"Holy Jackpot! You've won $10,000! You both selected {ch}")
    else:
        print(f' You lost! Computer selected {m} and you selected {ch}, try again!')
   

               
    return True


#Calling the function
pay()



#loop to run function infinitely replays
# unless user selects 4 to end loop
while pay():
    pass

        



