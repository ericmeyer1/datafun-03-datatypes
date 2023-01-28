"""
Eric Meyer

Created: 1/26/2023

Data Analytics Fundamentals - Module 3 Project

Domain: Human Resources


"""

# import some modules first - how many can you make use of?

import math
import statistics # importing needed stats module for descriptive and predictive analytics


## Lists 1 -- statistics
print('Lists 1 -- statistics')
print('---------------------')
employee_wage_list = [12, 14, 14, 16, 18, 18, 22, 23, 25, 25, 27, 30, 30, 30, 35, 38, 40, 40, 41, 43]  # creating list1 for task 3
print(f'Employee hourly wage list: {employee_wage_list}')

mean_employee_id_list = statistics.mean(employee_wage_list)
print(f'Mean of employee wages = {mean_employee_id_list}')

median_employee_id_list = statistics.median(employee_wage_list)
print(f'Median of employee wages = {median_employee_id_list}')

mode_employee_id_list = statistics.mode(employee_wage_list)
print(f'Mode of employee wages = {mode_employee_id_list}')


## Lists 2 -- correlation and prediction
print()
print('Lists 2 -- correlation and prediction')
print('-------------------------------------')
workday_hour = list(range(8, 18)) # creating listx for task 3 (hour of the workday in military time)
print(f'Hour of workday list: {workday_hour}')

active_users = sorted((list(range(10,110, 10))), reverse = True) # creating listy for task 3 (active company pc users through workday)
print(f'Active users through workday list: {active_users}')

correlationxy = statistics.correlation(workday_hour, active_users)
print(f'Hour of workday and active user correlation: {correlationxy}')

slope, intercept = statistics.linear_regression(workday_hour, active_users)

new_workday_hour = 18

new_active_user_count = slope * new_workday_hour + intercept # calculating how many users are on for the future hour of 18
print(f'Predicted hour 18 active users: {int(new_active_user_count)}') # predicts 0 active users at hour 18 military time (6pm)


## Lists 3 -- python built-in functions
print()
print('Lists 3 -- python built-in functions')
print('------------------------------------')
print('Employee wage list - python built-in functions:')
min_employee_wages = min(employee_wage_list)
print(f'Min: {min_employee_wages}')

max_employee_wages = max(employee_wage_list)
print(f'Max: {max_employee_wages}')

len_employee_wages = len(employee_wage_list)
print(f'Count: {len_employee_wages}')

sum_employee_wages = sum(employee_wage_list)
print(f'Sum: {sum_employee_wages}')

avg_employee_wages = sum_employee_wages / len_employee_wages
print(f'Average: {avg_employee_wages}')

set_employee_wages = set(employee_wage_list)
print(f'Set: {set_employee_wages}')

asc_employee_wages = sorted(employee_wage_list)
print(f'Asc sort: {asc_employee_wages}')

desc_employee_wages = sorted(employee_wage_list, reverse=True)
print(f'Desc sort: {desc_employee_wages}')


## Lists 4 -- list methods
print()
print('Lists 4 -- list methods')
print('-----------------------')
print('Employee profile detail list -- list methods:')
lst = [1001, 'Joe', 'Bob', 'Service Technician', 'Hourly']
print(lst)

lst.append(26.50)
print(f'Appended hourly rate: {lst}')

lst.extend(['Individual Contributor', 3, 'Darrell', 'Klay'])
print(f'Extending with postion level, years of service, and manager: {lst}')

lst.insert(4, 'Mechanical Service')
print(f'Inserted department at index 4: {lst}')

lst.remove('Mechanical Service')
print(f'Removing department: {lst}')

count_lst_position = lst.count('Service Technician')
print(f'Position count in profile details: {count_lst_position}')

#asc_lst = sorted(lst)      #unable to utlize sort functions due to my list having integers and strings!
#print(asc_lst)

#desc_lst = sorted(lst, reverse=True)
#print(lst)

new_lst = lst.copy()
print(new_lst)

first = new_lst.pop(0)
print(first)

last = new_lst.pop(-1)
print(last)


## Lists 5 -- list transformations (filter and map)
print()
print('Lists 5 -- list transformations (filter and map)')
print('------------------------------------------------')
employee_ids = list(range(1001, 1021))
print(f'List of 20 employee IDs: {employee_ids}')

first_10_employees = list(filter(lambda x: x < 1011, employee_ids))
print(f'Filtered list to first 10 employees: {first_10_employees}')

cbrt_employee_ids = list(map(lambda x: x ** (1/3), employee_ids))   
print(f'Cube root of list: {cbrt_employee_ids}')
                                                            # cube and volume doesn't make sense on employee IDs, but practicing the logic anyway.
volume_employee_ids = list(map(lambda x: x ** 3, employee_ids))
print(f'Cube of list: {volume_employee_ids}')


## Lists 6 -- list transformations (list comprehension)
print()
print('Lists 6 -- list transformations (list comprehension)')
print('----------------------------------------------------')
lower_wages = [rate for rate in employee_wage_list if rate < 18]
print(f'Wages lower than $18/hr in employees_wages list: {lower_wages}')

three_times_wages = [rate*3 for rate in employee_wage_list]
print(f'Wages times 3 results: {three_times_wages}')

overtime_wages =  [rate*1.5 for rate in employee_wage_list] # calculating OT rates (time and a half base rate)
print(f'Respective overtime rate for each employee: {overtime_wages}')

