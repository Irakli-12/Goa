# 1) მიმოიხედეთ ოთახში, აირჩიეთ რაიმე ობიექტი და შექმენით მისი dictionary (მინიმუმ 5 key:value pair უნდა ჰქონდეს)
objects = {
    "object": "Computer",
    "object1": "Keyboard",
    "object2": "Pc",
    "object3": "Chair",
    "object4": "Table"
}
# 2) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს key'ები
for x in objects.keys():
    print(x)

# 3) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს value'ები
for x in objects.values():
    print(x)
# 4) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს key'ები და value'ები ერთად
for x in objects.items():
    print(x)