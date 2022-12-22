'''
        MAIN MODULE FOR GAME LAUNCHER

    Name          : Sundareshwaran J
    Roll Number   : 20UIT037
    Name of the Game : SA GAME LAUNCHER
'''

# importing user defined modules 
from Games import *             
from Register import *
from designs import*

#importing time module 
import time


#loop to print loading using time module

print('\n\n\t\t\tKindly use Full screen mode...\n\n')

print('\n\n\t\t\t\tLoading',end='')
for i in range(6):
    time.sleep(1)
    print('.',end='')
print('\n')

# call the user defined functions 
display()
    
intro()

# function to get the choice from the user 
def choices():
    
    choice = input('\nEnter (register/login/help) : ')
    
    if choice.lower()=='help':
        manual()
        choices()
    elif choice.lower()=='login':
        login()
    

    elif choice.lower()=='register':
        register()  
        
    else:
        print('\n','\t'*4,'INVALID CHOICE !')
        choices()
choices()

# main function which executes all the games

def main():
    ch='yes'    #assigning 'yes' to variable ch for continuous execution of the loop
    while  ch.lower()== 'yes':

                    #print the choices of games

        print('\n'  ,'$^'*50,'\n')
        print('''\n

                                    LIST OF GAMES
                                    =============

                                1. ROCK PAPER SCISSOR
                                2. HAND CRICKET
                                3. JUMBLED WORDS
                                4. GUESS THE NUMBER

                            TYPE "QUIT" TO EXIT FROM LAUNCHER
                
                    TYPE "HELP" TO GET THE USER MANUAL OF THIS LAUNCHER''')

                #get the choice of game from user
        user_choice=input('\nEnter the number of game which you want to play : ')

        # calls the game based on user choice
        if user_choice == '1':              #choice for rock paper scissor game
            
            please_wait()
            design_rps()
            RPS()
            
        elif user_choice == '2':            #choice for hand cricket game
            
            please_wait()

            # gets choice from the user if they need manual of particular game 
            help_choice=input('\n\t  Do you need help ! (yes/no) :')
            if help_choice.lower()=='yes':
                hc_manual()
                design_hc()
                handcricket()
            elif help_choice.lower()=='no':
                design_hc()
                handcricket()
            else:
                print('\n\t\t Invalid input !')
                
            
        elif user_choice =='3':             #choice for jumbled words game
                
            please_wait()
            help_choice=input('\n\t  Do you need help ! (yes/no) :')
            if help_choice.lower()=='yes':
                jw_manual()
                design_jw()
                jumbled()
            elif help_choice.lower()=='no':
                please_wait()
                design_jw()
                jumbled()
            else:
                print('\n\t\t Invalid input !')
            
        elif user_choice == '4':            #choice for guess the number game
            
            please_wait()
            help_choice=input('\n\t  Do you need help ! (yes/no) :')
            if help_choice.lower()=='yes':
                gtn_manual()
                print()
                design_gtn()
                print()
                guess_the_number()
            elif help_choice.lower()=='no':
                please_wait()
                design_gtn()
                print()
                guess_the_number()
            else:
                print('\n\t\t Invalid input !')

        elif user_choice.lower()=='help':       
            manual()                    #print the manual when user needs help
                
            
        elif(user_choice.lower() == 'quit'):

            #Thanks the user when they quit and gets 

            thank()
            print('\n\t\t PLEASE GIVE YOUR RATING  ',end=' ')
            star = input('How many stars do you like to give : ')
            print('\n\n\t\t\t\t  Thanks for your rating...')
            opinion = input('\n\n\t\t\t   Do you like to give any feedback (yes/no)...')
            if opinion.lower()=='yes':
                ip = input('\n\tPlease type your Feedback and press Enter : \n\t')
                with open('opinion.txt','a+') as f:
                    f.write(ip)
                    f.write('\n')

                print('\n\n\t\t\t\t  Thanks for your valuable feed back...')
                
            bye()
            time.sleep(3)
            
            exit()      #automatically exits from idle when user likes to quit
            break
        else:
            print('\n','\t'*4,'INVALID CHOICE !')
            main()
main()
    
