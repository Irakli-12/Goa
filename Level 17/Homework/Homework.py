# 1) თქვენი სიტყვებით ახსენით თუ რაში გვჭირდება ფუნქციების გამოყენება პითონში.
# ფუნქციები საქმეს გვიმარტივებს

# 2) გადახედეთ რესურსს პითონში ფუნქციების შესახებ:
# https://www.w3schools.com/python/python_functions.asp
# Done
# 3) შექმენით ფუნქცია სახელწოდებით double_values რომელიც არგუმენტად მიიღებს სიას და დააბრუნებს ახალ სიას, 
# სადაც თითოეული ელემენტი გაორმაგებული იქნება.
def double_values(lst):
    doubled_list = []  
    for x in lst:  
        doubled_list.append(x * 2)

    return doubled_list

numbers = [1, 2, 3, 4, 5]
numbers1 = double_values(numbers)
print(numbers1)
# 4) შექმენით ფუნქცია, რომელსაც არგუმენტად გადასცემთ სიას (ჩათვალეთ, რომ სიაში ინახება Integer-ი რიცხვები).
#  ამ ფუნქციამ საბოლოოდ უნდა დააბრუნოს სიიდან მხოლოდ ლუწი რიცხვები.
def name(lst):
    numbers_even = []
    for x in lst:
        if x % 2 == 0:
            numbers_even.append(x)
    return numbers_even

nums = [2, 5, 6, 8, 3]
even_nums = name(nums)
print(even_nums)
# 5) შექმენით ფუნქცია და გადაეცით არგუმენტად სია. ფუნქციამ უნდა დააბრუნოს ახალი სია, რომლის თითოეული 
# ელემენტიც უნდა იყოს კვადრატში აყვანილი.
def name1(list2):
    nums42 = []
    for x in list2:
        nums42.append(x ** 2)
    return nums42

list31 = [2, 5, 3, 6, 9]
print(name1(list31))

# 6) შექმენით ფუნქცია და არგუმენტად გადაეცით String-ი. ფუნქციამ ეგრედწოდებულად უნდა 
# "გაფილტროს" ეს სტრინგი თანხმოვანი ასოებისგან და მხოლოდ დააბრუნოს 
# ის ხმოვანი ასოები, რომლებსაც ეს სტრინგი შეიცავს.


# 7) შექმენით ფუნქცია და გადაეცით რიცხვების სია არგუმენტად. ფუნქციის მიზანი იქნება, 
# რომ სიიდან დააბრუნოს მხოლოდ უარყოფითი რიცხვები.

# 8) წინა დავალების ანალოგიურად შექმენით ფუნქცია და გადაეცით რიცხვების სია არგუმენტად. ამ შემთხვევაში
#  ფუნქციის მიზანი იქნება, რომ სიიდან დააბრუნოს მხოლოდ დადებითი რიცხვები.

# 9) შექმენით ფუნქცია და მას პარამეტრად  გადაეცით ერთი რიცხვი. ფუნქციამ უნდა დააბრუნოს ეს რიცხვი 
# აყანილი კვადრატში და გამრავლებული 10-ზე. (ხარისხში აყვანის ოპერატორის შესახებ მოიძიეთ რესურსები, რათა გამოიყენოთ დავალებაში.)

# 10) შექმენით ფუნქცია. მას გადაეცით ორი პარამეტრი: x და y რიცხვები. ფუნქციამ უნდა დააბრუნოს x რიცხვი აყვანილი y ხარისხში.
