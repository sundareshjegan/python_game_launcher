#importing pre defined modules 
import time
import sys

#using sys module to print colour font in IDLE
shell = sys.stdout.shell
def please_wait():
    print('\n\n\t\t\t\tPlease wait',end='')

    for i in range(3):
        time.sleep(1)
        print('.',end='')
    print('\n')


#user defined function to display title of this launcher
def display():
    
    shell.write("""
                            █████████       █████████  
                           ███░░░░░███     ███░░░░░███ 
                          ░███    ░░░     ░███    ░███ 
                          ░░█████████     ░███████████ 
                           ░░░░░░░░███    ░███░░░░░███ 
                           ███    ░███    ░███    ░███ 
                           ░█████████     █████   █████
                           ░░░░░░░░░     ░░░░░   ░░░░░ 
                                                         
                     ""","KEYWORD")
    shell.write("""
           
                 ██████╗      █████╗     ███╗   ███╗    ███████╗                               
                ██╔════╝     ██╔══██╗    ████╗ ████║    ██╔════╝                               
                ██║  ███╗    ███████║    ██╔████╔██║    █████╗                                 
                ██║   ██║    ██╔══██║    ██║╚██╔╝██║    ██╔══╝                                 
                ╚██████╔╝    ██║  ██║    ██║ ╚═╝ ██║    ███████╗                               
                 ╚═════╝     ╚═╝  ╚═╝    ╚═╝     ╚═╝    ╚══════╝                               
                                                                                               
██╗          █████╗     ██╗   ██╗    ███╗   ██╗     ██████╗    ██╗  ██╗    ███████╗    ██████╗ 
██║         ██╔══██╗    ██║   ██║    ████╗  ██║    ██╔════╝    ██║  ██║    ██╔════╝    ██╔══██╗
██║         ███████║    ██║   ██║    ██╔██╗ ██║    ██║         ███████║    █████╗      ██████╔╝
██║         ██╔══██║    ██║   ██║    ██║╚██╗██║    ██║         ██╔══██║    ██╔══╝      ██╔══██╗
███████╗    ██║  ██║    ╚██████╔╝    ██║ ╚████║    ╚██████╗    ██║  ██║    ███████╗    ██║  ██║
╚══════╝    ╚═╝  ╚═╝     ╚═════╝     ╚═╝  ╚═══╝     ╚═════╝    ╚═╝  ╚═╝    ╚══════╝    ╚═╝  ╚═╝

 ""","COMMENT")
    shell.write('*='*50,"KEYWORD")


#*******************************************************************************************************


#*********************************************************************************************************



def design_rps():
    shell.write("""
            ╦═╗╔═╗╔═╗╦╔═    ╔═╗╔═╗╔═╗╔═╗╦═╗    ╔═╗╔═╗╦╔═╗╔═╗╔═╗╦═╗╔═╗
            ╠╦╝║ ║║  ╠╩╗    ╠═╝╠═╣╠═╝║╣ ╠╦╝    ╚═╗║  ║╚═╗╚═╗║ ║╠╦╝╚═╗
            ╩╚═╚═╝╚═╝╩ ╩    ╩  ╩ ╩╩  ╚═╝╩╚═    ╚═╝╚═╝╩╚═╝╚═╝╚═╝╩╚═╚═╝



                    1 = rock
                    2 = Paper
                    3 = Scissors
            
            * Type "quit" to exit from this game...\n""","KEYWORD")
    

    
def design_gtn():
    shell.write("""
              __      _  __  __   ___     _                  _   _  _  
             /__ | | |_ (_  (_     | |_| |_   |\ | | | |\/| |_) |_ |_) 
             \_| |_| |_ __) __)    | | | |_   | \| |_| |  | |_) |_ | \
             
            * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - ""","COMMENT")

