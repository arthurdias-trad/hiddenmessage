
# coding: utf-8

# coding: utf-8

# In[4]:


# Set the passcode the user needs to enter as their name to activate program.

passcode = "a"


#Get the user to enter a passcode, check if its compatible, if not kick user.

login = input("Welcome to Message Mate \n Please enter your name :). ")

while True:
    if passcode != login:
        print("Sorry this program is down for maintence. \n We expect all upgrades to be done within 48 hours. \n Please check back then.")
        break 
    
    else:
        name = input("Now that we know you can be trusted what name would you like to go by?")

#If user passes the test welcome them back, and find out if they wish to receive or leave a message    
    
    if passcode == login:
        print("Welcome back Commander",name +"!")
    
# Get user input for action and make sure that its either receive, or leave.
    
    while True:
        action = input("Do you wish to leave a message, or receive a message?")
        if action.lower() == "receive":
            print("I understand, lets see if anyone cares enough about you to have left a message")
            break 
        if action.lower() == "leave":
            print("Excellent, I am sure someone will be very happy to hear from you",name + "!")
            break
        else:
            print("Sorry but we only deal in certainties, please enter either 'receive' or 'leave':D!")
        
#Allow user to leave a message, save message in a varaible, hash message, display hash to be used as a key.        
    
    count = 0

    if action.lower() == "leave":
        message = input("So what exactly is so important that you couldn't say it anywhere else? : ")
        message = message[count]
        message = ""
        print(message[count])
        
        
        break
        
    
    


# In[9]:


# Set the passcode the user needs to enter as their name to activate program.

passcode = "ch33s3cakE"


#Get the user to enter a passcode, check if its compatible, if not kick user.

login = input("Welcome to Message Mate \n Please enter your name :). ")


if passcode != login:
    print("Sorry this program is down for maintence. \n We expect all upgrades to be done within 48 hours. \n Please check back then.")
else:
    name = input("Now that we know you can be trusted what name would you like to go by?")

#If user passes the test welcome them back, and find out if they wish to receive or leave a message    
    
if passcode == login:
    print("Welcome back Commander",name +"!")
    
# Get user input for action and make sure that its either receive, or leave.
    
while True:
    action = input("Do you wish to leave a message, or receive a message?")
    if action.lower() == "receive":
        print("I understand, lets see if anyone cares enough about you to have left a message")
        break 
    if action.lower() == "leave":
        print("Excellent, I am sure someone will be very happy to hear from you",name + "!")
        break
    else:
        print("Sorry but we only deal in certainties, please enter either 'receive' or 'leave':D!")
    
    

