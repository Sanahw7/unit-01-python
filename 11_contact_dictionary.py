print("Contact Menu:")

menu= {}

while True:
    
    question1 = input('would you like to "Add contact", "Delete contact ", "List contacts" or "Exit"')
    
    if question1 == "Add contact":
        
        name = input("enter name")
        phone = int(input("Enter phone number"))
        menu[name] = phone
        print("Contact successfully added")
        
    if question1 == "Delete contact":
        name2 = input("Enter name")
        phone2 = int(input("Enter phone number"))
        del menu[name2]
        print("Contact successfully deleted")
        
        
    if question1 == "List contacts":
        
        for x in menu:
            print(x)
            print(menu[x])

            
            
    if question1 == "Exit":
            
            break
    
        
       
        
        
    
        
        
    
     
    