def design_hc():
    shell.write("""

                 _   _  _____  _   _  ___       ___    ___    _  ___    _   _  ___   _____ 
                ( ) ( )(  _  )( ) ( )(  _`\    (  _`\ |  _`\ (_)(  _`\ ( ) ( )(  _`\(_   _)
                | |_| || (_) || `\| || | ) |   | ( (_)| (_) )| || ( (_)| |/'/'| (_(_) | |  
                |  _  ||  _  || , ` || | | )   | |  _ | ,  / | || |  _ | , <  |  _)_  | |  
                | | | || | | || |`\ || |_) |   | (_( )| |\ \ | || (_( )| |\`\ | (_( ) | |  
                (_) (_)(_) (_)(_) (_)(____/'   (____/'(_) (_)(_)(____/'(_) (_)(____/' (_)

                *************************************************************************""","COMMENT")
                                                                           
    shell.write("""
                                              
                                   ..                                          
                                  ,##:                                         
                                  %,.#:                                                                            
                                  +%#%@,                                    
                                   +##:#.                                   
                                    %%.,#.                                  
                                    .%+.,#.                                 
                                     .%+ :#..%%.                            
                                      .#:.:##:+%.                           
                                       .#::#..+#%                           
                                        .##..+%.%+            .:+:.         
                                        ,#..+%. .%+          :#%@+@+.       
                                        .#,.+%.   .%+        :#. %,%#%       
                                        .#:+%.     .#:.     .#.  +::+#,      
                                         .##.       .#:     ,%   +,:+:+      
                                          .#,        .#:.   :+   #.+:,%      
                                           .#,        .#,   ,%  ,% #.,%      
                                            ,#,       ..#,  .#..#.,% %,      
                                             ,#.        .#,  :##,,#.:%       
                                              ,#.        ,#,..+#+@+%%.       
                                               ,#.        ,#.  .+%+,         
                                                :#.        ,#.               
                                                 :#.        ,#.              
                                                  :#.        :#.             
                                                   +%.        :#.            
                                                    +%.        +#.           
                                                    .+%       ,#+%.          
                                                      %+     ,#, #.          
                                                       .%+   ,#, ,#.          
                                                        .%+ ,#, ,#,           
                                                        .#+#,.,#.            
                                                         .#+.:#.             
                                                          .###.              
                                                            ..                
                                                                        ""","STRING")


    
def design_jw():
    
    print("꧁༒☬𝓙𝓤𝓜𝓑𝓛𝓔𝓓 𝓦𝓞𝓡𝓓𝓢☬༒꧂                𓂀 𝕁𝕌𝕄𝔹𝕃𝔼𝔻 𝕎𝕆ℝ𝔻𝕊 𓂀")

    print('\n')
    print("""                   ⒿⓊⓂⒷⓁⒺⒹ ⓌⓄⓇⒹⓈ

        o o   o o   o o--o  o     o--o o-o       o       o  o-o  o--o  o-o    o-o  
        | |   | |\ /| |   | |     |    |  \      |       | o   o |   | |  \  |     
        | |   | | O | O--o  |     O-o  |   O     o   o   o |   | O-Oo  |   O  o-o  
    \   o |   | |   | |   | |     |    |  /       \ / \ /  o   o |  \  |  /      | 
     o-o   o-o  o   o o--o  O---o o--o o-o         o   o    o-o  o   o o-o   o--o  """) 


    print('\n\t\t\t JUMBLED WORDS')
    print('\t\t\t ^^^^^^^ ^^^^^')

   
#******************************************************************************************
def rps_manual():
    print("""

    +---------------------------------------------------------------------------------------------------------+
    |                                                                                                         |
    |                                  ROCK,PAPER and SCISSOR                                                 |
    |                                 ========================                                                |
    |                                                                                                         |
    |                             Welcome to rock,paper,scissors game.                                        |                                                |
    |                                                                                                         | 
    |       STEP 1:                                                                                           |
    |      --------                                                                                           |
    |                                                                                                         |
    |           * Here,enter your name and your opponent will be the computer(named ALEXA).                   |
    |                                                                                                         |
    |       STEP 2:                                                                                           |
    |      --------                                                                                           |
    |           * Before starting the game,know these....                                                     |
    |                                                                                                         |
    |                           1=rock                                                                        |
    |                           2=paper                                                                       |
    |                           3=scissors                                                                    |
    |                                                                                                         |
    |         These are the values,where you can either Enter 1 or rock,2 or paper,3 or scissors              |
    |                                                                                                         |
    |       STEP 3:                                                                                           |
    |      ---------                                                                                          |
    |           * Start the game by entering any choice (1/rock , 2/paper , 3/scissors)                       |
    |                                                                                                         |
    |       STEP 4:                                                                                           |
    |      --------                                                                                           |
    |                          WINNING CRITERIA                                                               |
    |                         ==================                                                              |
    |                                                                                                         |
    |        * If you and the opponent choose the same choice,it will be considered as tie point.             |
    |        * If you choose rock and the opponent chooses paper,you lose as paper covers the rock.           |
    |        * If you choose rock and the opponent chooses scissors,you win as rock breaks the scissors.      |
    |        * If you choose paper and the opponent chooses rock,you win as paper covers the rock.            |
    |        * If you choose paper and the opponent chooses scissors,you lose as scissors cut the paper.      |
    |        * If you choose scissors and the opponent chooses paper,you win as scissors cut the paper.       |
    |        * If you choose scissors and the opponent chooses rock,you lose rock breaks the scissors.        |
    |                                                                                                         |
    |        STEP 5:                                                                                          |
    |       --------                                                                                          |
    |                                                                                                         |
    |           * If you give quit,your total score will be displayed...                                      |
    |             and you can go to choose any other game by entering their number.                           |
    |                                                                                                         |
    +---------------------------------------------------------------------------------------------------------+""")

