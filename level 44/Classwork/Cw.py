# 1) https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
# def friend(x):
#     names = []
#     for i in x:
#         if len(i) == 4:
#             names.append(i)
#     return names
# 2) https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
# def maskify(cc):
#     ans = []
#     for x in cc[:-4]:
#         x = '#'
#         ans.append(x)
#     return ''.join(ans) + cc[-4:]
# 3) https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
# def add_binary(a,b):
#     return bin(a+b)[2:]
# 4) https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
# def validate_pin(pin):
#     if not pin.isdigit():
#         return False
#     pin_length = len(pin)
#     if pin_length == 4 or pin_length == 6:
#         return True
#     else:
#         return False
# 5) https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
# def is_triangle(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return False
#     else:
#         return a + b > c and a + c > b and b + c > a