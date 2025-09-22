"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
a = 1 #created a variable  that equals 1 

while a < 11: #used a while loop saying a is less than 11 so it doesn't exceed 10

    print(a) #print out the varible 
    
    a += 1 #should print in ascending form 


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
b = 11 #created variable that equals 11 so it starts from there

while b > 0: # used a while loop to say greater than 0 so it doesn't descend into the negatives

    print(b)
    
    b -=1 #should print in descending form stopping at 0 


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
number = int(input("give me a number:")) #creatd an input that allows integers with the variable number. This prompts the user to give any number

result = 1 #created a new variable that 1

while number > 0: #made a while loop that says greater 0 so the number doesn't fall into the negatives
    result = number * result #this variable should multiple whatever number the user put in and the result
    number -= 1

print(result) #printing the new result
   

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
print("Guess my password") #I print instrutions for the user 

mypass= ("password") #made a variable for the correct password

userinp = input("") #made a second varible for the user to input their guess

while userinp != mypass: #this basically says if the password doesn't equal mypass aka the correct password, the user is give the message wrong
    print("Wrong") #it will then repeat until the user gets it right 
    
    userinp = input("") #this just asks the user the question
    
print("congrats") #once the user gets it right they'll be prompted with is message 

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while lo
"""

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""