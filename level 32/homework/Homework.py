# 1) შექმენით manual_sum ფუნქცია
def manual_sum(numbers):
    return sum(numbers)

print(manual_sum([1, 2, 3, 4]))
# 2) შექმენით manual_min 
def manual_min(numbers):
    return min(numbers)

print(manual_min([54, 25, 83, 12]))    
print(manual_min([74, -835, 5, 400])) 
# 8kyu:
# 1) https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m
# 2) https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
# 3) https://www.codewars.com/kata/583710ccaa6717322c000105/train/python
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
# 4) https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
# 5) https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
def invert(lst):
    return [-x for x in lst]