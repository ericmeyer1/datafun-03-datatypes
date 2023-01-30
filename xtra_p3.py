"""
Eric Meyer

Created: 1/30/2023

Data Analytics Fundamentals - Module 3 Project - Bonus

--------------------------

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# reading from hamlet file and getting list of words

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  # split on whitespace

# reading from julius caesar file and getting list of words

with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  # split on whitespace

# Removing duplicates by creating two sorted sets
wordset1 = set(sorted(wordlist1))
wordset2 = set(sorted(wordlist2))

# initializing a variable maxlen = 10
maxlen = 10

# using a list comprension to get a list of words longer than 10
longwordset1 = set([word for word in wordset1 if len(word) > maxlen])

longwordset2 = set([word for word in wordset2 if len(word) > maxlen])

# finding the intersection of the two sets
longwords = longwordset1 & longwordset2

# printing the length of the sets and the list
print(
    f'Number of words in file text_hamlet.txt that are more then 10 characters: {len(longwordset1)}')
print(
    f'Number of words in file text_juliuscaesar.txt that are more then 10 characters: {len(longwordset2)}')
print(
    f'Number of words in files text_hamlet.txt and text_juliuscaesar.txt that are more then 10 characters: {len(longwords)}')
print()
print(f"{sorted(longwords) = }")
print()

# checking work with doctest
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")
