# 1) შექმენით ფუნქცია რომელიც მიესალმება ადამიანს
def greet(name):
    print(f"Hello {name}")
print(greet("irakli"))
# 2) შექმენით ფუნქცია რომელიც უსურვებს ადამიანს წარმატებებს
print("წარმატებას გისურვებ")
# 3) შექმენით ფუნქცია რომელიც ადამიანს შეახსენებს რომ GOA'ს გაკვეთილი აქვს
def remember(lesson):
    print(f"{lesson} გაკვეთილი გაქვს")
print(remember("Goa"))
# 4) შექმენით ფუნქცია რომელიც მიიღებს ადამიანის სახელს და გამოიტანს მისალმებას
input1 = input("enter your  name")
def greet(name):
    print(f"Hello {name}")
print(greet(input1))
# 5) შექმენით ფუნქცია რომელიც მიიღებს ადამიანის ასაკს და ეტყვის სრულწლოვანია თუ არა
input2 = int(input("enter your age"))
if input2 >= 18:
    print("სრულწლოვანი ხარ")
else:
    print("არხარ სრულწლოვანი")
# 6) შექმენით ფუნქცია რომელიც მიიღებს ადამიანის ხელფასს და უთხარით ღარიბია, გაწონასწორებული თუ მდიდარი.
def income_status(salary):
    if salary < 1000:
        return "ღარიბი"
    elif 1000 <= salary <= 5000:
        return "გაწონასწორებული"
    else:
        return "მდიდარი"

salary = 3000
status = income_status(salary)
print(f"თქვენი სტატუსი არის: {status}")
