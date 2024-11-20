'''
    @Author: Dhananjay Kumar
    @Date: 11-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 11-10-2024
    @Title : Python program to print welcome message
'''

from logger import logger_init
import random

# Initialize logger
logger = logger_init(__name__)

def welcome(name):
    """
        Description :
            This function is used to return welcome message
        Parameters :
            name: This is the name that we have to give welcome message
        Return :
            It returns the welcome message.
    """
    return f"Welcome {name} to the Employee Wage Computation"

def attendance_check():
    """
        Description:
            This function is to return present or absent
        Return :
            It returns present or absent
    """
    attendance = random.randint(0, 1)
    if attendance == 1:
        return "Present"
    else:
        return "Absent"

def main():
    name = input("Enter the name: ")
    welcome_message = welcome(name)
    logger.info(welcome_message)  # Log the welcome message
    attendance = attendance_check()
    logger.info(f"Attendance: {attendance}")  # Log the attendance status

if __name__ == "__main__":
    main()
