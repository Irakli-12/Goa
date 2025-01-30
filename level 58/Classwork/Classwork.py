# 1)https://www.codewars.com/kata/526c7363236867513f0005ca
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
# 2)https://www.codewars.com/kata/559ac78160f0be07c200005a
def name_shuffler(str_):
    name2, name1 = str_.split()
    return f"{name1} {name2}"
# 3)https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e
def shorten_to_date(long_date):
    variable = long_date.split(",")
    return variable[0]
# 4)https://www.codewars.com/kata/529eef7a9194e0cbc1000255
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    return sorted(test) == sorted(original)
# 5)https://www.codewars.com/kata/52fb87703c1351ebd200081f
def what_century(year):
    year = int(year)
    century1 = (year + 99) // 100
    suffix = 'th'  
    
    if century1 % 10 == 1 and century1 % 100 != 11:
        suffix = 'st'
    elif century1 % 10 == 2 and century1 % 100 != 12:
        suffix = 'nd'
    elif century1 % 10 == 3 and century1 % 100 != 13:
        suffix = 'rd'
    
    return f"{century1}{suffix}"