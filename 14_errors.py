"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try: #Used a try statement because the code is bad 
        result = num1 / num2
    except:
        print("Can't Divide by zero") #The error message you'll get
    print("Result:", result)


""""
Example 2: Opening Files
"""

def read_file(filename):
    try: #The try statement holds the bad code
        file = open(filename, 'r')
    except: #This is testing the code 
        print("File doesn't exist")
    contents = file.read()
    print("File contents:", contents)
    file.close()

"""
Example 3: List Items
"""

def get_item(lst, index):
    try: #It's suppposed to get the items but failed to 
        item = lst[index]
    except:
        print("List out of range")# What went wrong
    print("Item:", item)

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    try:#It's supposed to get the values 
        value = dictionary[key]
    except:
        print(dictionary)
        print("Value:",value)

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try: #This code failed unable to open the file
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError: 
        print("Error: File not found.")#the message saying the user will get
    else:

        print(("File processing completed"))
    
    finally:

        if filename: 
            print("File operation attempted ")
        else:
            print("Cleanup: No file was opened")      
# Example usage:
process_file("example.txt")
