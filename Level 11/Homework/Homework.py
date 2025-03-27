# 1) შექმენით Number guess game, if else statement-ების გამოყენებით.
number = 5
num1 = int(input("Enter Number You Are Guessing: "))
if number == num1:
    print("You Won!")
else:
    print("You Lose!")
# 2) შექმენით Number guess game, while ციკლების გამოყენებით.
secret_number = 10
guess = 0
while guess != secret_number:
    guess = int(input("Enter Num: ")) 

    if guess == secret_number:
        print("Correct!")
    else:
        print("Uncorrect :(")

# 3) გაიხსენეთ გაკვეთილზე გაკეთებული დავალება მომხმარებლის სისტემაში შესვლის მცდელობაზე 
# და დამოუკიდებლად გააკეთეთ იგივე while ციკლის საშუალებით.

# 4) გადაუარეთ სტრინგს for loop-ით და სტრი გში მხოლოდ ლუწ ინდექსებზე მდგომი ასოები დაბეჭდეთ .

# 5) გამოიყენეთ range და ლუწ ინდექსებზე მდგომი რიცხვები შეკრიბეთ. ჯამი გამოიტანეთ ტერმინალში.