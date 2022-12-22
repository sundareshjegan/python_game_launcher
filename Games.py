
#importing predefined modules to perform respective operations
import random
import time
import math
from designs import *

# user defined function to play rock paper scissor game
def RPS():

    #Initially score is zero 
    score = 0
    alex_score = 0

    ch = input('\n\tDo you need help(yes/No) : ')
    if ch.lower() == 'yes':
        rps_manual()
        name = input('\n\tEnter your name : ')          #get player name 
        name = name.upper()
        
    else:
        name = input('\n\tEnter your name : ')
        name = name.upper()

    print('\n\n\t \tHey ',name,' I am ALEXA... Lets play  !')

    #while loop to play rock paper scissor game
    
    while True:
        
        user_action = input("\nEnter a choice (1/rock, 2/paper, 3/scissors): ")

        if user_action == '1':
            user_action = 'rock'
        elif user_action == '2':
            user_action = 'paper'
        elif user_action == '3':
            user_action = 'Scissors'
        elif user_action == 'help':
            rps_manual
             

        user_action = user_action.lower()

        if user_action =='quit':

            if(score>alex_score):
                print('\n\n\t\tCongrats',name,'You won')
            elif score == alex_score:
                print('\n\n\t\t It is TIE..!')
            else:
                print('\n\n\t\tALEXA won the match...')

    # print the score board during end of the rock paper scissor game
            print('\n')
            print('\t','+','-'*36,'+')
            print('\t','|{}|'.format('SCORE  BOARD'.center(38)))
            print('\t','+','-'*36,'+')
            print('\t','|{} : {}|'.format(name.center(20),str(score).center(15)))
            print('\t','|{} : {}|'.format('ALEXA'.center(20),str(alex_score).center(15)))
            print('\t','+','-'*36,'+')
        
            
            print('\n \t   Well played ',name,'THANK YOU !')

            break
        
        possible_actions = ["rock", "paper", "scissors"]

        #using random function to choose the possible actions
    
        computer_action = random.choice(possible_actions)       
    
        print(f"\nYou chose {user_action}, Alexa chose {computer_action}.\n")

    # conditions for rock paper scissor game is checked based on user input    
        
        if user_action == computer_action:
            print("Both players selected {user_action}. \n\n\t\tIt's a tie!")
        
        elif user_action == "rock":
            if computer_action == "scissors":
                
                print("Rock smashes scissors! \n\n\t\tYou win!")
                score+=1
                
            else:
                print("Paper covers rock! \n\n\t\tYou lose.")
                alex_score +=1
                
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! \n\n\t\tYou win!")
                score+=1
                
            else:
                print("Scissors cuts paper! \n\n\t\tYou lose.")
                alex_score +=1
                
            
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! \n\n\t\tYou win!")
                score+=1
            else:
                print("Rock smashes scissors! \n\n\t\tYou lose.")
                alex_score +=1

        elif user_action == 'help' :
            rps_manual()

        else:
            print('Invalid Choice')
 
              
#************************************************************************************

