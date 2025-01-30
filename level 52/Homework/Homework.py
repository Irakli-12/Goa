# 1) გაიარეთ Sololearn'ი Lambda Expressions'ის ჩათვლით
# Done
# 2) შექმენით ცვლადი რომელსაც მნიშვნელობად მისცემთ lambda ფუნქციას რომელიც აბრუნებს 2 სტრინგის ჯამს
lambda_func = lambda s1, s2: s1 + s2
result = lambda_func("Hi ", "World")
print(result)
# 3) შექმენით ცვლადი რომელსაც მნიშვნელობად მისცემთ lambda ფუნქციას რომელიც აბრუნებს 3 რიცხვის ჯამს
lambda_func2 = lambda x, y, c: x + y + c
result1 = lambda_func2(3, 2, 5)
print(result1)
# 4) შექმენით ცვლადი რომელსაც მნიშვნელობად მისცემთ lambda ფუნქციას რომელიც არგუმენტად 
# იღებს list'ს და აბრუნებს მასში მყოფი რიცხვების ჯამს
list1 = [1, 2, 3, 4, 5]
lambda2 = lambda list1: sum(list1)
print(lambda2(list1))
# 5) შექმენით ცვლადი რომელსაც მნიშვნელობად მისცემთ lambda ფუნქციას რომელიც
# არგუმენტად იღებს string'ს და რაიმე სიმბოლოს და აბრუნებს რამდენჯერ მეორდება სიმბოლო string'ში
lambda3 = lambda string, i: string.count(i)
text = "hello world"
character = 'o'
print(lambda3(text, character))

# 6) გააკეთეთ ნებისმიერი 5 ცალი 8 kyu
# Done