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

def dailyWage(wage_per_hour, work_hour):
    """Description: 
        Function to calculate daily wage of Employee
    Parameters:
        wage_per_hour: rate of wage per hour
        work_hour : total hour of work done
    Returns:
        Daily Wage
    """
    return wage_per_hour*work_hour
    

def main():
    name = input("Enter the name: ")
    logger.info(welcome(name))
    attendance = attendance_check()
    wage_per_hour = 20
    fulltime_work = 8
    part_time_work = 4
    if(attendance==0):
        logger.info("Absent")
    elif attendance==1:
        logger.info("Present")
        logger.info(f"Daily wage of Full Time Employee is {dailyWage(wage_per_hour,fulltime_work)}")
    else:
        logger.info("Present")
        logger.info(f"Daily wage of Part Time Employee is {dailyWage(wage_per_hour,part_time_work)}")
    

if __name__ == "__main__":
    main()
