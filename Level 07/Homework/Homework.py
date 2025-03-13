# 1) კომენტარის სახით ჩამოწერეთ and და or ლოგიკური ოპერატორების ყველა შესაძლო გამოსახულება.
# ამასთანავე, მიუწერეთ თუ რა იქნება თითოეული ოპერაციის შედეგი.
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# 2) ტერმინალში გაშვების გარეშე დაადგინეთ თუ რას გამოიტანს მოცემული კოდი:
# True and False or True or True and False
# ბოლოს კი გაუშვით ეს კოდი და შეამოწმეთ თქვენი ვარაუდი გამართლდა თუ არა.
# True
print(True and False or True or True and False)
# 3) მომხმარებელს შემოატანინე ორი რიცხვი, შეამოწმე არის თუ არა ეს რიცხვები ერთმანეთის ტოლი
# და შედეგი გამოიტანე ტერმინალში. (შედეგი Boolean მნიშვნელობის უნდა იყოს.)
input1 = int(input("Enter Number:"))
input2 = int(input("Enter Number:"))
print(input1 == input2)
# 4) მომხმარებელს შემოატანინე მისი შემაფასებელი ქულა (0-დან 100-ის ჩათვლით).

# • იმ შემთხვევაში თუ შემოტანილი ქულა მეტია ან ტოლია 90-ის, ტერმინალში გამოიტანე "Grade A".
# • თუ მისი ქულა მეტია ან ტოლია 70-ზე გამოიტანე "Grade B". 
# • თუ მომხმარებლის ქულა მეტია ან ტოლია 50-ზე ტერმინალში დაბეჭდე "Grade C"
# • ყველა დანარჩენ შემთხვევაში გამოიტანე  "Grade F"
score = int(input("Your Points Here: "))
if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Grade F")

# 5) მომხმარებელს შემოატანინე მთელი რიცხვი. იმ შემთხვევაში,
# თუ ეს რიცხვი არის ლუწი და ამავდროულად არის 10-ზე მეტი, დაბეჭდე True. ყველა სხვა შემთხვევაში False. 
number1 = int(input("Enter Number: "))
if number1 % 2 == 0 and number1 > 10:
    print(True)
else:
    print(False)