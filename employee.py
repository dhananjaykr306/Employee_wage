'''
    @Author: Dhananjay Kumar
    @Date: 11-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 11-10-2024
    @Title : Python program to manage employee wage computation using a class
'''

from logger import logger_init
import random

# Initialize logger
logger = logger_init(__name__)

class Employee:
    def __init__(self, name, wage_per_hour, full_time_work_hour, part_time_work_hour, working_days):
        """
        Initialize the Employee class with relevant attributes.

        Parameters:
            name (str): Employee's name.
            wage_per_hour (int): Rate of wage per hour.
            full_time_work_hour (int): Hours for full-time work.
            part_time_work_hour (int): Hours for part-time work.
            working_days (int): Total working days.
        """
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.full_time_work_hour = full_time_work_hour
        self.part_time_work_hour = part_time_work_hour
        self.working_days = working_days

    def welcome_message(self):
        """Generate a welcome message for the employee."""
        return f"Welcome {self.name} to the Employee Wage Computation"

    @staticmethod
    def attendance_check():
        """
        Simulate attendance check.

        Returns:
            int: 0 for Absent, 1 for Full-time, 2 for Part-time.
        """
        return random.choice([0, 1, 2])

    def daily_wage(self, work_hour):
        """Calculate daily wage based on work hours."""
        return self.wage_per_hour * work_hour

    def monthly_wage(self, work_hour):
        """Calculate monthly wage based on work hours."""
        return self.wage_per_hour * work_hour * self.working_days

    def wage_condition(self):
        """
        Calculate total wage with conditions for full-time and part-time work,
        considering attendance and maximum total hours (100 hours).
        """
        total_hours = 0
        total_wage = 0

        for day in range(1, self.working_days + 1):
            attendance = self.attendance_check()
            if attendance == 0:  # Absent
                continue
            elif attendance == 1:  # Full-time
                hours_worked = self.full_time_work_hour
            else:  # Part-time
                hours_worked = self.part_time_work_hour

            total_hours += hours_worked
            total_wage += hours_worked * self.wage_per_hour

            if total_hours >= 100:  # Stop when total hours reach or exceed the limit
                break

        return total_wage

    def log_employee_details(self):
        """Log the details of the employee's attendance and wages."""
        logger.info(self.welcome_message())
        attendance = self.attendance_check()

        if attendance == 0:
            logger.info("Absent")
        elif attendance == 1:
            logger.info("Present (Full-time)")
            logger.info(f"Daily wage of Full-Time Employee: {self.daily_wage(self.full_time_work_hour)}")
        else:
            logger.info("Present (Part-time)")
            logger.info(f"Daily wage of Part-Time Employee: {self.daily_wage(self.part_time_work_hour)}")

        logger.info(f"Monthly wage of Full-Time Employee: {self.monthly_wage(self.full_time_work_hour)}")
        logger.info(f"Monthly wage of Part-Time Employee: {self.monthly_wage(self.part_time_work_hour)}")
        logger.info(f"Total wage earned by Employee: {self.wage_condition()}")

def main():
    # Input and initialization
    name = input("Enter the name: ")
    wage_per_hour = 20
    full_time_work_hour = 8
    part_time_work_hour = 4
    working_days = 20

    # Create an Employee instance
    employee = Employee(name, wage_per_hour, full_time_work_hour, part_time_work_hour, working_days)

    # Log employee details
    employee.log_employee_details()

if __name__ == "__main__":
    main()
