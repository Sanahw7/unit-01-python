print("This your To-do list.")

with open("To-do.txt") as file:
    
    List = file.readlines()
    
print (List)


while True:
    
    increase = 1
     
    for x in List:
        print(x)
        
        print(increase)
        
        increase +=1
           
    
    question1 = input('would you like to "add", "remove", "exit" or "clear all" something?')
    
    if question1 == "add":
        
        print("What's your new To-do")
        
        answer1 = input("")
        
        List.append(answer1)
        
    if question1 == "remove":
    
        print("What do you want to remove?")
        
        answer2 = input("")
        
        List.remove(answer2)
        
    if question1 == "clear all":
        
        List.clear()
        
    
    if question1 == "exit":
        
        with open( "To-do.txt") as file:
            
            file.writelines(List)
            
            print(List)
            
            break
    

        
        
        
    
        
   
        
        
        
        
                    

     