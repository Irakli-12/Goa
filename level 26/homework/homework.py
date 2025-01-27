# 1) გააკეთეთ sololearn Function Arguments'მდე
# Done
# 2) შექმენით ფუნქცია რომელიც გამოიტანს 2 რიცხვის ჯამს
def plus(a, b):
    print(a + b)
print(plus(5, 5))
# 3) შექმენით ფუნქცია რომელიც გამოიტანს 3 რიცხვის ნამრავლს
def plus(a, b, c):
    print(a * b * c)
print(plus(5, 5, 5))
# 4) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სახელს და გვარს და გამოიტანს მისალმებას
def greetu(name, surname):
    print(f"Hello {name} {surname}")
print(greetu("irakli", "Gegia"))
# 5) შექმენით ფუნქცია რომელიც დააბრუნებს 2 რიცხვის ჯამს, შემდეგ კი დაბრუნებული მნიშვნელობა მიანიჭეთ ცვლადს
def sum_numbers(a, b):
    return a + b
num1 = 10
num2 = 15
total = sum_numbers(num1, num2)
print(f"total is: {total}")
# 6) შექმენით ფუნქცია რომელიც დააბრუნებს 3 რიცხვის ნამრავლს, შემდეგ კი დაბრუნებული მნიშვნელობა მიანიჭეთ ცვლადს
def multiply_three_numbers(a, b, c):
    return a * b * c
num1 = 2
num2 = 3
num3 = 4
product = multiply_three_numbers(num1, num2, num3)
print(f"namravli is: {product}")
