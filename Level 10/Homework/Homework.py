# 1) აუცილებლად გადახედეთ ჩანაწერს;
# Done
# 2) მოიყვანეთ while loop-ის მაგალითი და კომენტარის სახით ახსენით, თუ როგორ მუშაობს while ციკლი;
# ვიწყებთ ცვლადი count-ით
count = 0
# ვქმნიტ while loop-ს
while count < 5:
    # ვპრინტავთ მას
    print(count)
    # ვუმატებთ ყოველ while loop-ის გადავლაზე 1-ს
    count += 1 

# 3) კომენტარის სახით ახსენით თუ რა განსხვავებაა for loop-სა და while loop-ს შორის;
# for loop-ში ვიცით თუ რამდენჯერ განმეორდება ცვლადი, ინტეჯერი, ა.ს.შ. while loop-ში არა

# 4) ცვლადში შეინახეთ პაროლი. შემდეგ მომხმარებელს შემოატანინეთ პაროლი,
# სანამ მომხმარებლის მიერ შემოტანილი პაროლი 
# არ დაემთხვევა თქვენს პაროლს, გამოუტანეთ "Incorrect password. Try again".
# იმ შემთხვევაში თუ ეს პაროლები ერთმანეთს დაემთხვევა გამოიტანეთ 
# "Correct password. You have successfully logged in."
# (გააკეთეთ While ციკლით, არ გამოიყენოთ if else statement-ები.);
# შენახული პაროლი
stored_password = "secure123"
entered_password = ""

while entered_password != stored_password:
    entered_password = input("Enter the password: ")
    print("Incorrect password. Try again.")
print("Correct password. You have successfully logged in.")


# 5) ტერმინალში დაბეჭდეთ რიცხვები 1-დან 20-ის ჩათვლით ორ-ორის გამოტოვებით.
for x in range(1, 20, 2):
    print(x)
# 6) Sololearn-ში გაიარეთ While loops სექცია:
# ScreenShot in folder