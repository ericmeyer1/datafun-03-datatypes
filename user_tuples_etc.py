"""
Eric Meyer

Created: 1/30/2023

Data Analytics Fundamentals - Module 3 Project - Tuples and More

Domain: Human Resources

"""

# TUPLES
print('TUPLES')
print('-------------------')

# Creating employee tuples
employee_1 = ('Joe', 'Bob', 'Service Tech', 'Hourly', 25, 'Seasonal')
employee_2 = ('John', 'Guy', 'Engineer', 'Salary', 38, 'Full Time')
employee_3 = ('Sarah', 'Lee', 'Data Analyst', 'Salary', 35, 'Full Time')

print(f'{employee_1 = }')
print(f'{employee_2 = }')
print(f'{employee_3 = }')

# Slicing and concatenating two employee tuples together
print()

ee1_name = employee_1[0:2]
ee3_postion = employee_3[2:]

print(f'{ee1_name = }')
print(f'{ee3_postion = }')

employee_4 = ee1_name + ee3_postion

print(f'Created new employee 4 tuple: {employee_4}')

# Using tuple membership testing to look at an employee's work status
print()

ft_status = 'Full Time' in employee_1
print(f'Employee 1 is a full time employee: {ft_status}')

ft_status2 = 'Full Time' in employee_2
print(f'Employee 2 is a full time employee: {ft_status2}')

ft_status3 = 'Full Time' in employee_3
print(f'Employee 3 is a full time employee: {ft_status3}')

ft_status4 = 'Full Time' in employee_4
print(f'Employee 4 is a full time employee: {ft_status4}')

# Indexing employee 1 tuple and returning each of Joe Bob's profile details
first_name = employee_1[0]
last_name = employee_1[1]
postion = employee_1[2]
pay_format = employee_1[3]
pay_rate = employee_1[4]
work_status = employee_1[-1]

print(f'''
Joe's employee profile details:
      {first_name = }
      {last_name = }
      {postion = }
      {pay_format = }
      {pay_rate = }
      {work_status = }
      '''
      )

# SETS
print()
print('SETS')
print('-------------------')

# Creating two sets
location1_set = {'Joe', 'Frank', 'Sarah', 'Alex', 'Heather'}
location2_set = {'Alex', 'Frank', 'Bob', 'Heather', 'Anna'}

print(f'{location1_set = }')
print(f'{location2_set = }')

# Finding location sets' union and intersection
print()

location_union = location1_set | location2_set
location_intersection = location1_set & location2_set

print(f'{location_union = }')
print(f'{location_intersection = }')

# DICTIONARIES
print()
print()
print('DICTIONARIES')
print('-------------------')

# Counting names in the file text_names_in and creating a dictionary with those values

with open("text_names_in.txt") as name_file:
    name_list = name_file.read().split()

name_counts_dict = {name: name_list.count(name) for name in name_list}

print(f'''Name count in text_names_in file:

{name_counts_dict}
'''
)


