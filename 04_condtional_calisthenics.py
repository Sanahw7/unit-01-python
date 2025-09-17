'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
if 22 > 10:
    print("True")
else:
    print("False")

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
Print("Are you a student?")
Answer1= input( "yes or no")
Print("What's your age?")
Answer2= input()
if Answer1== "yes" or Answer2 < 18:
    print("Ticket price is $10") 
else:
    print("Ticket price is $20")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
print("Enter Apple.")
Fruit1= ["Apple", "Apple", "Apple"]
print("Apple" in Fruit1)
if "Apple" in Fruit1:
    print("Yes, that fruit is in the list.")
else: 
    print("No, that fruit is not in the list.")






'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''