def jumbled ():
    

        
    # function for choosing random word.
    def choose():
        
        words = ['python', 'computer', 'software', 'programming',
                 'statement', 'hardware', 'condition', 'reverse',
                 'function', 'technology', 'application']

        pick = random.choice(words)
        return pick

  #jumble function to shuffle the letters in a word
    def jumble(word):
        
        random_word = random.sample(word, len(word))

        jumbled = ''.join(random_word)
        return jumbled
  
  #thank funnction to display the score board
    def thank(p1n, p2n, p1, p2):

        print('\n')
        print('\t','+','-'*36,'+')
        print('\t','|{}|'.format('SCORE  BOARD'.center(38)))
        print('\t','+','-'*36,'+')
        print('\t','|{} : {}|'.format(p1n.center(20),str(p1).center(15)))
        print('\t','|{} : {}|'.format(p2n.center(20),str(p2).center(15)))
        print('\t','+','-'*36,'+')


        # check_win() function calling
        check_win(p1n, p2n, p1, p2)
  
        print('\n\t\t Thanks for playing...')

  
  
    # Function for declaring winner
    def check_win(player1, player2, p1score, p2score):
        if p1score > p2score:
            print("\n\n\t\t\twinner is :", player1)
        elif p2score > p1score:
            print("\n\n\t\t\twinner is :", player2)
        else:
            print("\n\n\t\tDraw..Well Played guys..")
  
  
    # Function for playing the game.
    def play():
        # enter player1 and player2 name
        p1name = input("\nPlayer 1, Please Enter your name : ")
        p2name = input("\nPlayer 2, Please Enter your name : ")
        p1name = p1name.capitalize()
        p2name = p2name.capitalize()
  

        pp1 = 0
        pp2 = 0
        turn = 0
  
        while True:
  
            picked_word = choose()      #choose() function call

            qn = jumble(picked_word)    #jumble function call
            print("\n\t\tJumbled word is :", qn)
  
            # checking turn is odd or even
            if turn % 2 == 0:

                print('\n',p1name, 'Its Your Turn....')
  
                ans = input("\nwhat is in your mind? ")
  
                # checking ans is equal to picked_word or not
                if ans == picked_word:
  
                    # incremented by 1
                    pp1 += 1
  
                    print('\n\t\tYour score is ', pp1)
                    turn += 1
  
                else:
                    print("\n\t\tBetter luck next time ..")
  
                    # player 2 turn
                    print('\n',p2name, 'Its Your Turn....\n')
  
                    ans = input('\nwhat is in your mind? ')
  
                    if ans == picked_word:
                        pp2 += 1
                        print("\n\t\tYour Score is :", pp2)
  
                    else:
                        print("\nBetter luck next time...\n\n\t\tCorrect word is :", picked_word)
                    try:
                        c = int(input("\n   Press 1 to continue and 0 to quit :"))
                    except:
                        print('\n\t\t Please Enter 1 or 0 !')
                        c = int(input("\n   Press 1 to continue and 0 to quit :"))
  
                    # checking the c is equal to 0 or not
                    # if c is equal to 0 then break out
                    
                    if c == 0:
                        thank(p1name, p2name, pp1, pp2)
                        break
  
            else:
  
                print('\n',p2name, 'Its Your Turn....')
                ans = input('\nwhat is in your mind? ')
  
                if ans == picked_word:
                    pp2 += 1
                    print("\n\t\tYour Score is :", pp2)
                    turn += 1
  
                else:
                    print("\n\t\t Better luck next time.. :")
                    print('\n',p1name, 'Its Your Turn....')
                    ans = input('\nwhat is in your mind? ')
  
                    if ans == picked_word:
                        pp1 += 1
                        print("\n\t\tYour Score is :", pp1)
  
                    else:
                        print("\n\t\tBetter luck next time...correct word is :", picked_word)

                        #get the choice from the user to play again
                        try:
                            c = int(input("\n   press 1 to continue and 0 to quit :"))
                        except:
                            print('\n\t\t Please Enter 1 or 0 !')
                            c = int(input("\n   Press 1 to continue and 0 to quit :"))
                              
                        if c == 0:
                            # thank() function calling
                            thank(p1name, p2name, pp1, pp2)
                            break
  
                c = int(input("\n\t\tpress 1 to continue and 0 to quit :"))
                if c == 0:
                    # thank() function calling
                    thank(p1name, p2name, pp1, pp2)
                    break
  
  
    play()
    
#**************************************************************************************************

