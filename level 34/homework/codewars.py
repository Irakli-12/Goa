# 8kyu:
# 1) https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"
# 2) https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)
# 3) https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
def zero_fuel(distance_to_pump, mpg, fuel_left):
     return mpg * fuel_left >= distance_to_pump
# 4) https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
def check(seq, elem):
    return elem in seq
# 5) https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python
# 7kyu:
# 1) https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for x in sentence:
        if x in vowels:
            count += 1
    return count
# 2) https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
# 3) https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python