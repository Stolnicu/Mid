print('Acesta este un mesaj')
print('Check')
print('doi')
# a = input('Apasa tasta R')
# print(a)
print("Elevul 'X' nu si-a facut tema")
print('Elevul "X" nu si-a facut tema') #folosim tipuri de ghilimele diferite pentru start/end si interior
#a = input("Mesaj")
print('double check')
print('Ana are mere \nIon are pere.')
print("""
\tAna are mere
Petre are cuie\n\n""") #3 ghilimele = \n; \t = TAB
variabila1 = 1
variabila2 = 2
variabila3 = f"Ana are {variabila1} mar si {variabila2} pere."
print(variabila3)
variabila4 = "Ana are {1} mar si {0} pere".format(variabila1, variabila2)
print(variabila4)
variabila5 = "Ana are {1} mar si {1} pere".format(variabila1, variabila2)
print(variabila5)
