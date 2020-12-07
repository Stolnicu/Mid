# print(2 > 3)
# a = None
# if 2 != 3: #nu este egal
#     a = True
# else:
#     a = False
#
# print(a)

# a = False
# b = True
# if a is False:
#     print(a)
#
# a = input('Introdu un numar')
# b = None
# if a.isdigit() or int(a) < 100:
#     b = False
# elif a.isdigit():
#     b = True
# print(b)
#
# nr1 = input('Introdu primul numar: ')
# nr2 = input('INtrodu al doilea numar: ')
# a = None
# if int(nr1) > int(nr2)
#     a = nr1
# else:
#     a = nr2
# print(a)

nr1 = input("Introdu nr1: ")
nr2 = input("Introdu nr2: ")
nr3 = input("Introdu nr3: ")
if nr1.isdigit() and nr2.isdigit() and nr3.isdigit():
    print(max(nr1, nr2, nr3))
else:
    print("NU se poate calcula")
