# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   GNuesca,11/14/2023,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json  "

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
    # for stud in students:
    #     json_data = (f'{stud["FirstName"]},{stud["LastName"]},{stud["CourseName"]}')
# Creates an empty file if one does not exist
except FileNotFoundError as e:
    print("Enrollments.json does not exist!!!")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    file = open(FILE_NAME, "w")
    file.close()
    print("!!!Empty File Created!!!")
# except KeyError as e:
#     print("!!! Please check the file dictionary keys are valid for this program !!!\n")
#     print(e, e.__doc__, type(e), sep='\n')
#     exit()
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    print("!!! Check file formatting !!!\n")
    # exit()
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            # Input the data
            noWhiteSpace = 'Field can not be blank. Please enter a valid first name.'
            student_first_name = input("What is the student's first name? ")
            if student_first_name.isspace():
                raise ValueError(noWhiteSpace)
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain letters.")
            student_last_name = input("What is the student's last name? ")
            if student_first_name.isspace():
                raise ValueError(noWhiteSpace)
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain letters.")
            course_name = input("Please enter the name of the course: ")
            if course_name.isspace():
                raise ValueError(noWhiteSpace)
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
            print('Please try again')
            continue
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
        students.append(student_data)
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        # Again attempt to notify user if there are issues with the file, but only with dictionary formatting
        try:
            print("-"*50)
            for stud in students:
                print(f'Student {stud["FirstName"]} {stud["LastName"]}is enrolled in {stud["CourseName"]}')
            print("-"*50)
            continue
        except KeyError as e:
            print("!!! Please check the file dictionary keys are valid for this program !!!\n")
            print(e, e.__doc__, type(e), sep='\n')
            # exit()

    # Save the data to a file
    elif menu_choice == "3":
        try:
            for stud in students:
                json_data = (f'{stud["FirstName"]},{stud["LastName"]},{stud["CourseName"]}')
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
        except KeyError as e:
            print("\n!!! Please check the file dictionary keys are valid for this program !!!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            # Would prefer to break out of program so user can fix dictionary key
            # break
            continue
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
            continue
        finally:
            if file.closed == False:
                file.close()
        for stud in students:
            print(f'Student {stud["FirstName"]} {stud["LastName"]} is enrolled in {stud["CourseName"]}')
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")