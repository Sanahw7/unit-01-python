print("This your To-do list.")

List=[]

while True:
    
    increase = 1
     
    for x in List:
        print(x)
        
        print(increase)
        
        increase +=1
           
    
    question1 = input('would you like to "add", "remove" or "clear all" something?')
    
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
        
        
        
    
        
   
        
        
        
        
                    

     