def jw_manual():
    print("""
        +===================================================================================================================+

                                                    ⒿⓊⓂⒷⓁⒺⒹ ⓌⓄⓇⒹⓈ
                                                  -------------------------
        
            1.It is a two player game and each player will be provided with a jumbled word.                           
            
            2.Do remember the jumbled set of words will be asked in random manner to both the players.
            
            3.First,both the players should enter the names and start the game.
            
            4.First,the jumbled word will be given to player 1 and he will be asked to
              find the correct word by jumbling the letters of the word.
            
            5.If the first player answers correctly,he will be provided with a point and next jumbled
              word will be given to him to answer.
            
            6.If he fails or gives the wrong answer or guess,the next turn will be provided to the next player(player 2).
            
            7.If the next player answers correct,he will be provided with a point.If he also fails to
              answer the same word missed by the previous player,the games ends by providing the result with score.
              
            8.The player who scores high points will be considered as the winner of the game.
            
            9.If both the player does get the same score or not even a single point,the game will be considered as draw.
            
            10.If you give 1 to continue and 0 to quit,your total score will be displayed and you can
               go to choose any other game by entering their number.
               
        +------------------------------------------------------------------------------------------------------------------+
        """)
def gtn_manual():
    print("""
        +------------------------------------------------------------------------------------------------------------------+

                                            G U E S S    T H E    N U M B E R
                                          -------------------------------------
        
            1.Welcome to GUESS THE NUMBER game.It is a single player game and you can enter by entering your name first.
            
            2.Enter lower bound limit and upper bound limit as per your wish.
              (Ex:Lower bound limit :- 25
                  Upper bound limit :- 31)
                  
            3.The number range from where you guess the answer, will be dependent on whatever the limits you give accordingly.
            
            4.Also,the number of chances to find the correct guess(answer) will be given based on the limits you give.
            
            5.From the example given,consider your choosing 29.Consider,it is showing "You guessed too high".So the chances
              must be below 29.
              
            6.Now consider your choosing 26,and its shows "You guessed too low".So the guessing answer must lie in between
              26 and 29.
              
            7.Now as a third chance,you guess as 28.
              So it is the correct answer and you will be shown "Congratulations,you did it in 3 try."
            
            8.If you didn't complete your guessing within the chances given,it shows the correct answer and "Better luck next time"
            
            9.So, the game is to guess the correct number within the given number of chances.
            
            10.So the given example helps you to continue the game.
            
            11.If you give quit,you can go to choose any other game by entering their number.
            
        +===================================================================================================================+
        """)        

