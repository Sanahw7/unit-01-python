import os 
import sys


"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""

var = os.getcwd() #made a variable called "var" and used the os moduleto print the current directory

print(var)

"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""

var2 = os.listdir() #made a variable that holds the os and the command that list the files and current directories

print()

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
directory_P = "Data" 


if os.path.isdir("Data"): #used a conditional so they'll be able to tell if the directory exist or not
    print("Directory already exists")
    
else:
    print("Directory doesn't exist") #This is what's printed if it doesn't exist
    
    


"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
file_p = "config.txt"

if os.path.exists(file_p) #this tests if file_p exist or not
    print("")
    
else:
    print("File not found")

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print(sys.version) #used sys module and the .version sees what version of python you're using 

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""

print(sys.platform) #.platform sees what version interpreter you're using 