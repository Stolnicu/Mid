from collections import Counter  # pentru Problema 2

# Problema 1



# Problema 2

lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']

# Cerinta 1 - sortati lista dupa nume:
lista_nume.sort()
print(lista_nume)

# Cerinta 2 - Determinati numarul de aparitii al fiecarui nume:
print(Counter(lista_nume))

# Cerinta 3 - Listati numele care apare de cele mai multe ori in lista initiala:
print(sorted(set([i for i in lista_nume if lista_nume.count(i) == 3])))

# Cerinta 4 - Listati numele care apare de cele mai putine ori in lista initiala:
print(sorted(set([i for i in lista_nume if lista_nume.count(i) == 1])))
