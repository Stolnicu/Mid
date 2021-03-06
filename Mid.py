from collections import Counter  # pentru Problema 2

# Problema 1

string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

# [start, end, text]

patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]


def inlocuire(oldstring, newstring, start_index, end_index, nofail=False):
    # raise an error if index is outside of the string
    # print(nofail, oldstring, start_index, end_index, range(len(oldstring)))
    if not nofail and int(start_index) and int(end_index) not in range(len(oldstring)):
        raise ValueError("index outside given string")

    # if not error, but the index is still not in the correct range
    if start_index < 0:  # add it to the beginning
        return newstring + oldstring

    if end_index > len(oldstring):  # add it to the end
        return oldstring + newstring

    # insert the new string between "slices" of the original
    return oldstring.replace(oldstring[start_index - 1:end_index - 1], newstring)


for patch in patches:
    string = inlocuire(string, patch[2], patch[0], patch[1])
    print(string)
# inlocuire(string, "King", start_index=int(input('Indexul de pornire: ')), end_index=int(input('Indexul de sfarsit: ')))


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
