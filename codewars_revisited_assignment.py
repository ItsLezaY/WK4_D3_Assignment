# 1) Vowel count

# DESCRIPTION:
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.


# My original solution:

# def get_count(s):
#     vowels = "aeiou"
#     count = 0
    
#     for char in s:
#         if char in vowels:
#             count += 1
    
#     return count



# Adjusted Solution - used set for more efficient check along with list comprehension

# def get_count(s):
#     vowels = set("aeiou")
#     count = sum(1 for char in s if char in vowels)
#     return count



# 2) Find the smallest integer in the array

# DESCRIPTION:
# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.



# My original solution:

# def find_smallest_int(arr):
#     smallest = arr[0]
#     for num in arr:
#         if num < smallest:
#             smallest = num
#     return smallest

# Adjusted SOlution: 
# You can literally just use the min() method to minimize the code to 1 line. (ｏ・_・)ノ”(ノ_<。)

# def find_smallest_int(arr):
#     return min(arr)



# 3) Valid Parentheses

# DESCRIPTION:
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= length of input <= 100

# All inputs will be strings, consisting only of characters ( and ).
# Empty strings are considered balanced (and therefore valid), and will be tested.
# For languages with mutable strings, the inputs should not be mutated.



# My original solution:

# def valid_parentheses(paren_str):
#     empty_list = []

#     for char in paren_str:
#         if char == "(":
#             empty_list.append('(')
#         elif char == ')':
#             if not empty_list:
#                 return False
#             empty_list.pop()
#     return len(empty_list) == 0



# Adjusted Solution: 
# Instead of using an empty list to store valid parentheses, I use a variable to keep track of the count. In terms of time and space complexity, they're similar.

# def valid_parentheses(paren_str):
#     open_count = 0

#     for char in paren_str:
#         open_count += 1 if char == "(" else -1 if char == ")" else 0
#         if open_count < 0:
#             return False

#     return open_count == 0

# Adjusted Solution: 
# You can use the replace() method to replace every "()" with an empty string, so every valid parentheses is removed.

# def valid_parentheses(x):
#     while "()" in x:
#         x = x.replace("()", "")
#     return x == ""






