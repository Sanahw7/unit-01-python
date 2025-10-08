"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
Food = "Mcdonald's, pizza, seafood" #created a string 

for x in Food: #used a for loop so it can look over each character
   
   print(x) #it should print it by each word seperately down
    


"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
num = [1, 2, 3, 4, 5 ] #created a variable holding a list 
result = 1 #made a new variable that equal 1 so it adds it one time

for s in num:
    result += s #should mean that result is added to s aka num
   


print(result) #prints out the sum
  


"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
junk = ["Mcdonald's", "pizza", "seafood" ] #made a variable holding a list

for z in junk: #used a for loop for the variable junk

  print(z) #print the new answer with it's own line 

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result
"""
def_1 = { #make a a dictionary
    
    'python': 1, 
    
    'CSS' : 2,
    
    'javascript' : 3,

    'html': 4 # gave each string a value
    
} 

for y in def_1:

  print(y)


"""
In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

#What I noticed was it printed out the values of the list veritcally