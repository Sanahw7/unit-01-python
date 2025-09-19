num1 = float(input('Enter the first number: ')) #Made 2 variables so user can input 2 numbers and it can support floats
num2 = float(input('Enter the second number: '))

print()
input1= input("Select operation:"
"Addition,"
"Subtraction,"
"Multiplication,"
"Division,"
"Floor Divison,"
"Exponential,"
"Remainder,")
  
if input1 == "Addition": #Created if statements for each operation 
    print(num1 + num2) 
    
elif input1 == "subtraction":
    print(num1-num2)
        
elif input1== "Multiplication":
    print(num1*num2)
            
elif input1== "Division":
    if num2 == 0:
        print("You can't calculate with that number") #this message will print if the denominator is 0
    print(num1/num2)
    
                
elif input1== "Floor division":
    print(num1//num2)

elif input1== "Exponential":
    print(num1**num2)

elif input1== "Remainder":
    print(num1%num2)

else: print("Invalid operation") #If none of these operations are entered I made an else statement
        
    
          
            
