# 1) https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
# def longest(s1, s2):
#     ხ = set(s1 + s2)
#     return ''.join(sorted(ხ))
# 2) https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
# def openOrSenior(data):
#     list =[]
#     for age, hcap in data:
#         if age >= 55 and hcap > 7:
#             list.append('Senior')
#         else: list.append('Open')
#     return list
# 3) https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
# def find_next_square(sq):
#     sqrt=sq**(0.5)
#     if sqrt % 1 == 0:
#         return (sqrt+1)**2
#     return -1
# 4) https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
# def nb_year(p0, percent, aug, p):
#     inhabitants = 0
#     n = 0
#     while inhabitants < p:
#         inhabitants = int(p0 + p0 * (percent/100) + aug)
#         n += 1
#         p0 = inhabitants
#     return n
# 5) https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
# def reverse_words(T):
    # w = T.split(' ')
    # r = []
    # for i in w:
    #     r.append(i[::-1])
    # return ' '.join(r)