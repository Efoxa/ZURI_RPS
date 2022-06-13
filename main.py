from copy import error
import random


def user_choice():
    user_option = input('Choose R, P or S: ')
    if user_option in ['ROCK', 'rock', 'r', 'R']:
        user_option = 'rock'

    elif user_option in ['PAPER', 'paper', 'p', 'P']:
        user_option = 'paper' 

    elif user_option in ['SCISSORS', 'scissors', 's', 'S']:
        user_option = 'scissors'

    else:
        print(error)

        user_choice()

    return user_option   

def comp_choice():
    possible_choice = ['rock', 'paper', 'scissors']
    comp_option = random.choice(possible_choice)
    return comp_option

while True:
    print('')    
    user_option = user_choice()
    comp_option = comp_choice()
    print(f'\nPLAYER ({user_option}) : CPU ({comp_option}).\n')

    if  user_option == comp_option:
        print(f"Both players selected ({user_option}). It's a tie!")

    elif user_option == 'rock':
        if comp_option == 'scissors':
            print('PLAYER WIN!')

        else:
            print('CPU WIN!')

    elif user_option == "paper":
        if comp_option == 'rock':
            print('PLAYER WIN!')

        else:
            print('CPU WIN!')

    elif user_option == 'scissors':
        if comp_option == 'paper':
            print('PLAYER WIN!')

        else:
            print('CPU WINS!')

    user_option = input('Do you want to play again? (yes/no) ')
    if user_option in ['Y', 'YES', 'yes', 'y']:
        pass 
    elif user_option in ['N', 'NO', 'n', 'no']:
        break
    else:
        break

