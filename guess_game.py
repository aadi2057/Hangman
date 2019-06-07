import os, sys, time

def clear_screen():
    """
    This function clears the screen.
    """
    os.system('cls')


print('\n\n\n\n\n\n\n','..........Welcome to Hangman game.........'.center(100,' '))
print('\n\n\nGame Instructions:','\nYou need to guess a word. you can make a maximum of 10 wrong guess.')
input('Press Enter to conitnue.....')
clear_screen()
word = input('Enter a Word:')
clear_screen()
word_list = [ x for x in word]  #this list stores all the letters of the word to guess.

health  = 10 #this is the total miss that a player can make

#print(word_list)


while health >=1:
    print('Your health is: ', health)

    if len(word_list) == 0:
        """
        this statement will be satisfied when the list is empty
        """
        print('Congrats!!! You Won')
        input('Press Enter to quit....')
        break

    else:

        player_guess= input('Enter a letter to gues  a word ')
        print('You have {} more letters to guess.....'.format(len(word_list)))
        if player_guess in word_list:
            word_list.remove(player_guess)
            """
            if player guesses a correct letter then the letter
            is removed from the word_list.
            """

        else:
            print('Wrong Guess!!!\n')
            health=health-1
            if health < 1:
                clear_screen()
                print('\n\n\n\n\n\nSorry!!!You Lose......'.center(100))
                input('\n\n\n\n\nPress Enter to continue....')




