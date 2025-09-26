print("What is your grade?") #prompted user with a question
grade1= int(input("9 or 10 or 11 or 12"))
if grade1 <= 10: #if they're less than or equal to 10 they can't get a parking spot 
    print("no parking pass") #output

else: 
    question2= print("Do you have a pass") #alternative if they're greater than 10th grade
    question2 = input("yes or no") 

    if question2=="yes": #if the person puts yes they will be asked their parking spot
        print("What spot are you parking in?")

    else:
        print("you can't park") #alternative option 
        question3= print("What's your permit number?")
        question3= input("A23 or B15")

        if question2 == question3: #The parking number has to equal their parking spot
            question4= int(input)("What time did you arrive?") 
            if question4 >= 730: #if they arrive at or before 730 they can park here
                print("You can park here")

        else: 
            print("Parking number and spot doesn't match.") #alternative if they arrive earlier than 730


    else:
    print("You're too early try again later.")




 



