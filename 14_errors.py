"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except:
        print("Can't Divide by zero")
    print("Result:", result)


""""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        file = open(filename, 'r')
    except:
        print("File doesn't exist")
    contents = file.read()
    print("File contents:", contents)
    file.close()

"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
        item = lst[index]
    except:
        print("List out of range")
    print("Item:", item)

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)
