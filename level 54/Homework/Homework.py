# 1) გაიარეთ sololearn'ი map and filter'ის ჩათვლით
# Done
# 2) Use the map function to double the numbers in a list: [2, 4, 6, 8, 10].
list1 = [2, 4, 6, 8, 10]
list1_mapped = list(map(lambda x: x * 2, list1))
print(list1_mapped)
# 3) Write a program using map to concatenate "Hello, " to each name in a list: ["Alice", "Bob", "Charlie"].
list2 = ["Alice", "Bob", "Charlie"]
list2_mapped = list(map(lambda name: "Hello " + name, list2 ))
print(list2_mapped)
# 4) Use map to calculate the lengths of strings in a list: ["apple", "banana", "kiwi"].
list3 = ["apple", "banana", "kiwi"]
list3_mapped = list(map(lambda x: len(x), list3))
print(list3_mapped)
# 5) Use the filter function to keep only positive numbers from a list: [-5, 3, -2, 7, 0, 10].
list4 = [-5, 3, -2, 7, 0, 10]
list4_mapped = list(filter(lambda x: x > 0, list4))
print(list4_mapped)
# 6) Write a program using filter to extract words starting with the letter 
# "p" from a list: ["pear", "apple", "peach", "grape"].
list5 = ["pear", "apple", "peach", "grape"]
list5_mapped = list(filter(lambda x: x.startswith('p'), list5))
print(list5_mapped)

# 7) Use filter to find numbers greater than 50 in a list: [10, 55, 42, 78, 65, 20].
list6 = [10, 55, 42, 78, 65, 20]
list6_mapped = list(filter(lambda x: x > 50, list6))
print(list6_mapped)