#main user defined function for guess the number game.
def guess_the_number():

    try:
    
        name = input('\n     Enter your name : ')       #gets player name 
        name = name.upper()

        lower = int(input("\n\tEnter Lower bound limit :- "))

        # Taking Inputs
        upper = int(input("\n\tEnter Upper bound limit :- "))
        if upper<lower:
            print('\n\tSorry upper limit is lower than lower limit')
        else:

            # generating random number between the lower and upper bound limits
            
                x = random.randint(lower, upper)
                print("\n\t\t\t Welcome",name,"\n\n\tYou've only ",
                       round(math.log(upper - lower + 1, 2)),
                  " chances to guess the number..!\n")
             
            # Initializing the number of guesses.
                count = 0
             
            # for calculation of minimum number of
            # guesses depends upon range
                while count <math.log(upper - lower + 1, 2):
                    count += 1
             
                # taking guessing number as input
                    guess = int(input("\n  Guess a number:- "))
             
                # tests the condition
                    if x == guess:
                        print("\n\t\tCongratulations you did it in ",
                              count, " try")
                        print('\n\t\t \t\t Well played')
                        print('\t\t \t\t **** ******')
                    
                    # Once guessed, loop will break
                        break
                    elif x > guess:
                        print("\n  You guessed too small!")
                    elif x < guess:
                        print("\n  You Guessed too high!")
             
            # If Guessing is more than required guesses,prints this output.

                    if count >= math.log(upper - lower + 1, 2):
                        print("\n\t   The number is %d" % x)
                        print("\n\tBetter Luck Next time!")
    except:
        print('\n\t\t      O O P S !')
        print('\n\t\t Some thing went wrong...!')
        print('\n\t\tPlease enter numbers only...')

#********************************************************************************
#main function to play handcricket game
def handcricket():
    try:

        #function to change the bat one player is out
        def bat_change():
            global i
            global  bat_player
            if(bat_player==name):
                bat_player='Siri'
            else:
                bat_player=name
            i+=1
            game()

        #game function to play the game and testing conditions
        def game():
            global score_player,score_sri,bat_player,name,i
            while True:
                player_hand = input('\n\tEnter the number 1 to 6 :')
                if player_hand.lower()=='quit':
                    print('\n\t\t THANK YOU...!')
                
                    break
            
                else:
                    player_hand=int(player_hand)
                if player_hand in [1, 2, 3, 4, 6]:
                    pass
                else:
                    print("\n\t\tInvalid input")
                    game()
                list2=[1, 2, 3, 4, 5, 6]
                sri_hand = random.choice(list2)
                print('\n\tIn Siri hand ',sri_hand)
                if (bat_player == name):
                    score_player += player_hand
                else:
                    score_sri += sri_hand
                if player_hand == sri_hand:
                    break

            if(bat_player==name):
                print('\n\t\t',bat_player,'is out')
                print('\n\t\t Score = ',score_player)
            else:
                print('\n\t\t',bat_player,'is out')
                print('\n\t\t Score = ', score_sri)

            if i==0:
                bat_change()
            else:
                if(score_player>score_sri):
                    print('\n\t  CONGRATS..You won the match')
                elif(score_sri>score_player):
                    print('\n\tSIRI WON THE MATCH')
                else:
                    print('\n\t\t Match draw')
                print('\n\t\t WELL PLAYED...BYE')
                
        def hand_cricket():

            global score_player,score_sri,bat_player,i,name
            score_player=0
            score_sri=0
            i=0
            print('\n\n\t\t\t HAND CRICKET')
            print('\t\t\t ^^^^ ^^^^^^^')

            name = input('\tEnter player name : ')
            name = name.upper()

            print('\n\t\t HAI ',name,'..!!!')
            print('\t\t ~~~ ','~'*len(name))

            name1 = name.capitalize()
            print('\n Hey ',name1,' I am Siri...! Lets play...')

            choice=random.choice(['0','1'])
            if (choice=='1'):
                print('\tYou won the toss...')
                bat_bowl=input('\nCHOOSE (BAT or BOWL) : ')
                bat_bowl.lower()
                if(bat_bowl in ['bat','bowl']):
                    if(bat_bowl=='bat'):
                        bat_player=name
                    else:
                        bat_player='Siri'
                else:
                    print('\n\tInvalid input so the game is restarting now')
                    hand_cricket()
            elif(choice == '0'):
                print('\t Siri won the toss...\n')
                list1=['bat','bowl']
                bat_bowl=random.choice(list1)
                if(bat_bowl=='bat'):
                    bat_player='Siri'
                else:
                    bat_player=name
                print('Siri choosed to ',bat_bowl)
            game()
             
        hand_cricket()
    #exception case when any run time error occurs
    except:
        print('\n\t\t      O O P S !')
        print('\n\t\t  Some thing went wrong...!')
        print('\n\t   Please read the manual and play again...')

#**********************************************************************************           
            








