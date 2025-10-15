"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

from datetime import datetime #I imported the datetime module

my_date = datetime.now() #made a variable that is supposed to find the current date and time

print(my_date) #it will then print out starting with the year, month then day and time including milliseconds


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import datetime 

my_datee = datetime.now() #created a variable using the datetime.now module so it'd find the current date

the_string = my_datee.strftime("%m/%d/%Y") #the strftime was used because it formats how you want your time to look capitalization matters

print(the_string) #It should print out the date with "/"

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
my_string1 = "09/07/2008" #The first string 

my_date = datetime.strptime(my_string1, "%m/%d/%Y") #formatted the date using strptime with a new variable

my_string2 = "05/27/2005" #the second date 

my_date2 = datetime.strptime(my_string2, "%m/%d/%Y") #formatted the date 

print(my_date-my_date2) #this prints out the difference between the days of the dates


"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

print("What's your birthdate?") #The user is prompted with a question 

answer1 = input() #They will have to enter their birthdate in mm-dd-YYYY format

my_date = datetime.strptime(answer1, "%m/%d/%Y") 