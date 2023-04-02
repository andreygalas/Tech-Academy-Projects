Name = input('Please enter the name of the person who created this game: ')
print('This game was made by the amazing ' + 'Andrey' + '!')
print('Welcome to my quessing game!')
print('In this program, you will try to quess a word that I chose.')

def start():
    Player_Name = input('What is the name of the player? ')
    print('Greetings, ' + Player_Name + '! It is time to quess!')
    Secret_Word = 'Flower' .lower()
    Guesses = ' '
    Turns_Left = 5
    while Turns_Left > 0:
        Wrong_Answers = 0
        for Letter in Guesses:
            if Letter in Guesses:
                print (Letter)
            else:
                    print('_')
                    Wrong_Answer += 1
        if Wrong_Answers == 0:
            print('YOU WIN! You guessed my word: ' + Secret_Word + '!!!!!')
            break
        Guess = input('Guess a letter here: ').lower()
        Guesses += Guess

        if Guess not in Secret_Word:
            Turns_Left -= 1
            print('Oops! This letter is not my word. Please try again.')
            print('You have ' + str(Turns_Left) + ' more quesses left. you can do it!')
            if Turns_Left == 0:
                print('GAME OVER')

def Player_Again ():
           Again == input('Would you like to play again? ') .lower()
           if Again == 'no' .lower():
               quit()
           if Again == 'Yes' .lower():
               start()
           else:
               print('Please enter Yes or No. Thank You!')
               Play_Again()
Play_Again()

start()
