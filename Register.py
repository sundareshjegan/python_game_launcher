
#importing re module to check the credentials
import re
#importing time module
import time

#user defined function to print the introduction
def intro():
    print("""
                TO USE THIS GAME LAUNCHER YOU NEED TO REGISTER
                
                        TYPE 'Register' to register.
                        
                   * If you had an account Type login.
                   
                * Type "HELP" to get manual of this game""")
            

#user defined function to register into the game launcher
def register():
    print("\n\t\t\t WELCOME TO 'SA' GAME LAUNCHER")

    #getting cerdentitials like e-mail,password from the user
    name = input('\n\tEnter your name       : ')            
    email = input('\tEnter email           : ')
     
    print('\n','\t'*4,'Password should contain 8 letters')
    password1= input('\tEnter password        : ')
    password2 = input('\tEnter confirrm password : ')
    
    name = name.upper()
    name = " ".join(name)

    #conditions to check all the given details are perfect 

    if len(password2)>=8:
        if password1==password2: 
            if email.islower():
                pattern = r"[0-9]*[a-z]+[0-9]*@[a-z]+"
                match = re.match(pattern,email)
                if match:
                    
                    print('\n\t\t\t\tPlease Wait')
                    print('\n\t\t\tYour account is registering')
                    print('\n\n\t\t\t\tRegistering',end='')
                    
                    for i in range(5):
                        time.sleep(1)
                        print('.',end='')
                    print('\n')
                    print('\n\t\t\t     REGISTRATION SUCCESSFUL')
                    print('\t\t\t     =======================')

                    
                    f=open("details.txt","a+")              #opening a file to write the details of user
                    
                    for i in range(1):
                        f.write(email)
                        f.write("$")
                        f.write(name)
                        f.write('|')
                        f.write(password2)
                        
                        f.write("\n")
                        
                    f.close()

                    print('\n','*='*50)
                    print('\n'*2,'\n\t\t\t\t W E L C O M E \t',name)
                    length = len(name)
                    print('\t\t\t\t(-------------\t','-'*length,')')
                   
                    
                    
                    dict={'name':name,'email':email,'password':password2}
                    return dict
                    exit()
                else:
                    print('\n\n\t\t Plese Enter valid email')
                    register()
            else:
                print('\n\n\t\t E-mail should only contain lower case letters only')
                register()

        else:
            print('\n\n\t\t Enter correct confirm password')
            register()
    else:
        print('\n\n\t\t Password should contain 8 or more letters...')
        register()

#user defined function to login
      
def login():
    f=open("details.txt","r")           #opens the file to read the user details
    list=[]                             #creates an empty list
    user_dict={}                        #creates an empty dictionary

    #reads the data in the file
    for i in f:
        list.append(i)   

    #for loop to split the data   
    for i in list:
        temp=i.split('|')
        password=temp[1]
        temp=temp[0].split("$")
        email=temp[0]
        name=temp[1]

        user_dict[email]={'name':name,'pass':password}
    

    #get the email and password from the user
    email = input('\n\tEnter email : ')
    password = input('\n\tEnter the password : ')

    #check whether the details are already present in the file
    
    if email not in user_dict.keys():
        print('\n\t\t Sorry your email id is not registered...')
        choice = input('\n Do you want to register again (yes / no): ')
        if choice == 'yes' :
            register()
        elif(choice == 'no') :
            login()
        else:
            print("\n\t Please give (yes/no)")
            exit()
                           
    elif password not in user_dict[email]['pass']:
            print('\n\t\t Sorry Password is wrong...')
            login()
    
    else:
        for i in user_dict.keys():
            
            if i == email:
                if user_dict[i]['pass']==password+'\n':
                    print('\n\n\t\t WELCOME BACK...  ',user_dict[i]['name'])
                    l = len(user_dict[i]['name'])
                    print('\t\t(---------------  ','-'*l,')')
        












    
    
