# ყველა დავალებაში გამოიყენეთ map ან filter.
# 1) შექმენით რაიმე list'ი რომელშიც იქნება integer'ები და შემდეგ ამოწერეთ მხოლოდ ისეთი რიცხვები რომლებიც მეტია ან ტოლია 40'ის.
list1 = [5, 40, 41, 11, 55]
result1 = list(filter(lambda x: x >= 40, list1))
print(result1)
# 2) შექმენით რაიმე list'ი რომელშიც იქნება integer'ები და შემდეგ გამოიტანეთ list'ი სადაც იქნება ყველა რიცხვის კვადრატი.
list2 = [1, 2, 3, 4, 5]
result2 = list(filter(lambda x: x % 2 == 0, list2))
print(result2)  
# 3) შექმენით რაიმე list'ი რომელშიც იქნება string'ები და შემდეგ ამოწერეთ მხოლოდ ისეთები რომლებიც მთავრდება "a" სიმბოლოთი.
list3 = ["apple", "ia" "banana"]
result3 = list(filter(lambda x: x.endswith("a"), list3))