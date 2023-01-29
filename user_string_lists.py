"""
Eric Meyer

Created: 1/28/2023

Data Analytics Fundamentals - Module 3 Project - String Lists

Domain: Human Resources

"""

# imports first

import random


# defining domain lists - employee payroll system profile details

list_postions = ['Service Tech', 'Assembler', 'Engineer', 'Salesman', 'HR Manager']

list_departments = ['Service', 'Production', 'Engineering', 'Sales', 'Administration']

list_pay_format = ['Salary', 'Hourly']

list_work_status = ['Full Time', 'Part Time', 'Seasonal', 'Temporary Full Time']

list_position_level = ['Individual Contributor', 'Manager', 'Director']


# string lists 1 - len, set, and zip

print()
print('string lists 1 - len, set, and zip')
print('----------------------------------')
print('Applying the len function to list_positions shows us:')
position_count = len(list_postions)
print(f'There are {position_count} positions in list_positions.')

print()
print('Using the set function to create a random ordered object from list_departments:')
set_departments = set(list_departments)
print(f'Here is a new set for list_departments: {set_departments}.')

print()
print('Using the zip function to create a tuple:')
employee_combined_details = zip(list_pay_format, list_work_status)
print(f'Here is the tuple for list_pay_format and list_work_status: {list(employee_combined_details)}')


# string lists 2 - random choice

print()
print()
print('string lists 2 - random choice')
print('------------------------------')
print(f'Utilizing random.choice to randomly select a postion from list_positions: {random.choice(list_postions)}')

print()
print(f'John Doe will be in the position of {random.choice(list_postions)} at your company.')
print(f'In this role he will be on {random.choice(list_pay_format)} wages.')


# string lists 3 - get unique words

print()
print()
print('string lists 3 - get unique words')
print('---------------------------------')
with open("text_names_in.txt", "r") as file:
    text = file.read()
    list_words = text.split()  # splits all names on whitespace (creates a list)
    unique_words = set(list_words)  # this set removes duplicates from previous list and creates a random set of the names

sorted_unique_words = sorted(unique_words)
name_count = len(sorted_unique_words)
print(f'The provided text_names_in file has {name_count} unique names!')
print(f"Your baby's random name is.....'{random.choice(sorted_unique_words)}'! Just kidding...you can chose your own baby's name!")
