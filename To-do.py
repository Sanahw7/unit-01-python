print("This your To-do list.")

List=['Apples', 'plums', 'grapes', 'oranges']

while True:
    
    question1 = input('would you like to "add" or "remove" something?')
    
    if question1 == "add":
        
        print("What's your new To-do")
        
        answer1 = input("")
        
        List.append(answer1)
        
    if question1 == "remove":
    
        print("What do you want to remove?")
        
        answer2 = input("")
        
        List.remove(answer2)
        
        for x in List:
            print(x)
            
    question2= input('Would you like to "remove", "add" or "clear all"')
    
    if question2== "clear all":
            
        List.clear()
        
        print("Here's your current list:")
        
        for z in List:
            print(z)
    
        
   
        
        
        
        
                    

     