def manual():
    shell.write("""



 (                                 *           (                        )     )            )       (     
 )\ )    (       (        (      (  `          )\ )    (             ( /(  ( /(    (    ( /(       )\ )  
(()/(    )\      )\ )     )\     )\))(   (    (()/(    )\        (   )\()) )\())   )\   )\()) (   (()/(  
 /(_))((((_)(   (()/(  ((((_)(  ((_)()\  )\    /(_))((((_)(      )\ ((_)\ ((_)\  (((_) ((_)\  )\   /(_)) 
(_))   )\ _ )\   /(_))_ )\ _ )\ (_()((_)((_)  (_))   )\ _ )\  _ ((_) _((_) _((_) )\___  _((_)((_) (_))   
/ __|  (_)_\(_) (_)) __|(_)_\(_)|  \/  || __| | |    (_)_\(_)| | | || \| || \| |((/ __|| || || __|| _ \  
\__ \   / _ \     | (_ | / _ \  | |\/| || _|  | |__   / _ \  | |_| || .` || .` | | (__ | __ || _| |   /  
|___/  /_/ \_\     \___|/_/ \_\ |_|  |_||___| |____| /_/ \_\  \___/ |_|\_||_|\_|  \___||_||_||___||_|_\


                            __  ___   ___     _   __   __  __   ___       __ 
                           /  |/  /  /   |   / | / /  / / / /  /   |     / / 
                          / /|_/ /  / /| |  /  |/ /  / / / /  / /| |    / /  
                         / /  / /  / ___ | / /|  /  / /_/ /  / ___ |   / /___
                        /_/  /_/  /_/  |_|/_/ |_/   \____/  /_/  |_|  /_____/
                                                                             """)
    print("""

    Please follow below steps :

        1.Welcome to SA game launcher.
        
        2.You can type to register,when you are new to this launcher.
          Once you have registered,you can login with your details whenever you want.
          
        3.You can choose any of these four games by typing their numbers respectively.
           
            LIST OF GAMES
          %=%=%=%=%=%=%=%=%
          
            1.ROCK PAPER SCISSOR
            2.HAND CRICKET
            3.JUMBLED WORDS
            4.GUESS THE NUMBER
            
        4.After entering the game number, you want to play,you can start playing by entering your name.
        
        5.If you no need to play any games from launcher,you can type "QUIT" and exit from game 
          launcher.
          
        6.Once you enter into any game,you can type "help" to receive user manual of that particular game.
        
        7.The opponent for HAND CRICKET is Siri and opponent for ROCK PAPER SCISSOR is Alexa.(i.e computer is opponent)
        
        8.JUMBLED WORDS is a two player game and GUESS THE NUMBER is a single player game.

        9. At last please provide your rating and give your valuable feedback.
        
        10.You can enjoy and have fun in playing games provided by our GAME LAUNCHER!

        * Feel free to contact us to share your comments
        * If you had any queries regarding this launcher please contact us.

                CONTACT : 20uit037@kamarajengg.edu.in
                          20uit035@kamarajengg.edu.in
                          
    +========================================================================================================+""")


def hc_manual():
    print("""


        +========================================================================================================+
                                        H A N D   C R I C K E T
                                      %-%-%-%-%-%-%-%-%-%-%-%-%-%
            
            1.It is a single player game,where the opponent is Siri(i.e computer)
            
            2.The rules will be based on what you choose,either batting or bowling.
            
              If you win the toss,you can choose either batting or bowling.
              Else Siri would choose either batting or bowling,if it wins the toss.
              
            3.BATTING
            
                *If you choose batting,you can type any number from 1 to 6 against your opponent Siri(bowler).
                *You must type opposite number aginst the bowler to score your runs according to whatever number
                 you type.
                *If you type the same number what the bowler keeps,then you will considered as "OUT".
                *The runs will be calculated as what you scored.

            4.BOWLING
            
                *If you choose bowling,you can type any number from 1 to 6 against your opponent Siri(Batsman)
                *You must be cunning clever to bowl against the batsman.
                *Try to keep the same number as the batsman continue to keep the same number. 
                *Unless you make him out,you are suppose to keep on bowling.
                
        +========================================================================================================+""")
    
#**********************************************************************************************************
def thank():
    print("""

                     ______ __ __ ___    _  __ __ __  __  __ ____   __  __
                    /_  __// // // _ |  / |/ // //_/  \ \/ // __ \ / / / /
                     / /  / _  // __ | /    // ,<      \  // /_/ // /_/ / 
                    /_/  /_//_//_/ |_|/_/|_//_/|_|     /_/ \____/ \____/
                                                                                                                                                       
                                                                                                                                                                        
                                =*                                                                                                                                      
                                 =##*:               -+#+                                                                                                               
                                  *#####+.      -=#####:                                                                                                                
                                  .##*.-*###**###=:*@#-                                                                                                                 
                                   :##=   .:+-    *@#.                                                                                                                  
                                  .=##*-        .*##.                                                                                                                   
                             .:*###+-            .=###+.                                                                                                                
                         -+######*====::.      .     :###*:                                                                                                             
                               ......-+##:   =####@@#########*-                                                                                                         
                                       =#*:.+##-                                                                                                                        
                                       .*####*-                                                                                                                         
                                        -###+.                                                                                                                          
                                         =#*-                                                                                                                           
                                         -+:""")

def bye():
    print("""
                                                 )         
                                       (      ( /(         
                                     ( )\     )\())   (    
                                     )((_)   ((_)\    )\   
                                    ((_)_   __ ((_)  ((_)  
                                     | _ )  \ \ / /  | __| 
                                     | _ \   \ V /   | _|  
                                     |___/    |_|    |___|""")
                                                    

    














    
        

