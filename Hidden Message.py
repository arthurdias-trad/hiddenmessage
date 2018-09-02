

# coding: utf-8

# In[ ]:


# Set the passcode the user needs to enter as their name to activate program.

passcode = "a"

messages = []  # Need to find a way for this not to reset the list each time the code is run.

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
        print("Welcome back Commander",name.title() +"!")
    
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
        
#Allow user to leave a message, save message in a list, hash message, display hash to be used as a key.  


    if action.lower() == "leave":
        message = input("So what exactly is so important that you couldn't say it anywhere else? : ")
        messages.append(message)
        location = messages.index(message)
        message = ""
        lock = hash(messages[location])
        print(key)
        print(messages[location])
        print(location)
        
        break
        
        
# This is the part of the code to check your messages   
# Check the hash against the hashes of the items in the list, if its the same display the message, and change the messages
   
    if action.lower() == "receive":
        key = input("What key were you given?")
        for item in messages:
            if hash(item) == key:
                print(item)
                item = "Sorry we can't find what your looking for"
                break
    else:
        print("Sorry that code doesn't exist, it may have been used already :(. \n Try torturing the information out of your friend!)")
        break 
            
        
    
    

