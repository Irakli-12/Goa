# 1) ჩამოთვალეთ ყველა დღეს ნასწავლი error'ის ტიპი და ახსენით რა რა შემთხვევაში გამოდის
# NameError
# When Variable is not Defined and its putted in Print 

# SyntaxError
# When you wrote something wrongly in code

# IndexError
# for example list has 3 index (0, 1, 2) and you tried to output index[3]

# 2) დაწერეთ ისეთი კოდი სადაც იქნება NameError და გაუმკლავდით try/except'ით
str2 = "hello world"
try:
    print(str3)
except NameError:
    print("Check name of Variable")
# 3) დაწერეთ ისეთი კოდი სადაც იქნება IndexError და გაუმკლავდით try/except'ით
list2 = ["hi", 1]
try:
    print(list2[3])
except IndexError:
    print("Check indexed of List")
# 4) დაწერეთ ისეთი კოდი სადაც იქნება ValueError და გაუმკლავდით try/except'ით
string = int("Value_Error")
try:
    print(string)
except ValueError:
    print("Check Variable's Value")
# 5) კომენტარებით ახსენით რაში გვადგება try/except
# Try/Except გვადგება ისეთი კოდის გამოსწორებაში რომელსაც ერორი აქვს