# 1) https://www.codewars.com/kata/55a14f75ceda999ced000048/train/python
def temple_strings(obj, feature): 
    return obj + " are " + feature
# 2) https://www.codewars.com/kata/5966e33c4e686b508700002d
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    
    res = int(a) + int(b)
    return str(res)
# 3) https://www.codewars.com/kata/5810085c533d69f4980001cf
def calculator(a, b, sign):
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))) and sign in ['+', '-', '*', '/']:
        if sign == '+':
            return a + b
        elif sign == '-':
            return a - b
        elif sign == '*':
            return a * b
        elif sign == '/':
            if b == 0:
                return "unknown value"  
            return a / b
    else:
        return "unknown value"
print(calculator(1, 2, "+")) 
print(calculator(1, 2, "&"))  
print(calculator(1, "k", "*"))  