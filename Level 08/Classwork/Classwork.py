# 1) მომხმარებელს შემოატანინეთ ერთი რიცხვი, შემდეგ შეამოწმეთ არის თუ არა ეგ რიცხვი
# >= 5 და <= 10 (ანუ არის თუ არა 5დან 10შორის დიაპაზონში (შუალედში))
your_num = int(input("Enter Your Number: "))
if your_num >= 5 and your_num <= 10:
    print("Number is between 5 and 10.")
else:
    print("Number isn't between 5 and 10.")