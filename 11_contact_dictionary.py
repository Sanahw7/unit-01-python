print("Contact Menu:")

menu= {} #Made an empty dictionary for the users answer

while True: #used a while statement to it would go on forever
    
    question1 = input('would you like to "Add contact", "Delete contact ", "List contacts" or "Exit"') #The user has to input one of the 4 choices
    
    if question1 == "Add contact": #For the first choice 
        
        name = input("enter name") #Enter the name
        phone = int(input("Enter phone number")) #put in the number and I used the integer fucntion so it allows numbers
        menu[name] = phone #put the key into the the brackets
        print("Contact successfully added") #The result is the contact name and phone is added and you're prompted with this message
        
    if question1 == "Delete contact": #The second choice 
        name2 = input("Enter name")
        phone2 = int(input("Enter phone number"))
        del menu[name2] #put the key in the variable so it will delete it
        print("Contact successfully deleted")
        
        
    if question1 == "List contacts":
        
        for x in menu: 
            print(x) #prints the string
            print(menu[x]) #prints the number. So both are printed line by line listing them vertically

            
            
    if question1 == "Exit":
            
            break #pauses the code
    
        
       
        
        
    
        
        
    
     
    

