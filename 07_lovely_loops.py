campaign_name = input("Enter your campaign name:") #created a variable for each input the user needs to put in

email_list_input = input("Enter email addresses , : ")

company_type= input ("What company type is it: ")
email_list = email_list_input.split(",")
engagement.split(",")

domian_counts = {}
engagement_summary = {"opened": 0, "clicked": 0, "bounced": 0, "unsubscribed": 0} #made a dictionary that holds the engagement summary so it counts how many times each situation happened

for x in email_list: #made a for loop so it iterates each if statment to see what happened to the email
    print(x)
    
    engagement= input("Enter engagement status: ")

    if engagement == "opened":
        
        engagement_summary["opened"]+= 1
        
    if engagement == "clicked":
        
        engagement_summary ["clicked"]+= 1
        
    if engagement == "bounced":
        
        enegagement_summary["bounced"]+=1
        
    if engagement == "unsubscribed":
        
        engagement_summary["unsubscribed"]+=1 #it should go up by 1 
       
 
click_rate = engagement_summary['clicked']/len(email_list) * 100 #counts the percent

if click_rate >= 50: percent="Excellenet"
elif click_rate >= 30: percent= "Good"
elif click_rate > 0: percent= "Needs Improvement"
elif click_rate == 0: percent = "poor"

print()
print(campaign_name)
print(email_list_input)
print(company_name)
print(email_list)
print(domain_counts)
print(engagement_summary)
print(percent) #should print every result out 



    
    



