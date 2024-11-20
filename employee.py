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
    

def monthlyWage(wage_per_hour, work_hour, working_days):
    """Description: 
        Function to calculate monthly wage of Employee
    Parameters:
        wage_per_hour: takes the rate per hour for work
        work_hour: Total work hour
        working_days: total working days for employee
    Returns:
        Monthly Wage
    """
    return wage_per_hour*work_hour*working_days

def wageCondition(wage_per_hour, full_time_work_hour, part_time_work_hour, working_days):
    """Description: 
        Function to calculate the monthly wage of an Employee.
    Parameters:
        wage_per_hour: Rate per hour for work.
        full_time_work_hour: Hours worked for full-time.
        part_time_work_hour: Hours worked for part-time.
        working_days: Total working days for the employee.
    Returns:
        int: Monthly wage.
    """
    total_hours = 0
    total_wage = 0
    for i in range(1,21):
        if(attendance_check()==0):
            total_wage  = total_wage+0
        elif attendance_check() ==1:
            total_wage = total_wage+ full_time_work_hour*wage_per_hour
            total_hours = total_hours+full_time_work_hour
            if(total_hours>=100):
                break
        else:
            total_wage = total_wage+ part_time_work_hour*wage_per_hour
            total_hours = total_hours+part_time_work_hour
            if (total_hours>=100):
                break
    return total_wage


def main():
    name = input("Enter the name: ")
    logger.info(welcome(name))
    attendance = attendance_check()
    wage_per_hour = 20
    fulltime_work = 8
    part_time_work = 4
    working_days = 20
    if(attendance==0):
        logger.info("Absent")
    elif attendance==1:
        logger.info("Present")
        logger.info(f"Daily wage of Full Time Employee is {dailyWage(wage_per_hour,fulltime_work)}")
    else:
        logger.info("Present")
        logger.info(f"Daily wage of Part Time Employee is {dailyWage(wage_per_hour,part_time_work)}")
    logger.info(f"Monthly wage of Full Time Employee is {monthlyWage(wage_per_hour,fulltime_work,working_days)}")
    logger.info(f"Monthly wage of Part Time Employee is {monthlyWage(wage_per_hour,part_time_work,working_days)}")
    logger.info(f"Total wage earned by Employee is  {wageCondition(wage_per_hour,fulltime_work,part_time_work,working_days)}")

if __name__ == "__main__":
    main()
