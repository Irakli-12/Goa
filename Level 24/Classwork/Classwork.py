# 7 kyu
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
# https://www.codewars.com/kata/559590633066759614000063/train/pythondef 
# min_max(lst):
    # return [min(lst), max(lst)]
# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python
# def arithmetic(a, b, operator):
#     if operator == "add":
#         return a + b
#     elif operator == "subtract":
#         return a - b
#     elif operator == "multiply":
#         return a * b
#     elif operator == "divide":
#         return a / b
# https://www.codewars.com/kata/566fc12495810954b1000030/train/python
# def nb_dig(n, d):
#     d = str(d)  
#     count = 0
    
#     for k in range(n + 1):
#         count += str(k**2).count(d) 
    
#     return count
# https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python
# def two_oldest_ages(ages):
#     first, second = float('-inf'), float('-inf')  
#     for age in ages:
#         if age > first:
#             second, first = first, age 
#         elif age > second:
#             second = age 
#     return [second, first]