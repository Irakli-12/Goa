# 1) გააკეთეთ sololearn Error Handling თავის Module Quiz'ის ჩათვლით
# Done
# 2) ივარჯიშეთ exception handling'ზე, საკლასო დავალებაში მოცემული დავალებებიდან, მეორედან მეოთხეს ჩათვლით თავიდან გააკეთეთ სხვანაირი მაგალითებით (სხვა ტიპის მაგალითები მოიყვანეთ, უბრალოდ ცვლადის სახელები არ შეცვალოთ)
str2 = "hello world"
try:
    print(str3)
except NameError:
    print("Check name of Variable")
    list2 = ["hi", 1]
try:
    print(list2[3])
except IndexError:
    print("Check indexed of List")
# 3) შექმენით ფუნქცია რომელიც იღებს რიცხვებს, ზოგი იქნება სტრინგი ზოგი იქნება ინტეჯერი (მაგ: [10, "10"]) და გამოიტანეთ მათი ჯამი. (exception'ებს გაუმკლავდით try/except'ის გარეშე. hint: გამარტივებისთვის გამოიყენეთ list comprehension
def sum_mixed_numbers(numbers):
    return sum(int(number) for number in numbers)

numbers = [10, "10"]
finish = sum_mixed_numbers(numbers)
print(finish)

# 4) https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
# def str_count(strng, letter):
    # return strng.count(letter)

# 5) https://www.codewars.com/kata/555a67db74814aa4ee0001b5/train/python

# def is_even(n): 
#   if n % 2 == 0:
#     return True
# else:
#     return False